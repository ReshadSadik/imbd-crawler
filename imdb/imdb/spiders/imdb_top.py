# -*- coding: utf-8 -*-
import scrapy


class ImdbTopSpider(scrapy.Spider):
    name = 'imdb_top'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        pass
