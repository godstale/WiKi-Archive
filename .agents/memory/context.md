# Project Context

## Overview
WiKi-Archive는 다양한 주제의 정보를 위키 형식으로 정리하고 보존하는 프로젝트입니다. 각 주제는 독립적인 폴더 구조(`[topic]/wiki/`)를 가지며, 자동화된 스크립트를 통해 업데이트됩니다.

## Active Topics
1. **Restaurants**: 전국 맛집 정보 (정규화된 데이터 기반)
2. **AI Reddit Trends**: 일간 AI 관련 레딧 포스트 요약 (7일 보존)
3. **Daily News**: 주요 언론사 및 구글 뉴스의 헤드라인 리포트 (7일 보존) - **NEW**

## Update Strategy
- `ai-reddit-trends`와 `daily-news`는 `.agents/scripts/`의 파이썬 스크립트를 사용하여 일간 업데이트를 수행합니다.
- 7일간의 데이터를 유지하며, 인덱스 파일을 자동으로 갱신합니다.

## Recent Changes (2026-05-12)
- `daily-news` 주제 추가 및 초기 데이터 생성.
- `update_daily_news.py` 스크립트 구현.
- 루트 `index.md`에 `daily-news` 추가.
