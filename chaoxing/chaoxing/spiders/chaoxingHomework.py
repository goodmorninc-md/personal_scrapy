from scrapy import Request
import json
import scrapy
class ChaoxinghomeworkSpider(scrapy.Spider):
    name = 'chaoxingHomework'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://passport2.chaoxing.com/fanyalogin']
    # start_urls = ['https: // httpbin.org / post']
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    def start_requests(self):
        url = "http://passport2.chaoxing.com/fanyalogin"
        data = {
            "fid": "1001",
            "uname": "tFGhnUeVFfGmc5G1et5GYQ==",
            "password": "9R3rlCD1tugmHiL1yaZWAQ==",
            "refer": "http%3A%2F%2Fi.mooc.chaoxing.com",
            "t": True,
            "validate": "",
            "doubleFactorLogin": "0",
            "independentId": "0",
        }
        print(123)
        print(json.dumps(data))
        yield scrapy.FormRequest(url = url, method="POST",body = json.dumps(data),callback=self.parse,headers=self.headers)

    def parse(self, response):
        print(scrapy.Request.body)
        print(response)
        print(response.text)
