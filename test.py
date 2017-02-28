from living_search.spiders.bilibili import *
from living_search.dbHelper import *
from scrapy.crawler import CrawlerRunner,reactor
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings  # 导入seetings配置
# db = DBHelper()
# sql = "select a.sample_topicsID as topics_id,a.sample_keyword as word,a.t_rule_id as rule_id  from sample_keywords a order by sample_topicsID desc"
# params = ()
# data = db.find(sql, *params)
settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
settings.set("ITEM_PIPELINES" , {
    'living_search.pipelines.DatabasePipeline': 300,
})
data = [(0,'柯南',0),(1,'银魂',1)]
runner = CrawlerRunner(settings)
d = runner.crawl(BilibiliSpider,wordlist=data)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished