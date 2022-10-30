# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


class MyspiderItem(reptile.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = reptile.Field()
    value = reptile.Field()

