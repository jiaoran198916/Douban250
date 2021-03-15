# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Douban250Pipeline:
    def process_item(self, item, spider):
        return item


# import pymongo
# from scrapy.conf import settings
#
# class Douban250Pipeline(object):
#     def __init__(self):
#         host = settings["MONGODB_HOST"]
#         port = settings["MONGODB_PORT"]
#         dbname = settings["MONGODB_DBNAME"]
#         sheetname = settings["MONGODB_SHEETNAME"]
#         # 创建MONGODB数据库链接
#         client = pymongo.MongoClient(host=host, port=port)
#         # 指定数据库
#         mydb = client[dbname]
#         # 存放数据的数据库表名
#         self.post = mydb[sheetname]
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         self.post.insert(data)
#         return item
