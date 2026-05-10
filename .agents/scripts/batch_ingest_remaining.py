import json
import os
import re

def clean_filename(name):
    # Replace /, :, \ with _
    name = re.sub(r'[/:\\?*|"<>]', '_', name)
    # Limit length to 100
    return name[:100].strip()

def get_region(location):
    if not location:
        return "전국"
    # Extract first part of address (e.g. 서울특별시, 경기도)
    parts = location.split()
    if parts:
        region = parts[0]
        # Normalize common regions
        if "서울" in region: return "서울"
        if "경기" in region: return "경기"
        if "인천" in region: return "인천"
        if "강원" in region: return "강원"
        if "충청북도" in region or "충북" in region: return "충북"
        if "충청남도" in region or "충남" in region: return "충남"
        if "전라북도" in region or "전북" in region: return "전북"
        if "전라남도" in region or "전남" in region: return "전남"
        if "경상북도" in region or "경북" in region: return "경북"
        if "경상남도" in region or "경남" in region: return "경남"
        if "부산" in region: return "부산"
        if "대구" in region: return "대구"
        if "광주" in region: return "광주"
        if "대전" in region: return "대전"
        if "울산" in region: return "울산"
        if "세종" in region: return "세종"
        if "제주" in region: return "제주"
        return region
    return "전국"

def ingest_all():
    data_path = '.agents/memory/restaurant_data_final.json'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    restaurants = data.get('restaurants', [])
    total_count = len(restaurants)
    print(f"Total records in JSON: {total_count}")
    
    os.makedirs('wiki/entities', exist_ok=True)
    os.makedirs('wiki/sources', exist_ok=True)
    
    # Process records from 200 onwards
    remaining = restaurants[200:]
    created_count = 0
    
    for i, res in enumerate(remaining):
        name = res.get('이름', 'Unknown')
        location = res.get('위치', '')
        region = get_region(location)
        phone = res.get('전화번호', '')
        hours = res.get('영업시간', '')
        rating = res.get('평가', '')
        source = res.get('Source', '')
        review = res.get('리뷰', '')
        
        filename = clean_filename(name)
        if not filename:
            filename = f"Unknown_{200 + i}"
            
        file_path = f"wiki/entities/{filename}.md"
        
        content = f"""# {name}
- **지역**: {region}
- **위치**: {location}
- **전화번호**: {phone}
- **영업시간**: {hours}
- **평가**: {rating}
- **출처**: {source}

## 상세 정보
{review}

---
[[Restaurant]] #맛집 #{region}
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        created_count += 1
        if created_count % 500 == 0:
            print(f"Created {created_count} files...")

    # Rebuild source index with ALL restaurants
    source_path = 'wiki/sources/national-restaurant-list.md'
    source_content = [
        "# 전국 맛집 리스트 통합 (Refined)",
        "",
        "이 리스트는 정확한 인코딩 및 필드 추출 과정을 거쳐 재구축되었습니다.",
        "",
        "## 통계",
        f"- 총 수집 건수: {total_count}",
        "",
        "## 전체 리스트"
    ]
    
    for i, res in enumerate(restaurants):
        name = res.get('이름', 'Unknown')
        filename = clean_filename(name)
        if not filename:
            filename = f"Unknown_{i}"
        location = res.get('위치', '')
        region = get_region(location)
        source_content.append(f"- [[{filename}]] ({region})")
        
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(source_content))
            
    print(f"Successfully created {created_count} restaurant pages and updated the source index.")

if __name__ == "__main__":
    ingest_all()
