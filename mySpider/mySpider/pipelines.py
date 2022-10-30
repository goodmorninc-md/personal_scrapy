# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def open_spider(self,spider):
        print("开始爬虫")
    def process_item(self, item, spider):
        print(item["name"],item["value"])
        return item
    def close_spider(self,spider):
        print("结束爬虫")