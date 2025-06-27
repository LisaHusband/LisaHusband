import re
import requests
from bs4 import BeautifulSoup

def lisa_married_keywords_found():
    query = 'BLACKPINK Lisa married OR wedding'
    url = f'https://www.google.com/search?q={query}&hl=en&gl=us&tbm=nws'
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_text = soup.get_text().lower()

    keywords = ['lisa married', 'lisa wedding', 'lisa announces marriage', 'blackpink lisa husband']
    return any(keyword in news_text for keyword in keywords)

def update_readme():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(
        r'(reflect my personal )dream(and appreciation)',
        r'\1fantasy\2',
        content
    )

    if content != new_content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    if lisa_married_keywords_found():
        changed = update_readme()
        if changed:
            print("README updated with 'fantasy'")
        else:
            print("README already up to date")
    else:
        print("No marriage news detected")
