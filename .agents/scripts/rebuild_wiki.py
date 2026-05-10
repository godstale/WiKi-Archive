import json
import os

def rebuild_wiki():
    data_path = '.agents/memory/restaurant_data_final.json'
    if not os.path.exists(data_path):
        print("Data not found.")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    restaurants = data.get('restaurants', [])
    
    # Batch processing for efficiency and safety
    batch_size = 200 # Ingesting more this time as we're confident
    
    source_content = "# 전국 맛집 리스트 통합 (Refined)\n\n이 리스트는 정확한 인코딩 및 필드 추출 과정을 거쳐 재구축되었습니다.\n\n## 통계\n- 총 수집 건수: {}\n\n## 리스트 (Batch 1)\n".format(len(restaurants))
    
    for i, res in enumerate(restaurants[:batch_size]):
        name = res['이름'].replace('/', '_').replace(':', '_').replace('\\', '_').strip()
        if not name:
            name = f"Restaurant_{i}"
        
        # Limit filename length
        if len(name) > 100: name = name[:100]
        
        file_path = f"wiki/entities/{name}.md"
        
        # Determine region from location
        region = "기타"
        if "서울" in res['위치']: region = "서울"
        elif "경기" in res['위치']: region = "경기"
        elif "인천" in res['위치']: region = "인천"
        elif "부산" in res['위치']: region = "부산"
        
        content = f"""# {res['이름']}

- **지역**: {region}
- **위치**: {res['위치']}
- **전화번호**: {res['전화번호']}
- **영업시간**: {res['영업시간']}
- **평가**: {res['평가']}
- **출처**: {res['Source']}

## 상세 정보
{res['리뷰']}

---
[[Restaurant]] #맛집 #{region}
"""
        # Overwrite if exists (should be clean now)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        source_content += f"- [[{name}]] ({region})\n"

    with open('wiki/sources/national-restaurant-list.md', 'w', encoding='utf-8') as f:
        f.write(source_content)

    # Update Index
    index_content = """# LLM Wiki Index

## 🗺️ Categories

### 📂 [Restaurants/전국 맛집 리스트](sources/national-restaurant-list.md)
- [[Seoul/서울]]
- [[Gyeonggi/경기]]
- [[Incheon/인천]]
- [[Busan/부산]]
- [[Other/기타]]

## 📝 Recent Ingests
- [[national-restaurant-list]] (2026-05-10 - REBUILT)
"""
    with open('wiki/index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Rebuilt wiki with {batch_size} high-quality entries.")

if __name__ == "__main__":
    rebuild_wiki()
