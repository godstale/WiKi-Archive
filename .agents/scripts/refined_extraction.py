import pandas as pd
import json
import os
import re
import pdfplumber

def clean_name(name):
    if not name: return ""
    return re.sub(r'\s+', ' ', str(name)).strip()

def process_csv():
    path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    results = []
    try:
        # CP949 is common for Korean Excel-exported CSVs
        df = pd.read_csv(path, encoding='cp949')
        for _, row in df.iterrows():
            name = clean_name(row.get('상호명', ''))
            if name:
                results.append({
                    "이름": name,
                    "지역": "",
                    "위치": clean_name(row.get('주소', '')),
                    "전화번호": "",
                    "영업시간": "",
                    "평가": "",
                    "리뷰": f"주요메뉴: {row.get('주요메뉴', '')}",
                    "Source": "CSV"
                })
    except Exception as e:
        print(f"CSV Error: {e}")
    return results

def process_pdf():
    path = 'docs/전국맛집리스트2022.pdf'
    results = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text: continue
                lines = text.split('\n')
                for line in lines:
                    # PDF Pattern observed: Name | Menu/Phone | Address
                    # Looking at raw output: "상호명, 메뉴, 주소" pattern exists in some lines
                    # We need a more robust parser. Many lines have phone numbers.
                    phone_match = re.search(r'\d{2,4}-\d{3,4}-\d{4}', line)
                    if phone_match:
                        phone = phone_match.group()
                        parts = line.split(phone)
                        name_part = parts[0].strip()
                        addr_part = parts[1].strip() if len(parts) > 1 else ""
                        
                        # Extract name from name_part (it might contain index or menu)
                        # Example: "1. 식당이름 메뉴"
                        name = re.sub(r'^\d+[\.\s]+', '', name_part).split(' ')[0]
                        if name and len(name) > 1:
                            results.append({
                                "이름": name,
                                "지역": "",
                                "위치": addr_part,
                                "전화번호": phone,
                                "영업시간": "",
                                "평가": "",
                                "리뷰": f"Raw: {line}",
                                "Source": "PDF"
                            })
    except Exception as e:
        print(f"PDF Error: {e}")
    return results

if __name__ == "__main__":
    csv_data = process_csv()
    pdf_data = process_pdf()
    
    all_data = csv_data + pdf_data
    valid_data = [res for res in all_data if res['이름']]
    
    with open('.agents/memory/restaurant_data_refined.json', 'w', encoding='utf-8') as f:
        json.dump({"restaurants": valid_data}, f, ensure_ascii=False, indent=2)
    
    print(f"Refined Extraction: {len(valid_data)} restaurants found.")
    print(f"Sample: {valid_data[0] if valid_data else 'None'}")
