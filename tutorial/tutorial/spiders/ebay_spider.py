from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ebay"

    def start_requests(self):
        # Tech & electronics category
        root = 'https://www.ebay.com.au/b/Electronics/bn_7000259947'
    
        yield scrapy.Request(url=root, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")