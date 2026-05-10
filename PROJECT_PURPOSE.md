## 프로젝트의 목표

아래 링크에 있는 LLM-WiKi 스킬로 작성된 지식 베이스(wiki 폴더)는 wiki-hub 스킬을 이용해서 github 기반으로 공유, 업데이트, 백업 할 수 있습니다.
- https://github.com/godstale/LLM-WiKi
- https://github.com/godstale/WiKi-Hub

Wiki Archive 프로젝트는 많은 사용자들이 필요로하는 wiki 지식 베이스를 미리 만들어두고 주기적으로 업데이트 해서 제공하기 위해 만든 프로젝트 입니다.
따라서 내부에 llm-wiki, wiki-hub 스킬을 submodule 로 포함해서(.agents/skills 폴더에) 같이 연동되는 것을 염두에 두고 개발을 진행합니다. WiKi Archive 프로젝트는 아래 github repo 와 연결해야 합니다.
- https://github.com/godstale/WiKi-Archive

## WiKi Archive 프로젝트는 아래와 같이 관리합니다.
- 만들려고 하는 wiki 주제(topic)별로 폴더를 만들고 그 안에 wiki 폴더를 만듭니다. 
- 그리고 이 topic 폴더에 llm-wiki 스킬을 적용하여 wiki 를 작성합니다.
- topic 위키 작성이 끝나면 wiki-hub 스킬을 적용하여 wiki 를 github 에 백업합니다.
- WiKi-Archive repo 하나에 여러개의 topic wiki 를 만들어서 wiki-hub 로 배포하므로, 이렇게 배포가 가능한지 확인하는 테스트가 필요합니다.
- 주기적으로 현재 프로젝트에 생성된 topic wiki 들이 최신 내용으로 업데이트를 해야합니다. 따라서 각 topic 안에는 작업을 어떻게 수행해야 하는지를 기술한 HOW-TO-UPDATE.md 파일을 추가해야 합니다. 그래야 나중에 사용자 또는 cron agent 의 간단한 명령만으로 업데이트 작업을 수행할 수 있습니다.
- 따라서 claude, gemini, hermes 같은 LLM 모델을 기반으로 하는 agent 라도 이 WiKi-Archive 프로젝트의 특정 topic wiki 를 쉽게 작성 및 업데이트할 수 있어야 합니다.

## WiKi Archive 프로젝트에 Topic 을 생성하고 업데이트 하는 과정
- 사용자가 특정 문서, 이미지, 영상 등을 입력하는 경우
  - 해당하는 토픽이 없다면 topic 을 생성 (이미 존재한다면 그 topic 의 폴더로 이동)
  - 입력한 리소스의 내용을 wiki 에 등록
- 사용자가 특정 URL 을 입력하는 경우
  - 해당하는 토픽이 없다면 topic 을 생성 (이미 존재한다면 그 topic 의 폴더로 이동)
  - 입력한 URL 의 내용을 추출
  - 추출한 내용을 wiki 에 등록

## WiKi Archive 기본 토픽
- 일반 트렌드 요약
  - daily 뉴스
  - 커뮤니티 (딴지, 클리앙, 다모앙, 뽐뿌 등)
  - 주식 
  - 유투브 인기 영상
- AI 트렌드
  - 레딧 AI 관련 서브레딧
  - AI 툴 정보
  - AI 툴 사용 팁
  
