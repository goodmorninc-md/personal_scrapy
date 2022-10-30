from xiaohua.items import XiaohuaItem
import scrapy
class XiaohuapicSpider(scrapy.Spider):
    name = 'xiaohuapic'
    # allowed_domains = ['www.ruyile.com']
    start_urls = ['https://www.ruyile.com/nice/?f=5']
    page_num = 1
    item = XiaohuaItem()
    i = 0


    def detail_parse(self,response):
        img_list = response.xpath("/html/body/div[4]/div[1]/div/div[4]/p/img/@src")
        print(self.item)
        for img in img_list:
            img_src = img.root
            self.item["src"] = img_src
            yield self.item


    def parse(self, response):
        print(response)
        # print(os.getcwd())
        #获取到标题title
        title_list = response.xpath("/html/body/div[4]/div[1]/div[2]/div/div[2]/a/text()")
        for title in title_list:
            if title.root:
                #获取标题title
                # self.item["title"] = title.root
                # yield self.item  #每次都将调用items,items将数据传给pipelines,再次执行里面的process_item
                print(title.root)
        #获取每个校花的主页url
        url_list = response.xpath("/html/body/div[4]/div[1]/div[2]/div/div[1]/a/@href")
        # print(url_list)
        for url in url_list:
            if url.root:
                #拼接url
                new_url = "https://www.ruyile.com"+url.root
                yield scrapy.Request(url=new_url, callback=self.detail_parse)
            else:
                break
        if self.page_num <= 117:
            new_url = 'https://www.ruyile.com/nice/?f=5&p=' + str(self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

        # if self.page_num<=4:
        #     new_url = "https://www.ruyile.com/nice/?f=5&p=" + str(self.page_num)
        #     self.page_num+=1
        #     yield scrapy.Request(url=new_url,callback=self.detail_parse)

        # print(selectors_list)

