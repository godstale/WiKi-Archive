#!/usr/bin/env bash
#=============================================================================
# register-cron.sh — Hermes 크론잡 등록 래퍼 스크립트
#
# 외부 에이전트(geminiCLI, Claude Code 등)가 Hermes Gateway의 cron 스케줄러에
# 정기 작업을 등록할 수 있도록 하는 CLI 인터페이스입니다.
#
# 사용법:
#   bash .agents/scripts/register-cron.sh \
#     --schedule "0 9 * * *" \
#     --name "my-job" \
#     --prompt "정기적으로 실행할 작업 설명" \
#     --workdir "/path/to/project" \
#     --deliver "telegram:-1001234567890" \
#     [--repeat N] \
#     [--skill "skill-name"] \
#     [--no-agent]
#
# 필수 인자:
#   --schedule | -s   실행 스케줄 (예: "30m", "every 2h", "0 9 * * *")
#   --name     | -n   작업 이름 (식별용)
#   --prompt   | -p   작업 프롬프트 (수행할 작업 설명)
#
# 선택 인자:
#   --workdir  | -w   작업 디렉토리 (AGENTS.md 로드됨)
#   --deliver  | -d   배송 대상 (기본값: origin)
#   --repeat   | -r   반복 횟수 (기본값: forever)
#   --skill    | -k   첨부할 스킬 이름 (여러 번 지정 가능)
#   --no-agent | -n   에이전트 없이 스크립트만 실행
#   --script   | -x   실행할 스크립트 경로
#
# 예시:
#   bash .agents/scripts/register-cron.sh \
#     --schedule "0 7,19 * * *" \
#     --name "ai-reddit-trends" \
#     --prompt "Reddit AI 트렌드를 수집하여 위키에 저장하세요." \
#     --workdir "/mnt/c/___Workspace/Projects/WiKi-Archive" \
#     --deliver "origin"
#
# 주의:
# - cron 시간은 시스템 시간(KST) 기준입니다.
# - --workdir을 설정하면 해당 디렉토리의 AGENTS.md/CLAUDE.md가 주입됩니다.
# - 프롬프트는 자체 완결적(self-contained)이어야 합니다.
#=============================================================================

set -euo pipefail

# === 인자 파싱 ===
SCHEDULE=""
NAME=""
PROMPT=""
WORKDIR=""
DELIVER="origin"
REPEAT=""
SKILLS=()
NO_AGENT=""
SCRIPT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --schedule|-s)  SCHEDULE="$2";  shift 2 ;;
    --name|-n)      NAME="$2";      shift 2 ;;
    --prompt|-p)    PROMPT="$2";    shift 2 ;;
    --workdir|-w)   WORKDIR="$2";   shift 2 ;;
    --deliver|-d)   DELIVER="$2";   shift 2 ;;
    --repeat|-r)    REPEAT="$2";    shift 2 ;;
    --skill|-k)     SKILLS+=("$2"); shift 2 ;;
    --no-agent)     NO_AGENT="--no-agent"; shift ;;
    --script|-x)    SCRIPT="$2";    shift 2 ;;
    --help|-h)
      head -50 "$0" | grep "^#" | sed 's/^#//'
      exit 0
      ;;
    *)
      echo "❌ 알 수 없는 인자: $1"
      echo "사용법: bash $0 --help"
      exit 1
      ;;
  esac
done

# === 검증 ===
if [[ -z "$SCHEDULE" ]]; then
  echo "❌ --schedule 인자는 필수입니다."
  exit 1
fi

if [[ -z "$NAME" ]]; then
  echo "❌ --name 인자는 필수입니다."
  exit 1
fi

if [[ -z "$PROMPT" && -z "$SCRIPT" ]]; then
  echo "❌ --prompt 또는 --script 중 하나는 필수입니다."
  exit 1
fi

# === hermes cron create 명령어 구성 ===
CMD="hermes cron create"

CMD+=" '${SCHEDULE}'"

if [[ -n "$PROMPT" ]]; then
  # 프롬프트를 임시 파일로 저장하여 인용 문제 회피
  PROMPT_FILE=$(mktemp)
  echo "$PROMPT" > "$PROMPT_FILE"
  CMD+=" \"\$(cat ${PROMPT_FILE})\""
fi

CMD+=" --name '${NAME}'"
CMD+=" --deliver '${DELIVER}'"

if [[ -n "$WORKDIR" ]]; then
  CMD+=" --workdir '${WORKDIR}'"
fi

if [[ -n "$REPEAT" ]]; then
  CMD+=" --repeat '${REPEAT}'"
fi

for SKILL in "${SKILLS[@]}"; do
  CMD+=" --skill '${SKILL}'"
done

if [[ -n "$NO_AGENT" ]]; then
  CMD+=" $NO_AGENT"
fi

if [[ -n "$SCRIPT" ]]; then
  CMD+=" --script '${SCRIPT}'"
fi

# === 실행 ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Hermes Cron Job 등록"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  이름:      $NAME"
echo "  스케줄:    $SCHEDULE"
echo "  배송:      $DELIVER"
echo "  디렉토리:  ${WORKDIR:-"(기본값)"}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

eval "$CMD"
EXIT_CODE=$?

if [[ -n "${PROMPT_FILE:-}" ]]; then
  rm -f "$PROMPT_FILE"
fi

if [[ $EXIT_CODE -eq 0 ]]; then
  echo ""
  echo "✅ 크론잡 등록 완료: $NAME"
else
  echo ""
  echo "❌ 크론잡 등록 실패 (exit code: $EXIT_CODE)"
fi

exit $EXIT_CODE
