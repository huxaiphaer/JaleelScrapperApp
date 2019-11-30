# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class JaleelscrapperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='',
                                            database='flights_db'
                                            )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS  flights_tb""")
        self.curr.execute("""CREATE TABLE flights_tb(
           id int primary key auto_increment,
           Destination VARCHAR(45),
           Time TIME,
           Temperature VARCHAR(45),
           Note VARCHAR(45)
           )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO flights_tb(destination,time,temperature,note) values(%s,%s,%s,%s)""",
                          (item['destination'],
                           item['time'],
                           item['temperature'],
                           item['note']
                           ))
        self.conn.commit()
