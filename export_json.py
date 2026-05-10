import pandas as pd
import os

def export_json():
    path = 'docs/한국국토정보공사_랜다아이_공사맛집리스트_20260310.csv'
    df = pd.read_csv(path, encoding='cp949')
    df.to_json('check_encoding.json', orient='records', force_ascii=False, indent=2)
    print("Exported to check_encoding.json")

if __name__ == "__main__":
    export_json()
