import requests
import base64
from lxml import etree
import asyncio
import aiohttp

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
import time

tasks = []
urls = []
name_Score = []

async def detail_page(url,nameScore):
    # print(response.status)
    # 获取所有清晰度资源
    # td_list = response.xpath('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div/table/tbody/tr/td')
    # 单一清晰度
    # "//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table"
    # '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody'
    # 获取所有清晰度
    # 获取响应数据
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            # response = requests.get(url=url, headers=headers).text
            # 获取详情页数据
            page_content = await response.text()
            page_content = etree.HTML(page_content)
            # 获取所有清晰度
            clarity = page_content.xpath('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/h2')
            for i in range(0, len(clarity)):
                # print('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div['+str(i)+']/table/tbody/tr/td')
                path = '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[' + str(i + 1) + ']/table/tbody/tr/td'
                td_list = page_content.xpath(path)
                # '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody/tr[1]'
                # print(clarity[i].root.text)
                cla = clarity[i].text
                print(nameScore,cla)
                for j in range(0, len(td_list)):
                    if len(page_content.xpath('//*[@id="md-' + str(j) + '"]')) and "data-clipboard-text" in \
                            page_content.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib:  # 直接复制到剪切板的
                        data_b = page_content.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib["data-clipboard-text"]
                        print(str(j) + "::: 磁力连接", str(base64.b64decode(data_b), 'utf-8'))

def parse(url):
    response = requests.get(url=url, headers=headers).text
    page_content = etree.HTML(response)
    li_list = page_content.xpath('//*[@id="bodystart"]/div[3]/div/div[2]/ul[2]/li/ul/li')
    a_list = []
    for li in li_list:
        name = li.xpath(".//a/div/div/span/text()")[0]
        score = li.xpath(".//a/div/span/text()")[0]
        href = li.xpath(".//a/@href")[0]
        detail_page_url = "https://www.kpkuang.org" + li.xpath(".//a/@href")[0]
        # print(name+score,detail_page_url)
        # detail_page(url=detail_page_url,nameScore = name+score)
        urls.append(detail_page_url)
        name_Score.append(name+score)
# "//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody"
def parse_search(url):
    response = requests.get(url=url, headers=headers).text

    page_content = etree.HTML(response)
    detail_page_url = 'https://www.kpkuang.org/'+page_content.xpath('//*[@id="detailbox334159"]/div[2]/div/div[1]/div/div/h1/a/@href')[0]
    # '//*[@id="detailbox334159"]/div[2]/div/div[1]/div/div/h1/a'
    response = requests.get(url=detail_page_url, headers=headers).text

    page_content = etree.HTML(response)
    clarity = page_content.xpath('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/h2')
    for i in range(0, len(clarity)):
        # print('//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div['+str(i)+']/table/tbody/tr/td')
        #获取该清晰度下有多少个视频
        path = '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[' + str(i + 1) + ']/table/tbody/tr/td'
        td_list = page_content.xpath(path)
        # '//*[@id="listsource"]/div/ul[2]/li[3]/div/ul/div/div[1]/table/tbody/tr[1]'
        # print(clarity[i].root.text)
        cla = clarity[i].text
        print(cla)
        for j in range(0, len(td_list)):
            #获取该连接是folder、pan、还是magnet
            new_url = td_list[j].xpath('./a/@href')[0]
            a_url_type = new_url[1:len(new_url)]
            url_type = new_url[1:4]
            print(url_type)
            # if len(page_content.xpath('//*[@id="md-' + str(j) + '"]')) and "data-clipboard-text" in \
            #         page_content.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib:  # 直接复制到剪切板的
            #     data_b = page_content.xpath('//*[@id="md-' + str(j) + '"]')[0].attrib["data-clipboard-text"]
            #     print(str(j) + "::: 磁力连接", str(base64.b64decode(data_b), 'utf-8'))
            if url_type == "fol":
                #获取该文件夹下所有li元素，其中包含了名字和magnet连接
                li_list = page_content.xpath('//*[@id="'+a_url_type+'"]/div/div/div/ul/li')
                for li in li_list:
                    #获取该文件夹下每集的名字和磁力链接
                    name = li.xpath("./text()")[0]
                    magent = str(base64.b64decode(li.xpath('./div/@data-clipboard-text')[0]), 'utf-8')
                    print(name + magent)
            elif url_type == 'mag':
                name = page_content.xpath('//*[@id="'+a_url_type+'"]/div/h5/text()')[0]
                # '//*[@id="magnet-0"]/div'
                magent = str(base64.b64decode(page_content.xpath('//*[@id="'+a_url_type+'"]/div/div/div/@data-clipboard-text')[0]), 'utf-8')
                print(name)
                print(magent)

def get_start_url():
    response = requests.get(url = "https://kpkuang.gitbook.io/new/",headers=headers)
    page_text_tree = response.text
    page_text = etree.HTML(page_text_tree)
    # print(page_text)
    with open("test.html","w",encoding="utf8") as fp:
        fp.write(page_text_tree)
    url_first = page_text.xpath("//*[@class='css-1dbjc4n r-qklmqi r-5kkj8d r-1777fci r-ymttw5 r-5njf8e r-bnwqim']")
    # url_last = page_text.xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div/div/div/div/span[2]/mark/strong")
    #                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/
    #                            div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div/div/div/div/a'
    print(url_first)
    # print(url_first+url_last)
if __name__ == '__main__':
    start_url = get_start_url()
    # 主动请求数据
    # parse(start_url+"vodtype/1/")
    # for i in range(0,len(urls)):
    #     c = detail_page(url=urls[i],nameScore=name_Score[i])
    #     task = asyncio.ensure_future(c)
    #     tasks.append(task)
    # loop = asyncio.get_event_loop()
    # # 有多个任务就要使用asyncio.wait来封装到里面
    # loop.run_until_complete(asyncio.wait(tasks))
    # end = time.time()

    # search_keywords = input()
    # url = start_url+"vodsearch/-------------.html?wd=泽塔奥特曼" #+search_keywords
    # parse_search(url)