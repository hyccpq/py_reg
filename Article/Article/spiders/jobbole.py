# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/113789/']

    def parse(self, response):
        re_selector = response.xpath('//*[@id="post-113789"]/div[1]/h1/text()')
        print(re_selector)
        pass
