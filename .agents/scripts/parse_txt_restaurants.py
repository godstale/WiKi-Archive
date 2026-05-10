import json
import re

def parse_best_restaurant_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract URLs
    urls = re.findall(r'https?://[^\s\n]+', content)
    
    # Extract text-based list (assuming items are separated by newlines and might have some markers)
    # The previous read showed a section after URLs with names.
    text_list = []
    lines = content.split('\n')
    start_collecting = False
    for line in lines:
        if '# 留 ' in line or '# 맛집 리스트' in line:
            start_collecting = True
            continue
        if start_collecting and line.strip():
            text_list.append(line.strip())
            
    return urls, text_list

if __name__ == "__main__":
    urls, text_list = parse_best_restaurant_txt('docs/best-restaurant.txt')
    with open('.agents/memory/source_txt_parsed.json', 'w', encoding='utf-8') as f:
        json.dump({"urls": urls, "text_list": text_list}, f, ensure_ascii=False, indent=2)
    print(f"Parsed {len(urls)} URLs and {len(text_list)} text items from txt file.")
