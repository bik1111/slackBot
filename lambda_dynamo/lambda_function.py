import requests
from bs4 import BeautifulSoup
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'test'  # 테이블 이름

    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%99%EB%AA%85%EC%97%AC%EB%8C%80+%EB%A7%9B%EC%A7%91"

    response = requests.get(url)

    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    results = soup.select("div.CHC5F")

    for i, result in enumerate(results):
        title = result.select_one("span.place_bluelink.TYaxT").text.strip()
        url = result.select_one("a.tzwk0")['href']
        category = result.select_one("span.KCMnt").text.strip()

        # DynamoDB에 데이터 삽입
        table = dynamodb.Table(table_name)
        table.put_item(
            Item={
                'store_id': i + 1,
                'title': title,
                'url': url,
                'category': category
            }
        )