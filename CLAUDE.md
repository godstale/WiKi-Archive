# CLAUDE.md

프로젝트 루트의 핵심 매뉴얼입니다. 세부 규칙은 `.claude/rules/`를 참조하세요.

## 1. 빌드 및 테스트 (Build & Test)
- **위키 생성:** `LLM-WiKi` 스킬의 지침에 따라 실행.
- **동기화/배포:** `WiKi-Hub` 스킬의 지침에 따라 실행.

## 2. 코드 및 문서 스타일
- **문서 포맷:** 모든 위키 및 가이드는 Markdown 형식 준수.
- **언어:** 사용자 요청이 없는 한 한국어 작성을 원칙으로 함.

## 3. 계층적 메모리 전략
- **루트 CLAUDE.md:** 글로벌 안내 (30~70줄 유지).
- **하위 CLAUDE.md:** 특정 Topic 폴더 내 세부 지침.
- **조건부 규칙:** `.claude/rules/` 폴더 내 주제별 규칙 활용.

## 4. 핵심 참조 파일 (Important References)
- @AGENTS.md: 에이전트 통합 SOP.
- @PROJECT_PURPOSE.md: 프로젝트의 궁극적 목표.
- `.claude/rules/wiki-generation.md`: 위키 생성 세부 규칙.
- `.claude/rules/git-workflow.md`: 서브모듈 및 Git 작업 규칙.

## 5. 가차 (Gotchas - 클로드의 실수 방지)
- 서브모듈 경로(`.agents/skills/`)를 무시하고 루트에 직접 설치하지 말 것.
- `WiKi-Hub` 실행 전 원격 저장소(`origin`) 설정을 반드시 확인할 것.
