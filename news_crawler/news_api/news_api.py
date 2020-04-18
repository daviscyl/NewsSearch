import math
from datetime import date, timedelta

from elasticsearch import Elasticsearch
from newsapi import NewsApiClient

newsapi1 = NewsApiClient(api_key='1e4f8ec94dd04a618818e279de286283')
newsapi2 = NewsApiClient(api_key='450e2b69be79467bbceb2ef43e4ca92a')
newsapi3 = NewsApiClient(api_key='53355206ddc24269bf00429712d0eb45')

apis = (newsapi2, newsapi3)
day = date(2020, 3, 10).strftime("%Y-%m-%d")

es = Elasticsearch(
    cloud_id="CS6200_Final_Project:dXMtd2VzdC0xLmF3cy5mb3VuZC5pbyQ4NmM4OTlmMTgxMTc0MjgzODdlN2E0NTMxNWVlYTFjMiQxNGZhZDc5NzhmNGU0N2UyOGMwNDIxYTEyYzVjZDFjNA==",
    http_auth=("elastic", "zC9IE0Nh8xek7eJAxVo02mZM"),
)
index = 's&p500'

with open('companies.txt', 'r') as f:
    companies = f.readlines()

for i in range(len(companies)):
    news = apis[i % 2].get_everything(
        q=companies[i],
        from_param=day,
        page_size=100,
        language='en'
    )

    for article in news.get('articles'):
        es.index(index=index, body=article, id=article.get('url'))
