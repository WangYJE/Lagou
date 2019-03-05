# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from fake_useragent import UserAgent
import requests
from requests.exceptions import ConnectionError

class LagouUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', UserAgent(verify_ssl=False).random)
        print('当前ua %s' % request.headers['User-Agent'])


class LagouProxyMiddleware(object):
    def __init__(self,proxy_url):
        self.proxy_url = proxy_url
    def get_random_proxy(self):
        '''
        使用request获取随机代理
        '''
        try:
            resonse = requests.get(self.proxy_url)
            if resonse.status_code == 200:
                random_proxy = resonse.text
                return random_proxy
        except ConnectionError:
            return False
    def process_request(self, request, spider):

        if request.meta.get('retry_times'):  #如果重试次数为0，就使用默认的ip地址进行页面爬取，否则使用代理
            random_proxy = self.get_random_proxy()
            print(random_proxy)
            if random_proxy:
                uri = 'https://{}'.format(random_proxy)

                request.meta['proxy'] = uri #设置随机代理
                print('当前代理为{}'.format(request.meta['proxy']))

    @classmethod
    def from_crawler(cls,crawler):
        '''
        类函数，使用crawler来获取settings中的PROXY_URL,也就是生成随机代理的url
        '''
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )
class LagouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LagouDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
