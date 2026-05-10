# AGENTS.md

이 파일은 WiKi Archive 프로젝트를 관리하는 모든 LLM 에이전트(Claude, Gemini 등)를 위한 **통합 표준 운영 절차서(SOP)**입니다.

## 1. 핵심 원칙 (Core Mandates)
- **계층적 지침 준수:** 루트의 지침을 따르되, 하위 폴더(`[topic]/CLAUDE.md` 등)의 구체적 지침이 있을 경우 이를 우선합니다.
- **점진적 공개 (Progressive Disclosure):** 모든 정보를 한곳에 담지 않고, 주제별로 분리된 `.claude/rules/` 또는 `.cursor/rules/` 파일을 필요할 때만 참조합니다.
- **자동 동기화:** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`는 프로젝트 컨벤션 변경 시 반드시 세트로 업데이트되어야 합니다.

## 2. 프로젝트 구조 및 관리 방식
- **Topic 독립성:** 각 Topic은 별도 폴더로 관리하며, 내부에는 `wiki/` 폴더와 `HOW-TO-UPDATE.md`가 필수입니다.
- **스킬 활용:** `.agents/skills/` 하위의 `LLM-WiKi`, `WiKi-Hub`를 도구로 사용하여 위키를 생성하고 동기화합니다.
- **메모리 관리:** 에이전트의 실수나 새로운 인사이트는 즉시 해당 에이전트 가이드 또는 `.claude/rules/`에 반영하여 '가차(Gotchas)' 목록을 관리합니다.

## 3. 에이전트별 특화 가이드
- **Claude:** `CLAUDE.md` 및 `.claude/rules/*.md` 참조. YAML 프론트매터 기반의 조건부 로딩 활용.
- **Gemini:** `GEMINI.md` 참조. 프로젝트 목적(`PROJECT_PURPOSE.md`) 기반의 장기적 컨텍스트 유지.

## 4. 검증 및 품질 관리
- 작업 결과물은 반드시 `LLM-WiKi`의 검증 절차를 거쳐야 하며, `WiKi-Hub`를 통한 배포 전 상태를 확인해야 합니다.
