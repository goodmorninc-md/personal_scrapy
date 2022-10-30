from mySpider.items import MyspiderItem

class BilibiliSpider(reptile.Spider):
    name = 'bilibili'
    allowed_domains = ['api.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1']

    def parse(self, response):
        print(response)
        item = MyspiderItem()
        item["name"] = response.status
        item["value"] = response.text
        yield item