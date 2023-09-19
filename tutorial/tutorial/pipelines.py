# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

from tutorial.items import Products, Reviews


class TutorialPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'web-bot.mysql.database.azure.com',
            user = 'admin111',
            password = 'webBot111',
            database = 'web-bot'
        )

        # Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        # Create table if none exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id int NOT NULL auto_increment,
            brand text,
            name text,
            description text,
            sku VARCHAR(25),
            upc VARCHAR(25),
            ean VARCHAR(25),
            mpn VARCHAR(25),
            PRIMARY KEY(id)
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews(
            id int NOT NULL auto_increment,
            user text,
            date date,
            platform text,
            title text,
            content text,
            rating integer,
            productname text,
            PRIMARY KEY(id)
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id int NOT NULL auto_increment,
            categoryname text,
            productname text,
            PRIMARY KEY(id)
        )
        """)

    def process_item(self, item, spider):
        if isinstance(item, Products):
            self.cur.execute("select * from products where name = %s",(item['name'],))
            result = self.cur.fetchone()
            if result:
                spider.logger.warn('Product already in db: %s' %item['name'])
            else:
                self.cur.execute("""insert into products (brand, name, description, sku, upc, ean, mpn) values (%s,%s,%s,%s,%s,%s,%s)""",(
                    item["brand"],
                    item["name"],
                    item["description"],
                    item["sku"],
                    item["upc"],
                    item["ean"],
                    item["mpn"]
                ))
        if isinstance(item, Reviews):
            self.cur.execute("select * from reviews where content = %s",(item['content'],))
            result = self.cur.fetchone()
            if result:
                spider.logger.warn('Review already in db: %s' %item['title'])
            else:
                self.cur.execute("""insert into reviews (user, date, platform, title, content, rating, productname) values (%s,'%Y-%m-%d',%s,%s,%s,%d,%s)""",(
                    item["user"],
                    item["date"],
                    item["platform"],
                    item["title"],
                    item["content"],
                    item["rating"],
                    item["productname"]
                ))
        # if isinstance(item, Categories):
        #     self.cur.execute("select * from categories where categoryname = %s",(item['categoryname'],))
        #     result = self.cur.fetchone()
        #     if result:
        #         spider.logger.warn('Catgory already in db: %s' %item['categoryname'])
        #     else:
        #         self.cur.execute("""insert into categories (categoryname, productname) values (%s,%s)""",(
        #             item["categoryname"],
        #             item["productName"],
        #         ))

        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()