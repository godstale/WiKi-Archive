# How to Update Daily News

이 위키는 매일의 뉴스 헤드라인을 자동으로 수집하여 리포트를 생성합니다.

## 1. 업데이트 절차
1. `.agents/scripts/update_daily_news.py` 스크립트를 실행합니다.
   ```powershell
   python .agents/scripts/update_daily_news.py
   ```
2. 스크립트는 아래 URL에서 정보를 수집합니다.
   - https://www.yna.co.kr/
   - https://news.google.com/home?hl=ko&gl=KR&ceid=KR%3Ako
3. 수집된 정보는 `daily-news/wiki/entities/YYYY-MM-DD.md` 파일로 저장됩니다.
4. 최근 7일간의 데이터만 유지되며, 오래된 데이터는 자동으로 삭제됩니다.

## 2. 수집 정보 및 지침
- **헤드라인 (Headline)**
- **출처 (Source)**
- **작성시간 (Timestamp)**
- **URL (상세 페이지)**
  - **주의**: URL은 반드시 해당 뉴스의 **상세 내역 페이지 URL**이어야 합니다.
  - **효율성**: 뉴스 메인 페이지(인덱스)의 각 헤드라인 링크(`href`)에서 상세 페이지 URL을 직접 추출하여 저장합니다. 불필요하게 모든 상세 페이지를 일일이 방문하여 토큰을 낭비하지 않도록 합니다.

## 3. 유지관리
- 데이터 보존 기간: 7일
- `index.md`는 최신 리포트와 아카이브 목록을 자동으로 업데이트합니다.
