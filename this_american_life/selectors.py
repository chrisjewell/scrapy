https://www.thisamericanlife.org/radio-archives/episode/1/transcript




list_of_lines = response.xpath('//div[contains(@class, *)]').xpath('//p').extract()

interviewer_name = response.xpath('//div[contains(@class, "interviewer")]').xpath('h4/text()').extract()

timestamp = response.xpath('//p[contains(@begin, *)]/@begin').extract()

line_text = response.xpath('//p[contains(@begin, *)]/text()').extract()

host_name = response.xpath('//div[contains(@class, "host")]').xpath('h4/text()').extract()

speaker_name = response.xpath('//h4/text()').extract()
subject_name = response.xpath('//div[contains(@class, "subject")]/h4/text()').extract()

speaker_class = response.xpath('//div/@class').extract()

radio_date_text = response.xpath('//div[contains(@class, "radio-date")]/text()').extract()

act_id = response.xpath('//div[contains(@class, "act")]/@id').extract()

episode_num_text = response.xpath('//div[contains(@class, "radio-wrapper")]/@id').extract()

episode_id = response.xpath('//div[contains(@class, "radio-episode-num")]/text()').extract()

episode_title = response.xpath('//h2').xpath('a[contains(@href, *)]/text()').extract()

copyright = response.xpath('//div[contains(@class, "copyright")]/text()').extract_first()

full_audio_link = response.xpath('//p[contains(@class, "full-audio")]/text()').extract()