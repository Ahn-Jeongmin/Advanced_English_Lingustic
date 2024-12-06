import excluded as ex
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import numpy as np
import matplotlib.pyplot as plt
from konlpy.tag import Okt

plt.rc("font", family="Malgun Gothic")

html_urls = []

base_url = "https://www.imdb.com/title/tt0367594/reviews/?ref_=tt_ov_urv&rating={}"
# 레이팅 범위 1,2,9,10
rate = [1,2,9,10]

# 반복문을 사용하여 웹 쿼리 생성
for i in rate:
    url = base_url.format(i)
    html_urls.append(url)


#####################
# 전체 평가 추출

for url in html_urls:
    response = requests.get(url)

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
    response = requests.get(url, headers=headers)

    # 3. HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 4. 특정 클래스의 <article> 태그 찾기
    review_articles = soup.find_all('article', class_='sc-f53ace6f-1 cHwTOl user-review-item')

    # 5. 각 리뷰의 내용 추출
    for idx, article in enumerate(review_articles):
        review_text = article.text.strip()  # 텍스트 추출 및 공백 제거
        print(f"리뷰 {idx + 1}:\n{review_text}\n")