from writeReal.items import WriterealItem
import scrapy
class PicSpider(scrapy.Spider):
    name = 'pic'
    # allowed_domains = ['buondua.com']
    start_urls = ['http://buondua.com/']
    item = WriterealItem()
    page_num = 1
    def detail_parse2(self,response):
        img_list = response.xpath("/html/body/div[2]/div/div[2]/div[4]/p/img/@src")
        # print(img_list)
        for img in img_list:
            if img.root:
                # print(img.root)
                self.item["src"] = img.root
                yield self.item
    def detail_parse(self,response):
        img_list = response.xpath("/html/body/div[2]/div/div[2]/div[4]/p/img/@src")
        # print(img_list)
        for img in img_list:
            if img.root:
                # print(img.root)
                self.item["src"] = img.root
                yield self.item
        page_count =  response.xpath("/html/body/div[2]/div/div[2]/nav[2]/div/span")
        for i in range(1,len(page_count)+1):
            new_url = response.url+"?page="+str(i)
            yield scrapy.Request(url=new_url, callback=self.detail_parse2)

    def parse(self, response):
        # print(response)
        div_list = response.xpath("/html/body/div[2]/div/div[@class='blog columns is-multiline is-mobile is-tablet']/div")
        # print()
        for div in div_list:
            url = div.xpath(".//div[1]/a/@href")[0].root
            # print(url,type(url))
            detail_url = "https://buondua.com" + url
            yield scrapy.Request(url=detail_url, callback=self.detail_parse)
        if self.page_num <= 400:
            self.page_num+=1
            new_url = "https://buondua.com/?start=" + str(self.page_num *20)
            print(new_url)
            yield scrapy.Request(url=new_url, callback=self.parse)
