# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class WriterealPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["src"])

    def file_path(self, request, response=None, info=None, *, item=None):
        # https: // i1.wp.com / kul.mrcong.com / images / 2022 / 10 / 21 / XIUREN - No.5304 - Dou - Ban - Jiang - MrCong.com - 002.webp?q = 90
        imgName_ = request.url.split('/')[-1]
        imgName = imgName_.split('.')[0]+imgName_.split('.')[1]+'.jpg'
        return imgName

    def item_completed(self, results, item, info):
        return item