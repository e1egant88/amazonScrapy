from pathlib import Path
import numpy as np
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = "123"
        # filename = f"quotes-{page}.txt"
        # Path(filename).write_text("abc")
        # self.log(f"Saved file {filename}")
        
        with open('a.txt','a') as f:
            f.write('aaa\n')