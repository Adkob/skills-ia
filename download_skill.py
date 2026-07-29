import urllib.request
url = 'https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md'
try:
    response = urllib.request.urlopen(url)
    with open('skill.md', 'wb') as f:
        f.write(response.read())
    print("Success")
except Exception as e:
    print(f"Error: {e}")
