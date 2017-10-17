# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TalSpider(CrawlSpider):
    name = 'tal'
    allowed_domains = ['https://www.thisamericanlife.org/radio-archives/episode/']
    start_urls = ['https://www.thisamericanlife.org/radio-archives/episode/1/transcript/']

    def parse(self, response):
				
		for line in response.xpath('//div'):
			episode_num_text = line.xpath('.//div[contains(@class, "radio-wrapper")]/@id').extract()
			radio_date_text = line.xpath('.//div[contains(@class, "radio-date")]/text()').extract()
			episode_title = line.xpath('.//h2').xpath('a[contains(@href, *)]/text()').extract()
			begin_timestamp = line.xpath('.//p[contains(@begin, *)]/@begin').extract()
			speaker_class = line.xpath('.//div/@class').extract()
			speaker_name = line.xpath('.//h4/text()').extract()
			line_text = line.xpath('.//p[contains(@begin, *)]/text()').extract()
			full_audio_link = line.xpath('.//p[contains(@class, "full-audio")]/text()').extract()
			# #transcript_url = ''    
			# #episode_id = line.xpath('.//div[contains(@class, "radio-episode-num")]/text()').extract()
			# #year = ''
			# #radio_date_datetime = ''
			# #episode_hosts = line.xpath('.//div[contains(@class, "host")]').xpath('h4/text()').extract()
			# #act_id = line.xpath('.//div[contains(@class, "act")]/@id').extract()
			# #line_id = ''
			
			
			
			for item in zip(episode_num_text, radio_date_text, episode_title, begin_timestamp, speaker_class, speaker_name, line_text, full_audio_link):
				scraped_info = {
					'episode_num_text' : item[0], 
					'radio_date_text' : item[1], 
					'episode_title' : item[2],
					'begin_timestamp' : item[3], 
					'speaker_class' : item[4],
					'speaker_name' : item[5], 
					'line_text' : item[6], 
					'full_audio_link' : item[7],
					}
				yield scraped_info

		