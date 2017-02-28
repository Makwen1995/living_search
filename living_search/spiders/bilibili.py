# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from living_search.items import HostItem,LivingItem,ResultItem

class BilibiliSpider(Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    wordlist=[]
    def __init__(self, **kw):
        super(BilibiliSpider, self).__init__(**kw)
        wordlist = kw.get('wordlist')
        self.wordlist = wordlist


    def start_requests(self):
        pages = []
        for word in self.wordlist:
            requesturl = "http://live.bilibili.com/search/index/?keyword={0}".format(word[1])
            print(requesturl)
            pages.append(Request(requesturl, callback=self.parse, dont_filter=True,cookies={"topics_id":word[0],"keyword":word[1],"rule_id":word[2]}))
        return pages

    def parse(self, response):
        livingItems,hostItems,abstract=[],[],''
        for element in response.xpath('//ul[contains(@class, "room-list")]/li/a'):
            title=element.xpath('.//div[@class="listVtitle"]/text()').extract()
            host = element.xpath('.//div[@class="upTitle"]/text()').extract()
            peopleNum = element.xpath('.//div[@class="peopleNum"]/text()').extract()
            livingItems.append(LivingItem({'title': title, 'host': host, 'peopleNum': peopleNum}))
        for element2 in response.xpath('//ul[contains(@class, "anchor-list")]/li/a'):
            name=element2.xpath('.//div[@class="user-title"]/text()').extract()
            followers = element2.xpath('.//span[@class="star"]/text()').extract()
            channel = element2.xpath('.//span[@class="category-name single"]/text()').extract()
            hostItems.append(HostItem({'name': name, 'followers': followers, 'channel': channel}))
        living_len, host_len =len(livingItems),len(hostItems)
        if living_len>0:
            abstract += '共有'+str(living_len)+'个直播间：'+str(livingItems[:2])
        if host_len >0:
            abstract +='\n共有'+str(host_len)+'位主播：'+str(hostItems[:2])
        if abstract == '':
            return
        item =ResultItem()
        item.name = '哔哩哔哩直播-'+response.request.cookies['keyword']
        item.abstract = abstract
        item.keyword = response.request.cookies['keyword']
        item.url=response.url
        item.subject_id = response.request.cookies['topics_id']
        item.rule_id = response.request.cookies['rule_id']
        yield item