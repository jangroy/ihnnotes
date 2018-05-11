# -*- coding: utf-8 -*-
import scrapy
import logging
import re
from tester.items import EmailItem
from scrapy_splash import SplashRequest

class EmailSpider(scrapy.Spider):
    name = 'email'
    # allowed_domains = ['https://www.ritabk.com/']
    # use splash form filler
    # use email filter
    # duplicate filter
    http_user = '94c0310b124b48b596f0cda907506399'

    start_urls = ['https://www.yelp.com/search?find_desc=restaurant&find_loc=New+York,+NY,+United+States&start=0']

    def start_requests(self):
        for url in self.start_urls:
            logging.warning("This is a the url to parse" + url)
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):

        links = response.xpath('//a/@href').extract()
        crawledLinks = []
        
        for link in links:
        # If it is a proper link and is not checked yet, yield it to the Spider
            if not link in crawledLinks:
                link = "http://code.tutsplus.com" + link
                crawledLinks.append(link)
                yield SplashRequest(link, self.parse)

        
        def parse3(response):
            print("####finding emails")
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.body)
            print("####============================================================================================")
            print(emails)
            print("####============================================================================================")

        def parse2(response):
            print("####grab biz_website")
            yelp_biz_website = response.css('li span.biz-website a::attr(href)').extract_first()
            new_yelp_biz_website = 'https://www.yelp.com' + yelp_biz_website
            print(new_yelp_biz_website)

            if new_yelp_biz_website is not None:
                print("####going to biz website")
                yield SplashRequest(new_yelp_biz_website, callback=parse3,
                    endpoint='render.html',
                    args={'wait': 0.5},
                )
            
        self.logger.info('------------------------------Parse function called on %s', response.url)
        print("###############################start parse")
        yelp_biz_yelp_url = response.css('span.indexed-biz-name a.biz-name::attr(href)').extract()
        print("####got urls")
        print(yelp_biz_yelp_url)

        for yelp_url in yelp_biz_yelp_url:
            print("####find each yelp url")
            new_yelp_url = 'https://www.yelp.com' + yelp_url
            print(new_yelp_url)

            
            # yelp_biz_name = response.css('span.indexed-biz-name a.biz-name span::text').extract_first()
            
            
            print("####going to yelp url")
            yield SplashRequest(new_yelp_url, callback=parse2,
                endpoint='render.html',
                args={'wait': 0.5},
            )
    
        

        
        print("#####################################going to next page")
        next_page = 'https://www.yelp.com' + str(response.css('a.next::attr(href)').extract_first())
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
