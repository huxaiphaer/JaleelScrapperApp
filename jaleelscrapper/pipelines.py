# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import os
from dotenv import load_dotenv


class JaleelscrapperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # load variables from .env file
        load_dotenv()
        self.conn = mysql.connector.connect(host=os.getenv("HOST"),
                                            user=os.getenv("USER_NAME"),
                                            password=os.getenv("PASSWORD"),
                                            database=os.getenv("DATABASE"),
                                            auth_plugin='mysql_native_password'
                                            )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS  flights_tb""")
        self.curr.execute("""CREATE TABLE flights_tb(
           id int primary key auto_increment,
           Destination VARCHAR(75),
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
