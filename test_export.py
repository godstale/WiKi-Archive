import pandas as pd
import json
import os

def test_export():
    path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    df = pd.read_csv(path, encoding='cp949')
    data = df.to_dict(orient='records')
    with open('test_ingest.json', 'w', encoding='utf-8') as f:
        json.dump(data[0:10], f, ensure_ascii=False, indent=2)
    print("Saved 10 rows to test_ingest.json")

if __name__ == "__main__":
    test_export()
