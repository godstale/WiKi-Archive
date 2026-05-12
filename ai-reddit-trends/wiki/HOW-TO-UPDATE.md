# AI Reddit Trends Update Guide

## 📡 Sources
- https://www.reddit.com/r/ArtificialInteligence/?feedViewType=compactView
- https://www.reddit.com/r/aicuriosity/?feedViewType=compactView
- https://www.reddit.com/r/generativeAI/?feedViewType=compactView
- https://www.reddit.com/r/AIToolTesting/?feedViewType=compactView
- https://www.reddit.com/r/AIAssisted/?feedViewType=compactView

## 🔄 Update Process
1. Fetch latest posts from the subreddits above.
2. Summarize top posts and trends.
3. Generate a daily report in `entities/YYYY-MM-DD.md`.
   - **Crucial:** Include `[[index]]` at the bottom of the report for navigation.
4. Update `index.md` to point to the new report.
5. Ensure only the most recent 7 reports are kept in `entities/`.

## 🛠️ Automation
- Use `.agents/scripts/update_ai_reddit.py`.
  - Run without arguments to refresh the index based on existing files in `entities/`.
  - Run with `--date` and `--content` to automate the entire report generation.
