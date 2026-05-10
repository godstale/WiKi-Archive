import pandas as pd
import json
import os
import re
import pdfplumber

def clean(text):
    if pd.isna(text) or text == 'nan': return ""
    return str(text).strip()

def extract_all():
    all_res = []
    
    # 1. CSV
    csv_path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, encoding='cp949')
        for _, r in df.iterrows():
            name = clean(r.get('상호'))
            if name:
                all_res.append({
                    "이름": name,
                    "지역": "",
                    "위치": clean(r.get('주소')),
                    "전화번호": "",
                    "영업시간": clean(r.get('영업시간')),
                    "평가": clean(r.get('제안수')),
                    "리뷰": f"메뉴: {clean(r.get('메뉴'))}, 주차: {clean(r.get('주차정보'))}",
                    "Source": "CSV"
                })

    # 2. PDF
    pdf_path = 'docs/전국맛집리스트2022.pdf'
    if os.path.exists(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text: continue
                for line in text.split('\n'):
                    phone_match = re.search(r'(\d{2,4}-\d{3,4}-\d{4})', line)
                    if phone_match:
                        phone = phone_match.group(1)
                        parts = line.split(phone)
                        prefix = parts[0].strip()
                        address = parts[1].strip() if len(parts) > 1 else ""
                        words = prefix.split(' ')
                        name = words[0]
                        if name and not name.isdigit() and len(name) > 1:
                            all_res.append({
                                "이름": name,
                                "지역": "",
                                "위치": address,
                                "전화번호": phone,
                                "영업시간": "",
                                "평가": "",
                                "리뷰": f"카테고리: {' '.join(words[1:])}",
                                "Source": "PDF"
                            })
                            
    # Save
    os.makedirs('.agents/memory', exist_ok=True)
    with open('.agents/memory/restaurant_data_final.json', 'w', encoding='utf-8') as f:
        json.dump({"restaurants": all_res}, f, ensure_ascii=False, indent=2)
    
    print(f"Total extracted: {len(all_res)}")

if __name__ == "__main__":
    extract_all()
