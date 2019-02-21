# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request

from scrapy_stock.items import StockItem


class StockSpider(scrapy.Spider):
    name = 'stock'

    def start_requests(self):
        url = 'http://quote.eastmoney.com/stocklist.html'
        yield Request(url)

    def parse(self, response):
        item = StockItem()
        print "===============上海================"
        stocks_sh = response.css('div#quotesearch ul li a[href*="http://quote.eastmoney.com/sh"]::text')
        for stock in stocks_sh:
            item['stock_id'] = 's_sh' + re.findall('\((.*?)\)', stock.extract())[0]
            yield item

        print "===============深圳================"
        stocks_sz = response.css('div#quotesearch ul li a[href*="http://quote.eastmoney.com/sz"]::text')
        for stock in stocks_sz:
            item['stock_id'] = 's_sz' + re.findall('\((.*?)\)', stock.extract())[0]
            yield item
