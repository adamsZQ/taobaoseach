#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pymongo
from config import *


class ToMongo():
    def __init__(self):
        client = pymongo.MongoClient(MONGO_URL, 27017)
        self.db = client[MONGO_DB]


    def save_to_mongo(result):
        try:
            if db[MONGO_TABLE].insert(result):
                print("保存成功")
        except Exception as e:
            print("保存失败")
