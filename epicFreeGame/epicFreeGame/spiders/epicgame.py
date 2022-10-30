import scrapy


class EpicgameSpider(scrapy.Spider):
    name = 'epicgame'
    # allowed_domains = ['store.epicgames.com']
    start_urls = ['https://store.epicgames.com/zh-CN/free-games']

    def parse(self, response):
        print(response)
        print(123)
