# Task History
`n## 2026-05-10
- Wiki-Hub 호환성을 위해 구조 재편: [topic]/wiki 패턴 적용 (restaurants/wiki)
- GEMINI.md 및 wiki-generation.md 지침 업데이트
- 통합 index.md 생성
`n- Fixed syntax error in WSL /root/.bashrc (unclosed quote/trailing backslash on line 105).

## 2026-05-12
### Added New Topic: AI Reddit Trends
- Created i-reddit-trends/wiki/ structure.
- Generated first daily report (2026-05-12) by summarizing AI subreddits.
- Implemented .agents/scripts/update_ai_reddit.py for 7-day rolling retention.
- Updated root index.md.
- AI-Reddit-Trends 위키 검사 및 수정. index.md를 AI-Reddit-Trends.md로 변경하고 링크 구조를 정규화함. AGENTS.md 및 GEMINI.md에 주제별 격리(Topic Isolation) 지침을 추가함.
- AI-Reddit-Trends 위키 진입점을 index.md로 복구하여 독립적 토픽 호환성 확보. 개별 리포트의 백링크를 [[index]]로 수정함.
- 토픽 업데이트 시 HOW-TO-UPDATE.md 지침 준수 룰을 AGENTS.md 및 GEMINI.md에 명문화함.
