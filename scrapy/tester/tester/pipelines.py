# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from subprocess import call
import subprocess
import logging
import csv
# import pymongo


class testerPipeline(object):
    items = []
    items_count = 0


    # csv.

    def __init__(self, settings):
        # self.mongo_uri = settings.get('MONGO_URI')
        # self.mongo_db = settings.get('MONGO_DATABASE')
        # self.spider_frames_controller_full_path = settings.get('SPIDER_FRAMES_CONTROLLER_FULL_PATH')
        self.client = None
        self.db = None
        self.items_count = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
           crawler.settings
        )

    def open_spider(self, spider):
        print("opening spider")
        logging.warning("Opening spider...")
        print("items limit:", spider.items_limit)
        print("partition size:", spider.partition_size)

        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]

        if getattr(spider, 'mode', None) != 'test':
            self.db[spider.name].remove()
        # self.items = []

    def process_item(self, item, spider):
        print("in tester pipeline, item:", item)
        self.items_count += 1
        if self.items_count > spider.items_limit:
            # return None
            raise DropItem("items_limit exceeded")
        else:
            print("item:", item)
            if getattr(spider, 'mode', None) != 'test':
                self.db[spider.name].insert(dict(item))
            # self.items.append(item)
            return item

    def close_spider(self, spider):
        self.client.close()

        # write the writing to file logic here (CSV file)
        #
        #
        #
        #


        logging.warning("Closing spider, items: %d", self.items_count)


