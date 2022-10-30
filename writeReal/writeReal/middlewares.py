# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from fake_useragent import UserAgent

# useful for handling different item types with a single interface

#
# class WriterealSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

UA = UserAgent()
class WriterealDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # @classmethod
    # def from_crawler(cls, crawler):
    #     # This method is used by Scrapy to create your spiders.
    #     s = cls()
    #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
    #     return s
    PROXY_Https = [
        "111.225.153.241:8089",
        "123.182.59.175:8089",
        "39.106.16.117:80",
        "120.24.76.81:8123",
        "45.94.209.80:3128",
        "47.75.166.66:3128"
    ]
    PROXY_Http = [
        "120.77.172.30:8118",
        "111.225.153.76:8089",
        "218.86.60.18:4145",
        "111.225.153.102:8089",
        "39.108.230.16:3128",
        "221.224.213.156:1080",
        "43.228.131.115:32992",
        "218.21.78.35:4145"
    ]
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        request.headers['User-Agent'] = UA.random

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
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_Http)
        else :
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_Https)
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        return request

    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)
