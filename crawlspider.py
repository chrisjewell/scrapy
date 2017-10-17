# -*- coding: utf-8 -*-
import scrapy


class CrawlspiderSpider(scrapy.Spider):
    name = "crawlspider"
    allowed_domains = ["yelp"]
    start_urls = (
        'http://www.yelp/',
    )

    def parse(self, response):
        pass
