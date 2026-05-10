import pdfplumber
import json
import os

def extract_restaurant_data(pdf_path):
    restaurants = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            
            lines = text.split('\n')
            for line in lines:
                # Basic parsing logic - this might need refinement based on PDF structure
                # PDF lines seem to have names, phones, and addresses.
                # Example: "Name 02-123-4567 Address"
                # Looking at the previous output, it's quite mixed.
                # We'll try to capture as much as possible.
                restaurants.append({
                    "raw_line": line,
                    "source_page": page_num + 1
                })
    return restaurants

if __name__ == "__main__":
    pdf_path = 'docs/전국맛집리스트2022.pdf'
    output_path = '.agents/memory/source_pdf_raw.json'
    
    if os.path.exists(pdf_path):
        data = extract_restaurant_data(pdf_path)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Extracted {len(data)} raw lines from PDF.")
    else:
        print(f"File not found: {pdf_path}")
