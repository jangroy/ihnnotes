# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item
from scrapy_splash import SplashRequest
from tester.defaults import DefaultLoader, IndexItemSpider
from w3lib.html import remove_tags
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity, Compose


class CustomLoader(DefaultLoader):
    name_in = MapCompose(remove_tags, unicode.strip, unicode.upper)


def items_selector(s, r):
    return r.css('li.item')


def item_url_selector(s, i):
    i.css('a.url::attr(href)')


def next_page_url_fn_selector(s, r):
    # return r.xpath("//a[contains(.//text(), 'Next')]/@href")
    return r.xpath("//a[contains(.//text(), 'Next')]/@href")


class Yelp(IndexItemSpider):
    name = "yelp"
    # allowed_domains = ['']
    start_urls = ['https://www.yelp.com/search?find_desc=restaurant&find_loc=New+York,+NY,+United+States&start=0']
    ajax = True

    items_selector = items_selector
    item_url_selector = 'a.url::attr(href)'

    index_attrs = {'transmission': '.last dd:nth-child(6)',
                   'image_urls': '.photo::attr(src)'}
    item_attrs = {'name': '.ddc-page-title'}

    next_page_url_selector = next_page_url_fn_selector
    
    print("next_page_url_selector" + str(next_page_url_selector))
    print("item_url_selector" + str(item_url_selector))

    loader = CustomLoader

    items_per_page_limit = 4
    pages_limit = 1
