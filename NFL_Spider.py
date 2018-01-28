import scrapy
import pandas as pd


class NFL_Spider(scrapy.Spider):

    name = 'player_info'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    df = pd.read_csv('~/ds/metis/work/scrapy/tutorial/tutorial/spiders/nfl_players.csv')
    df_qb = df[df.pos == 'QB']
    df_qb['full_url'] = df_qb.apply(lambda x: 'https://www.pro-football-reference.com' + x['url'], axis=1)
    url_list = df_qb.full_url.tolist()

    start_urls = url_list

    def parse(self, response):
        try:
            name = response.xpath('//div[@id="meta"]/div/h1/text()').extract()[0]
        except:
        	name = 0
        try:
            throws = response.xpath('//div[@id="meta"]/div/p/text()').extract()[4]
        except:
        	throws = 0
        try:
            height = response.xpath('//div[@id="meta"]/div/p/span/text()').extract()[0]
        except:
        	height = 0
        try:
            weight = response.xpath('//div[@id="meta"]/div/p/span/text()').extract()[1]
        except:
        	weight = 0
        try:
            home_state = response.xpath('//div[@id="meta"]/div/p/span/a/text()').extract()[1]
        except:
        	home_state = 0
        try:
            home_city = response.xpath('//div[@id="meta"]/div/p/span/text()').extract()[4]
        except:
            home_city = 0


        yield {
        	'name': name,
            'throws': throws,
            'height': height,
            'weight': weight,
            'home_state': home_state,
            'home_city': home_city
        }        