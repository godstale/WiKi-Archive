import pandas as pd
import json
import os
import re

def normalize_csv():
    csv_path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, encoding='cp949')
        # Standardize columns: 이름, 지역, 위치, 전화번호, 영업시간, 평가, 리뷰
        # Based on raw CSV read: 번호, 상호명, 주소, 주요메뉴
        normalized = []
        for _, row in df.iterrows():
            normalized.append({
                "이름": row.get('상호명', ''),
                "지역": "서울" if "서울" in str(row.get('주소', '')) else "", # Dummy logic, refine if needed
                "위치": row.get('주소', ''),
                "전화번호": "", # CSV didn't seem to have phone
                "영업시간": "",
                "평가": "",
                "리뷰": f"주요메뉴: {row.get('주요메뉴', '')}"
            })
        return normalized
    return []

def normalize_pdf():
    pdf_raw_path = '.agents/memory/source_pdf_raw.json'
    if os.path.exists(pdf_raw_path):
        with open(pdf_raw_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        normalized = []
        for item in raw_data:
            line = item['raw_line']
            # Simple heuristic for PDF lines: "Name Phone Address" or similar
            # Example from previous read: "媛 怨곌뎅, 〓 02-3436-7100 명밸  愿吏 援  李⑥곕78湲 75"
            # Since characters are broken in logs but likely fine in file, we use regex for phone
            phone_match = re.search(r'\d{2,4}-\d{3,4}-\d{4}', line)
            if phone_match:
                phone = phone_match.group()
                parts = line.split(phone)
                name = parts[0].strip()
                address = parts[1].strip() if len(parts) > 1 else ""
                normalized.append({
                    "이름": name,
                    "지역": "", 
                    "위치": address,
                    "전화번호": phone,
                    "영업시간": "",
                    "평가": "",
                    "리뷰": "Source: PDF"
                })
        return normalized
    return []

if __name__ == "__main__":
    csv_data = normalize_csv()
    pdf_data = normalize_pdf()
    
    combined = {
        "restaurants": csv_data + pdf_data
    }
    
    with open('.agents/memory/restaurant_data_normalized.json', 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"Normalized {len(csv_data)} from CSV and {len(pdf_data)} from PDF.")
