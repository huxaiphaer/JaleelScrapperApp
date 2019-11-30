# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JaleelscrapperPipeline(object):

    def __init__(self):
        self.create_connection()
        # self.create_dabatase()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='',
                                            database='flights_db'
                                            )
        self.curr = self.conn.cursor()

    def create_dabatase(self):
        self.curr.execute("""Create Database  flights_db""")

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS  flights_tb""")
        self.curr.execute("""Create table flights_tb(
           id int primary key auto_increment,
           destination varchar(45),
           time varchar(45),
           temperature varchar(45),
           note varchar(45)
           )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into flights_tb(destination,time,temperature,note) values(%s,%s,%s)""",
                          (item['destination'],
                           item['time'],
                           item['temperature'],
                           item['note']
                           ))
        self.conn.commit()
