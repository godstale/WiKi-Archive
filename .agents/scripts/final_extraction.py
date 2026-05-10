import pandas as pd
import json
import os
import re
import pdfplumber
import requests
from bs4 import BeautifulSoup

def clean_text(text):
    if not text: return ""
    # Remove excessive whitespaces and newlines
    return re.sub(r'\s+', ' ', str(text)).strip()

def process_csv():
    path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    results = []
    try:
        df = pd.read_csv(path, encoding='cp949')
        for _, row in df.iterrows():
            # CSV Columns: 등록번호, 상호, 업종, 주소, 메뉴, 영업시간, 주차정보, 제안수, 댓글수
            name = clean_text(row.get('상호', ''))
            if name:
                results.append({
                    "이름": name,
                    "지역": "", # Will fill later or leave blank
                    "위치": clean_text(row.get('주소', '')),
                    "전화번호": "",
                    "영업시간": clean_text(row.get('영업시간', '')),
                    "평가": clean_text(row.get('제안수', '')),
                    "리뷰": f"메뉴: {row.get('메뉴', '')}, 주차: {row.get('주차정보', '')}",
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
                    # Pattern: Name Menu/Category Phone Address
                    # Example: 가온 곰국시, 떡만두국 02-3436-7100 서울특별시 광진구 아차산로78길 75
                    phone_match = re.search(r'(\d{2,4}-\d{3,4}-\d{4})', line)
                    if phone_match:
                        phone = phone_match.group(1)
                        parts = line.split(phone)
                        prefix = parts[0].strip()
                        address = parts[1].strip() if len(parts) > 1 else ""
                        
                        # Prefix usually has "Name Category"
                        # We'll take the first word as the name if it's not a number
                        prefix_words = prefix.split(' ')
                        name = prefix_words[0]
                        category = " ".join(prefix_words[1:]) if len(prefix_words) > 1 else ""
                        
                        if name and not name.isdigit():
                            results.append({
                                "이름": name,
                                "지역": "",
                                "위치": address,
                                "전화번호": phone,
                                "영업시간": "",
                                "평가": "",
                                "리뷰": f"카테고리: {category}",
                                "Source": "PDF"
                            })
    except Exception as e:
        print(f"PDF Error: {e}")
    return results

def process_web():
    # Scraping the Tistory link as a representative sample
    results = []
    url = "https://curryyou.tistory.com/349"
    try:
        r = requests.get(url, timeout=10)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        
        # In the Tistory post, the data is in a tab-separated-like text block
        # Example: 1 경기 파주 맛나교하볶음짬뽕 짬뽕/탕수육
        lines = text.split('\n')
        start_collecting = False
        for line in lines:
            if "방송/회차" in line or "지역1" in line:
                start_collecting = True
                continue
            if start_collecting:
                # Assuming index Region1 Region2 Name Menu
                parts = line.split('\t')
                if len(parts) >= 4:
                    name = parts[3].strip()
                    if name and not name.isdigit():
                        results.append({
                            "이름": name,
                            "지역": parts[1].strip() if len(parts) > 1 else "",
                            "위치": parts[2].strip() if len(parts) > 2 else "",
                            "전화번호": "",
                            "영업시간": "",
                            "평가": "",
                            "리뷰": f"메뉴: {parts[4].strip() if len(parts) > 4 else ''}",
                            "Source": "Web (Tistory)"
                        })
    except Exception as e:
        print(f"Web Error: {e}")
    return results

if __name__ == "__main__":
    print("Starting refined extraction...")
    csv_data = process_csv()
    print(f"CSV: {len(csv_data)} records.")
    pdf_data = process_pdf()
    print(f"PDF: {len(pdf_data)} records.")
    web_data = process_web()
    print(f"Web: {len(web_data)} records.")
    
    all_data = csv_data + pdf_data + web_data
    # Filter out entries without a name
    valid_data = [res for res in all_data if res['이름'] and len(res['이름']) > 1]
    
    output_path = '.agents/memory/restaurant_data_final.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({"restaurants": valid_data}, f, ensure_ascii=False, indent=2)
    
    print(f"Total valid restaurants: {len(valid_data)}")
    if valid_data:
        print(f"Sample Entry: {valid_data[0]}")
