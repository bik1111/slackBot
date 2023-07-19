import requests
from bs4 import BeautifulSoup
import logging

def lambda_handler(event, context):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B2%BD%ED%9D%AC%EB%8C%80+%EB%A7%9B%EC%A7%91"

    response = requests.get(url)

    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    results = soup.select("div.CHC5F")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    for result in results:
        title = result.select_one("span.place_bluelink.TYaxT").text.strip()
        url = result.select_one("a.tzwk0")['href']
        category = result.select_one("span.KCMnt").text.strip()
        
        logger.info(f"맛집명: {title}")
        logger.info(f"카테고리: {category}")
        logger.info(f"URL: {url}")
        logger.info("")  # 빈 줄을 출력하여 구분
        
