---
description: Git 작업, 서브모듈 관리 및 WiKi-Hub 동기화에 관한 지침. 사용자가 git 명령을 실행하거나 위키를 배포하려 할 때 적용됨.
pattern: "**/*"
---

# Git 및 서브모듈 워크플로우

## 1. 서브모듈 관리
- 스킬은 반드시 `.agents/skills/` 폴더 내의 서브모듈로 관리합니다.
- 서브모듈 업데이트 시 `git submodule update --remote`를 사용합니다.

## 2. WiKi-Hub 동기화
- 위키 작성이 완료되면 `WiKi-Hub` 스킬을 호출하여 GitHub에 반영합니다.
- 커밋 메시지는 `topic: [topic-name] update wiki contents` 형식을 권장합니다.

## 3. 안전 모드 (Gotchas)
- `origin` 리포지토리가 `https://github.com/godstale/WiKi-Archive`인지 확인 후 Push 하십시오.
- 대규모 변경 전에는 반드시 브랜치를 생성하여 작업하십시오.
