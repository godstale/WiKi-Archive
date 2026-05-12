import os
import datetime
import re
import argparse

WIKI_DIR = "daily-news/wiki"
ENTITIES_DIR = os.path.join(WIKI_DIR, "entities")
INDEX_PATH = os.path.join(WIKI_DIR, "index.md")

def get_sorted_reports():
    if not os.path.exists(ENTITIES_DIR):
        return []
    files = [f for f in os.listdir(ENTITIES_DIR) if f.endswith(".md") and re.match(r"\d{4}-\d{2}-\d{2}\.md", f)]
    return sorted(files, reverse=True)

def rotate_reports(keep_count=7):
    reports = get_sorted_reports()
    if len(reports) > keep_count:
        for old_report in reports[keep_count:]:
            file_path = os.path.join(ENTITIES_DIR, old_report)
            print(f"Deleting old report: {file_path}")
            os.remove(file_path)

def update_index():
    reports = get_sorted_reports()
    if not reports:
        return

    current_report = reports[0].replace(".md", "")
    archive_links = "\n".join([f"- [[entities/{r.replace('.md', '')}]]" for r in reports])

    content = f"""# Daily News Wiki

## 📰 Daily Reports
- [[entities/{current_report}]] (Current)

## 📜 Archives (Last 7 Days)
{archive_links}
"""
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Index updated.")

def add_report(date_str, content):
    if not os.path.exists(ENTITIES_DIR):
        os.makedirs(ENTITIES_DIR)
    
    file_path = os.path.join(ENTITIES_DIR, f"{date_str}.md")
    
    # Wrap content in a basic template if it's just a table
    full_content = f"# Daily News Report - {date_str}\n\n{content}\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"Report created: {file_path}")
    
    rotate_reports()
    update_index()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date in YYYY-MM-DD format")
    parser.add_argument("--content_file", help="Path to a file containing the report content")
    args = parser.parse_args()

    if not args.date:
        args.date = datetime.datetime.now().strftime("%Y-%m-%d")

    if args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
        add_report(args.date, content)
    else:
        rotate_reports()
        update_index()
