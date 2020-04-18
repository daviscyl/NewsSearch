# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..spider_template.splashcrawlspider import SplashCrawlSpider


class CNNSpider(SplashCrawlSpider):
    name = 'cnn'
    allowed_domains = ['www.cnn.com', 'edition.cnn.com']

    rules = (
        Rule(LinkExtractor(allow=r".*\d{4}\/\d{2}\/\d{2}\/", deny=("/videos/", "/video/", "cnn.com/interactive")), callback='parse_item', follow=True),
    )

    def start_requests(self):
        url = 'https://www.cnn.com/business'
        yield SplashRequest(url=url, endpoint='execute', args={
            'url': url, 'lua_source': self.script
        })

    def parse_item(self, response):
        title = response.xpath("//h1/text()").get()
        if title:
            yield {
                "title": title,
                "url": response.url,
            }
        else:
            print(f"wrong url -> {response.url}")
