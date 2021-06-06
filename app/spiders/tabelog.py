import scrapy


class TabelogSpider(scrapy.Spider):
    name = 'tabelog'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/rstLst/cafe/']

    def parse(self, response):
        tabelog = response.xpath('//')
