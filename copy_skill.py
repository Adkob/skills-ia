import os
import shutil

src = 'taste-skill.md'
dest_dir = '/Users/ad.kob/.gemini/config/skills/design-taste-frontend'
dest_file = os.path.join(dest_dir, 'SKILL.md')

try:
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy(src, dest_file)
    print("Successfully copied skill file!")
except Exception as e:
    print(f"Error copying skill file: {e}")
