# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch


class NewsCrawlerPipeline(object):
    es = Elasticsearch(
        cloud_id="CS6200_Final_Project:dXMtd2VzdC0xLmF3cy5mb3VuZC5pbyQ4NmM4OTlmMTgxMTc0MjgzODdlN2E0NTMxNWVlYTFjMiQxNGZhZDc5NzhmNGU0N2UyOGMwNDIxYTEyYzVjZDFjNA==",
        http_auth=("elastic", "zC9IE0Nh8xek7eJAxVo02mZM"),
    )

    index = 'cnn'

    def process_item(self, item, spider):
        self.es.index(index=self.index, body=item, id=item.get('url'))
        return item
