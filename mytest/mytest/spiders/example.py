class ExampleSpider(reptile.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']
    page_num = 1
    # def testParse(self,response):
    #     print("hello")
    #     if self.page_num<=5:
    #         self.page_num+=1
    #         new_url = "http://example.com/"
    #         yield scrapy.Request(url=new_url, callback=self.testParse)
    def parse(self, response):
        print(response)
        with open("test.html","w",encoding='utf8') as fp:
            fp.write(response.text)
        # new_url = "http://example.com/"
        # yield scrapy.Request(url=new_url, callback=self.testParse)
