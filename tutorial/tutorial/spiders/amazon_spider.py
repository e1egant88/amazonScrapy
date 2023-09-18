from pathlib import Path
import nltk
import string
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon"
    def start_requests(self):
        # Tech & electronics category
        root = 'https://www.amazon.com.au/electronics-store/b/?ie=UTF8&node=4851799051&ref_=nav_cs_electronics'
    
        yield scrapy.Request(url=root, callback=self.secCat)

    def secCat(self,response):
        secLvCat = response.xpath('//*[@class="a-spacing-micro apb-browse-refinements-indent-2"]/span/a/@href').getall()
        if len(secLvCat) != 0 :
            # test with 1st secLvCat
            for url in secLvCat[0:1]:
                yield response.follow(url, callback=self.parseCat)
        # else:
        #     currentUrl = response.request.url
        #     yield scrapy.Request(currentUrl, callback=self.parseBottomCat)

    def parseCat(self, response):
        LvCatAfterSec = response.xpath('//*[@class="a-spacing-micro s-navigation-indent-2"]/span/a/@href').getall()
        if len(LvCatAfterSec) != 0:
            # test with 1st LvCatAfterSec
            for url in LvCatAfterSec[0:1]:
                print('--------------------')
                print(url)
                yield response.follow(url, callback=self.parseCat)     
        else:
            print('=======================')
            currentUrl = response.request.url
            print(currentUrl)
            yield response.follow(currentUrl, callback=self.parseBottomCat)

    def parseBottomCat(self, response):
        # secLvCat = response.xpath('//*[@class="a-spacing-micro s-navigation-indent-2"]/span/a/@href').getall()
        print("currURL: "+response.request.url)
        seeAllBtn = response.xpath('//*[@class="a-cardui-body"]/a/@href').get()
        if seeAllBtn is not None:
            yield response.follow(seeAllBtn, callback=self.parseBottomCat)
        else:
            products = response.xpath('//*[@class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]/div/div/div/div/div/span/a/@href').getall()
            if len(products) != 0:
                for url in products[0:1]:
                    print(url)
                    yield response.follow(url, callback=self.parsePdct)
                nextBtn = response.xpath('//*[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]/@href').get()
                if nextBtn is not None:
                    yield response.follow(nextBtn, callback=self.parseBottomCat)
                else:
                    print('---------this page over---------')
            else:
                print('---no product in the category---')

    def parsePdct(self, response):
        brand = response.xpath('//*[@class="a-spacing-small po-brand"]/td[@class="a-span9"]/span/text()').get()
        name = response.xpath('//*[@id="productTitle"]/text()').get()
        name = name.strip()
        '''
        # replace name with tokens
        for i in string.punctuation:
            name = name.replace(i,'')
        name = nltk.word_tokenize(name)
        '''
        description = ''
        # SKU = None
        # UPC = None
        # EAN = None
        MPN = response.xpath('//th[text()=" Item Model Number "]/following-sibling::td/text()').get()
        if MPN is not None:
            MPN = ''.join(filter(str.isalnum,MPN))
        else:
            #for test
            MPN = 'abc'
        #save
        with open('products.txt','a') as f:
            f.write(name+'\n')

        seeMoreBtn = response.xpath('//a[@class="a-link-emphasis a-text-bold"]/@href').get()
        if seeMoreBtn is not None:
            yield response.follow(seeMoreBtn, callback=self.parseReviews)

        
    def parseReviews(self, response):
        divXpath = '//div[@class="a-section review aok-relative"]'
        div = response.xpath('//div[@class="a-section review aok-relative"]')
        if len(div) != 0:
            # for d in range(1,len(div)+1):
            for d in range(1,2):
                rating = response.xpath(divXpath+'[%d]'%d+'/div/div/div/a/i/span/text()').get()
                if rating is not None:
                    rating = [e.strip() for e in rating]
                    rating = int(rating[0])
                user = response.xpath(divXpath+'[%d]'%d+'/div/div/div/a/div/span/text()').get()
                date = response.xpath(divXpath+'[%d]'%d+'/div/div/span/text()').get()
                if date is not None:
                    # parse date format
                    pass
                platform = 'Amazon'
                title = response.xpath(divXpath+'[%d]'%d+'/div/div/div/a/span[2]/text()').get()
                content = response.xpath(divXpath+'[%d]'%d+'/div/div/div/span/span/text()').get()
                # save
                with open('reviews.txt','a') as f:
                    f.write(content+'\n')
            nextPageBtn = response.xpath('//li[class="a-last"]/a/@href').get()
            if nextPageBtn is not None:
                yield response.follow(nextPageBtn, callback=self.parseReviews)