# Wiki Archive Index

본 저장소의 통합 인덱스입니다. 각 주제별 위키로 이동하려면 아래 링크를 참조하세요.

## 주제별 위키 (Topics)

- [맛집 (Restaurants)](restaurants/wiki/index.md): 전국 맛집 정보 위키
- [AI 레딧 트렌드 (AI Reddit Trends)](ai-reddit-trends/wiki/index.md): 일간 AI 소식 및 트렌드 요약 위키


## 위키 관리 구조

```text
Project-Root/
├── [topic-name]/        # 주제별 루트 (독립 리포지토리/서브모듈 가능)
│   └── wiki/            # 실제 위키 콘텐츠
│       ├── entities/
│       ├── sources/
│       └── index.md
└── index.md             # 통합 인덱스 (이 파일)
```
