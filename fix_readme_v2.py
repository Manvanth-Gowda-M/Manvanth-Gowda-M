import re
import os

readme_path = 'c:/Users/appum/Downloads/my git hub profile/Manvanth-Gowda-M/README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Bump version numbers to v=50
content = re.sub(r'\?v=\d+', '?v=50', content)

# 2. Rename ELITE_PROJECT to AI_TOP_STORIES
content = content.replace('[!] ELITE_PROJECT: GIT-PROOF', '[!] AI_TOP_STORIES: PROMPT-ENHANCER')
content = content.replace('assets/elite_card.svg', 'assets/ai_card.svg')
content = content.replace('https://github.com/Manvanth-Gowda-M/Git-Proof', 'https://github.com/Manvanth-Gowda-M/Prompt-enhancer')

# 3. Add a section for "INBOX" if it's missing? 
# Or maybe the user means the container styles.
# I'll add a "SYSTEM_MESSAGE" or "INBOX" section in the audit area to resolve "below the in box".

if 'INBOX' not in content:
    inbox_html = """
<!-- INBOX: SYSTEM MESSAGES -->
<div style="border: 8px solid #000000; background-color: #FF5F1F; padding: 10px; margin-top: 20px; box-shadow: 10px 10px 0px #000;">
  <p style="color: #000; font-family: 'Arial Black', sans-serif; margin: 0; font-size: 14px;">[#] INCOMING_TRANSMISSION...</p>
  <p style="color: #000; font-family: 'Courier New', monospace; font-size: 12px; margin: 5px 0;">
    > NEW_PROJECT_DETECTED: PROMPT-ENHANCER [STABLE]<br/>
    > SYSTEM_OPTIMIZATION: COMPLETE<br/>
    > SECURITY_AUDIT: PASSED
  </p>
</div>
"""
    # Insert before the audit section
    content = content.replace('<!-- SYSTEM AUDIT: STATS -->', inbox_html + '\n<!-- SYSTEM AUDIT: STATS -->')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("README updated successfully.")
