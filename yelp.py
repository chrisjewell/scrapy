# -*- coding: utf-8 -*-
import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ["crawlspider"]
    start_urls = (
        'http://www.crawlspider/',
    )

    def parse(self, response):
        pass
