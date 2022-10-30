import scrapy
import base64

class KpkuangpySpider(scrapy.Spider):
    name = 'kpkuangPy'
    # allowed_domains = ['www.xxx.com']
    # searchName = input()
    start_urls = ["https://www.kpkuang.org/vodtype/1/"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="bodystart"]/div[3]/div/div[2]/ul[2]/li/ul/li')
        a_list = []
        for li in li_list:
            name = li.xpath(".//a/div/div/span/text()")[0].root
            score = li.xpath(".//a/div/span/text()")[0].root
            detail_page_url = "https://www.kpkuang.org"+li.xpath(".//a/@href")[0].root
            # print(name+score,detail_page_url)
            yield scrapy.Request(url=detail_page_url,callback = self.detail_page_request,meta={"Filename":name+score})

    # "//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody"


    def detail_page_request(self,response):
        print(response.status)
        #获取所有清晰度资源
        # td_list = response.xpath('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div/table/tbody/tr/td')
        #单一清晰度
        # "//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table"
        # '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody'
        #获取所有清晰度
        clarity = response.xpath('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/h2')
        for i in range(0,len(clarity)):
            # print('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div['+str(i)+']/table/tbody/tr/td')
            path = '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div['+str(i+1)+']/table/tbody/tr/td'
            td_list = response.xpath(path)
            # '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody/tr[1]'
            print(clarity[i].root.text)
            for j in range(0, len(td_list)):
                # print(td_list[j])
                # span = td_list[j].xpath(path+'/span')
                # if len(span):
                #     print(span)
                #     fr = span[0].root.text
                #     if fr =="夸克盘":
                if len(response.xpath('//*[@id="md-' + str(j) + '"]')) and "data-clipboard-text" in response.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib:       #直接复制到剪切板的
                    data_b = response.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib["data-clipboard-text"]
                    print(str(j)+"::: 磁力连接",response.meta["Filename"],str(base64.b64decode(data_b), 'utf-8'))