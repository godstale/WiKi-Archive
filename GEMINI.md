# GEMINI.md

Gemini 에이전트를 위한 실행 가이드입니다. 통합 지침은 `AGENTS.md`를 참조하세요.

## 1. 운영 전략
- **SOP 준수:** `.agents/` 폴더 내의 규칙과 메모리를 기반으로 작업합니다.
- **주제별 관리 (Multi-Topic):** 각 주제는 `[topic-name]/wiki/` 구조로 관리합니다. 이는 `wiki-hub`를 통한 독립적인 주제 공유 및 배포를 위함입니다.
  - 예시: `restaurants/wiki/`, `travel/wiki/`
  - 각 주제 폴더 내부의 `wiki/` 폴더가 실제 위키 콘텐츠(entities, sources 등)를 포함합니다.
- **이력 관리:** 작업 완료 후 `.agents/memory/history.md`에 수행 내용을 요약 기록합니다.

## 2. 메모리 관리
- 오류 발생 시 원인 분석과 해결 과정을 `.agents/memory/error_fixes.md`에 업데이트하여 지능적인 협업을 유지합니다.
- 복잡한 작업 전에는 `.agents/memory/context.md`를 최신화하여 장기 컨텍스트를 보존합니다.

## 3. 핵심 참조
- @AGENTS.md: 통합 SOP.
- @.agents/memory/context.md: 프로젝트 목표 및 현황.

## 4. 효율성 및 성능 최적화
- **Sub-Agent 적극 활용:** 본 프로젝트(Wiki-Archive)는 대량의 데이터를 정규화하고 수천 개의 위키 페이지를 생성하는 등 단순 반복 작업이 많습니다. 토큰 절약과 작업 속도 향상을 위해 `invoke_agent`를 통한 sub-agent 위임을 적극 권장하며, 특히 배치 파일 생성, 대규모 린팅, 그래프 빌드 등의 작업은 sub-agent에게 맡겨 메인 컨텍스트를 가볍게 유지합니다.
