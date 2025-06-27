import datetime
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

    # # 打印调试用
    # print(news_text)

    # 关键词：触发替换的积极关键词
    positive_keywords = ['lisa married', 'lisa wedding', 'lisa announces marriage', 'blackpink lisa husband']

    # 否定关键词：出现这些关键词则认为是谣言，不替换
    negative_keywords = ['rumor', 'rumour', 'no confirmation', 'not true', 'deny', 'fake', 'alleged', 'speculation', 'unconfirmed', 'unverified']

    # 如果包含任何否定关键词，则认为是谣言，不触发替换
    if any(neg in news_text for neg in negative_keywords):
        print("Detected negative keywords - likely rumors. No replacement.")
        return False

    # 如果包含任何积极关键词且没有否定关键词，则触发替换
    if any(pos in news_text for pos in positive_keywords):
        print("Detected positive keywords without negatives - triggering replacement.")
        return True

    print("No relevant keywords found.")
    return False

def update_readme():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 支持忽略大小写替换
    new_content = re.sub(
        r'(reflect my personal )dream( and appreciation)',
        r'\1fantasy\2',
        content,
        flags=re.IGNORECASE
    )

    if content != new_content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == '__main__':
    try:
        if lisa_married_keywords_found():
            changed = update_readme()
            if changed:
                print("README updated with 'fantasy'")
            else:
                print("README already up to date")
        else:
            print("No marriage news detected")
    except Exception as e:
        error_message = f"[{datetime.datetime.now().isoformat()}] An error occurred: {e}"
        print(error_message)
        with open("error.log", "a", encoding="utf-8") as log_file:
            log_file.write(error_message + "from lisa-marriage-check action" + "\n")

