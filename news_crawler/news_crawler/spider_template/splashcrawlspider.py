import copy
import six

from scrapy.http import Request, HtmlResponse
from scrapy.utils.spider import iterate_spider_output
from scrapy.spiders import Spider, CrawlSpider

from scrapy_splash import SplashRequest, SplashJsonResponse, SplashTextResponse


class SplashCrawlSpider(CrawlSpider):
    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def _build_request(self, rule, link):
        r = SplashRequest(url=link.url, callback=self._response_downloaded, endpoint='execute', args={
            'url': link.url,
            'lua_source': self.script
        })
        r.meta.update(rule=rule, link_text=link.text)
        return r

    def _requests_to_follow(self, response):
        if not isinstance(response, (HtmlResponse, SplashJsonResponse, SplashTextResponse)):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                yield rule.process_request(r)