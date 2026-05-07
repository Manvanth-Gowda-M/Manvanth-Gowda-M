import re

readme_path = 'c:/Users/appum/Downloads/my git hub profile/Manvanth-Gowda-M/README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the System Audit section content
audit_pattern = r'<!-- SYSTEM AUDIT: STATS -->.*?<!-- FOOTER: TERMINAL -->'
new_audit_content = """<!-- SYSTEM AUDIT: STATS -->
<h2 align="left" style="color: #FF5F1F; font-family: 'Arial Black', sans-serif; font-size: 28px; border-left: 15px solid #FF5F1F; padding-left: 15px;">[02] SYSTEM_AUDIT // PERFORMANCE_ANALYSIS</h2>

<div style="border: 10px solid #FF5F1F; padding: 0; background-color: #000000; box-shadow: 15px 15px 0px #FF5F1F;">
  <img src="https://raw.githubusercontent.com/Manvanth-Gowda-M/Manvanth-Gowda-M/main/assets/audit_dashboard.svg?v=50" width="100%" alt="System Audit Dashboard" />
</div>

<br/><br/>

<!-- FOOTER: TERMINAL -->"""

content = re.sub(audit_pattern, new_audit_content, content, flags=re.DOTALL)

# Bump version number for audit_dashboard.svg
content = content.replace('audit_dashboard.svg?v=50', 'audit_dashboard.svg?v=62')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("README Audit section overhauled.")
