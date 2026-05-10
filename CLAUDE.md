# CLAUDE.md

Claude 에이전트를 위한 실행 가이드입니다. 통합 지침은 `AGENTS.md`를 참조하세요.

## 1. 규칙 참조 (Rules)
- `.agents/rules/` 폴더의 마크다운 파일을 참조합니다.
- Claude Code의 경우, 파일 상단의 YAML 프론트매터를 분석하여 필요한 규칙을 자동으로 로드합니다.

## 2. 메모리 활용 (Memory)
- 세션 시작 시 `.agents/memory/context.md`를 읽어 프로젝트 현황을 파악합니다.
- 작업 중 실수가 발생하거나 새로운 패턴을 학습하면 `.agents/memory/error_fixes.md`에 기록합니다.

## 3. 핵심 참조
- @AGENTS.md: 통합 SOP.
- @.agents/memory/context.md: 프로젝트 목표 및 현황 (PROJECT_PURPOSE.md 대체).
