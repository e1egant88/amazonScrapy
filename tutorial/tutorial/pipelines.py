# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class TutorialPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'testserver10086.mysql.database.azure.com',
            user = 'songbaihu',
            password = 'Letsgo98',
            database = 'testserver10086'
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
            productName text,
            PRIMARY KEY(id)
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id int NOT NULL auto_increment,
            categoryName text,
            productName text,
            PRIMARY KEY(id)
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""insert into products (brand, name, description, sku, upc, ean, mpn) values (%s,%s,%s,%s,%s,%s,%s)""",(
            item["brand"],
            item["name"],
            item["description"],
            item["sku"],
            item["upc"],
            item["ean"],
            item["mpn"]
        ))

        self.cur.execute("""insert into reviews (user, date, platform, title, content, rating, productName) values (%s,'%Y-%m-%d',%s,%s,%s,%d,%s)""",(
            item["user"],
            item["date"],
            item["platform"],
            item["title"],
            item["content"],
            item["rating"],
            item["productName"]
        ))

        self.cur.execute("""insert into categories (categoryName, productName) values (%s,%s)""",(
            item["categoryName"],
            item["productName"],
        ))
