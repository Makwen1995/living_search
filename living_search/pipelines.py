# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .dbHelper import *
import datetime,codecs,json
class JsonWithEncodingPipeline(object):
    '''保存到文件中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''
    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')#保存为json文件
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"#转为json的
        self.file.write(line)#写入文件中
        return item
    def spider_closed(self, spider):#爬虫结束时关闭文件
        self.file.close()

class DatabasePipeline(object):
    '''保存到数据库中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''

    def __init__(self):
        self.db = DBHelper()

    # pipeline默认调用
    def process_item(self, item, spider):
        if spider.name == 'bilibili':
            print(item['name'])
        #sql = "insert into t_info_copy_test (name,abstract,source_url,keyword,subject_id,input_time,rule_id,uploader,source_type_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #params = (item["name"], item['abstrct'], item["url"], item['keyword'], item['subject_id'], datetime.datetime.now(),
        #item['rule_id'], 'PACHONG')
        #self.db.insert(sql, params)
