# AGENTS.md

이 파일은 WiKi Archive 프로젝트를 관리하는 모든 LLM 에이전트를 위한 **통합 표준 운영 절차서(SOP)**입니다.

## 1. 핵심 원칙 (Core Mandates)
- **중립적 관리:** 특정 에이전트에 종속되지 않도록 모든 규칙과 메모리는 `.agents/` 폴더에서 관리합니다.
- **주제별 격리 (Topic-Scoped Operations):** 모든 작업은 요청된 특정 주제(Topic) 폴더를 기준으로 수행하며, 명시적 지시 없이 타 주제의 위키를 수정하지 않습니다.
- **업데이트 지침 준수 (Follow Local Guides):** 주제(Topic)를 업데이트할 때는 해당 폴더 내의 `HOW-TO-UPDATE.md` 파일을 가장 먼저 확인하고 해당 지침을 엄격히 준수합니다.
- **점진적 공개 (Progressive Disclosure):** `.agents/rules/`의 세부 지침을 필요할 때만 참조하여 컨텍스트 효율을 극대화합니다.
- **지속적 학습 (Memory Strategy):** 작업 중 발생하는 오류, 수정 사항, 중요한 결정은 `.agents/memory/`에 기록하여 동일한 실수를 방지합니다.

## 2. 에이전트 전용 디렉토리 (.agents/)
- **rules/**: 모든 에이전트가 공유하는 상황별/도메인별 규칙.
- **memory/**: 에이전트의 작업 이력, 오류 수정 노하우, 도메인 지식 축적.
  - `history.md`: 주요 작업 이력 및 결정 사항.
  - `error_fixes.md`: 발생했던 오류와 그에 대한 해결책 (Gotchas).
  - `context.md`: 프로젝트의 현재 상태 및 장기 컨텍스트.
- **skills/**: 위키 작성 및 배포를 위한 서브모듈 도구들.

## 3. 작업 동기화 및 업데이트
- 프로젝트의 근간이 되는 목표나 컨벤션은 `PROJECT_PURPOSE.md`를 대체하는 `.agents/memory/context.md`를 기준으로 합니다.
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`는 항상 동기화된 상태를 유지해야 합니다.
