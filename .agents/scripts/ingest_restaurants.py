import json
import os

def create_wiki_pages():
    data_path = '.agents/memory/restaurant_data_normalized.json'
    if not os.path.exists(data_path):
        print("Data not found.")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    restaurants = data.get('restaurants', [])
    
    # Create wiki directories if they don't exist
    os.makedirs('wiki/entities', exist_ok=True)
    os.makedirs('wiki/sources', exist_ok=True)

    # Create a source page for the project
    source_content = "# 전국 맛집 리스트 통합 소스\n\n이 페이지는 다양한 소스(CSV, PDF, 웹)에서 수집된 맛집 정보의 통합 리스트입니다.\n\n## 수집 통계\n- 총 맛집 수: {}\n\n## 상세 리스트\n".format(len(restaurants))
    
    # Process only a subset for the first batch to avoid huge files/context
    batch_limit = 100 
    for i, res in enumerate(restaurants[:batch_limit]):
        name = res['이름'].replace('/', '_').replace(':', '_').strip()
        if not name:
            name = f"Unknown_Restaurant_{i}"
            
        file_path = f"wiki/entities/{name}.md"
        content = f"""# {res['이름']}

- **지역**: {res['지역']}
- **위치**: {res['위치']}
- **전화번호**: {res['전화번호']}
- **영업시간**: {res['영업시간']}
- **평가**: {res['평가']}

## 리뷰/설명
{res['리뷰']}

---
[[Restaurant]] #맛집 #{res['지역'] if res['지역'] else '전국'}
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        source_content += f"- [[{name}]] ({res['위치']})\n"

    with open('wiki/sources/national-restaurant-list.md', 'w', encoding='utf-8') as f:
        f.write(source_content)

    print(f"Created {batch_limit} restaurant pages and the source index.")

if __name__ == "__main__":
    create_wiki_pages()
