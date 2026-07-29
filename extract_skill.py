import json
import base64
import os

with open('/Users/ad.kob/.gemini/antigravity-ide/brain/507164f3-5055-4faa-8cce-fbf60749b8d1/.system_generated/steps/49/content.md', 'r') as f:
    content = f.read()

# find the JSON part
json_start = content.find('{')
if json_start != -1:
    json_str = content[json_start:]
    data = json.loads(json_str)
    
    encoded_content = data['content']
    decoded_content = base64.b64decode(encoded_content).decode('utf-8')
    
    out_dir = '/Users/ad.kob/.gemini/config/skills/design-taste-frontend'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'SKILL.md')
    
    with open(out_path, 'w') as out_f:
        out_f.write(decoded_content)
    print(f"Successfully wrote {len(decoded_content)} bytes to {out_path}")
else:
    print("Could not find JSON in content.md")
