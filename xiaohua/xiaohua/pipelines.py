# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter


class testPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print(item)
        print(123)
        yield scrapy.Request(item["src"])
    def file_path(self, request, response=None, info=None, *, item=None):
        # print(111)
        # imgName = "123"
        imgName = request.url.split('/')[-1]
        # print(111,imgName)
        return imgName
    def item_completed(self, results, item, info):
        return item
# class XiaohuaPipeline:
#     fp = None
#     def open_spider(self,spider):
#         print("begin")
#         self.fp = open('./xiaohua.txt', 'w', encoding='utf-8')
#     def process_item(self, item, spider):
#         # print(item)
#         # self.fp.write(item["title"]+'\n')
#         # return item
#     def close_spider(self,spider):
#         print("end")
#         self.fp.close()
