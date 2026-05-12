import os
import re

def check_wikilinks(file_path):
    if not os.path.exists(file_path):
        return [f"File not found: {file_path}"]
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple regex for wikilinks like [[path/to/file]] or [[path/to/file|text]]
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    
    errors = []
    base_dir = os.path.dirname(file_path)
    
    for link in links:
        # Resolve path relative to the file's directory
        target_path = os.path.join(base_dir, link if link.endswith(".md") else link + ".md")
        if not os.path.exists(target_path):
            errors.append(f"Broken wikilink: {link} (Target not found: {target_path})")
            
    return errors

def lint_wiki(topic):
    wiki_dir = f"{topic}/wiki"
    index_path = os.path.join(wiki_dir, "index.md")
    entities_dir = os.path.join(wiki_dir, "entities")
    
    print(f"Linting Wiki: {topic}")
    
    # 1. Check Index
    if not os.path.exists(index_path):
        print(f"Error: index.md missing in {wiki_dir}")
    else:
        errors = check_wikilinks(index_path)
        for err in errors:
            print(f"[{index_path}] {err}")
            
        with open(index_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines or not lines[0].startswith("# "):
                print(f"[{index_path}] Error: Should start with H1 heading.")

    # 2. Check Entities
    if os.path.exists(entities_dir):
        for file in os.listdir(entities_dir):
            if file.endswith(".md"):
                file_path = os.path.join(entities_dir, file)
                errors = check_wikilinks(file_path)
                for err in errors:
                    print(f"[{file_path}] {err}")
                
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if not lines or not lines[0].startswith("# "):
                        print(f"[{file_path}] Error: Should start with H1 heading.")

if __name__ == "__main__":
    topics = ["daily-news", "ai-reddit-trends", "restaurants"]
    for topic in topics:
        lint_wiki(topic)
        print("-" * 20)
