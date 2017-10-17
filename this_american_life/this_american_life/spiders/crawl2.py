# -*- coding: utf-8 -*-
import scrapy
from this_american_life.items import TalTranscriptItem

class CrawlSpider(scrapy.Spider):
	name = "transcript2"
	allowed_domains = ["https://www.thisamericanlife.org/radio-archives/episode/1/transcript"]
	start_urls = (
		'https://www.thisamericanlife.org/radio-archives/episode/1/transcript',
	)

	def parse(self, response):
		item = TalTranscriptItem()
		#for line in response.xpath('//div'):
		item['episode_id'] = response.xpath('//div[contains(@class, "radio-episode-num")]/text()').extract()
		item['episode_num_text'] = response.xpath('//div[contains(@class, "radio-wrapper")]/@id').extract()
		item['radio_date_text'] = response.xpath('//div[contains(@class, "radio-date")]/text()').extract()
		item['episode_title'] = response.xpath('//h2').xpath('a[contains(@href, *)]/text()').extract()
		item['begin_timestamp'] = response.xpath('//p[contains(@begin, *)]/@begin').extract()
		item['speaker_class'] = response.xpath('//div/@class').extract()
		item['speaker_name'] = response.xpath('//h4/text()').extract()
		item['line_text'] = response.xpath('//p[contains(@begin, *)]/text()').extract()
		item['full_audio_link'] = response.xpath('//p[contains(@class, "full-audio")]/text()').extract()
		#item['line_id'] = ''
		#item['transcript_url'] = ''	
		#item['year'] = ''
		#item['radio_date_datetime'] = ''
		#item['episode_hosts'] = response.xpath('//div[contains(@class, "host")]').xpath('h4/text()').extract()
		#item['act_id'] = response.xpath('//div[contains(@class, "act")]/@id').extract()
		yield item

	#	def parse_dir_contents(self, response):

