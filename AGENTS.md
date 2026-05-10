# AGENTS.md

이 파일은 WiKi Archive 프로젝트를 관리하는 다양한 LLM Agent들을 위한 공통 지침입니다.

## 핵심 원칙
- 모든 Topic은 독립적인 폴더로 관리됩니다.
- 각 Topic 폴더 내에는 `wiki` 폴더가 존재해야 합니다.
- 각 Topic 폴더 내에는 `HOW-TO-UPDATE.md` 파일이 존재하여 업데이트 절차를 기술해야 합니다.
- `LLM-WiKi` 스킬을 사용하여 위키를 작성하고, `WiKi-Hub` 스킬을 사용하여 GitHub에 백업/동기화합니다.

## 프로젝트 구조
- `.agents/skills/LLM-WiKi`: 위키 작성 스킬 (Submodule)
- `.agents/skills/WiKi-Hub`: 위키 배포/동기화 스킬 (Submodule)
- `[topic-name]/`: 개별 위키 토픽 폴더
  - `wiki/`: 실제 위키 데이터
  - `HOW-TO-UPDATE.md`: 해당 토픽의 업데이트 가이드

## 작업 동기화
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` 파일은 프로젝트의 설정이나 컨벤션이 변경될 때 항상 함께 업데이트되어야 합니다.
