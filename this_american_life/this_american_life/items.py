# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TalTranscriptItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	episode_id = scrapy.Field()
	episode_num_text = scrapy.Field()
	year = scrapy.Field()
	radio_date_text = scrapy.Field()
	radio_date_datetime = scrapy.Field()
	episode_title = scrapy.Field()
	episode_hosts = scrapy.Field()
	act_id = scrapy.Field()
	line_id = scrapy.Field()
	begin_timestamp = scrapy.Field()
	speaker_class = scrapy.Field()
	speaker_name = scrapy.Field()
	line_text = scrapy.Field()
	full_audio_link = scrapy.Field()
	transcript_url = scrapy.Field()