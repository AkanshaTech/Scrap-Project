from typing import Any
import scrapy
from requests import Response
from scrapy.http import FormRequest, Response
from scrapy.utils.response import open_in_browser
from ..items import QuotetorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes_spider'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
  

def parse(self,response):
        title=response.css('title::text').extract()
        yield{'titletext':title}



    # def parse(self, response: Response, **kwargs: Any) -> Any:
    #     token = response.css('form input::attr(value)').extract_first()
    #     return FormRequest.from_response(response, formdata={
    #         'crsf_token': token,
    #         'username': 'attreya01@gmail.com',
    #         'password': 'vchzchvzc'

    #     }, callback=self.start_scraping)

    # def start_scraping(self, response):
    #     open_in_browser(response)
    #     items = QuotetorialItem()
    #     all_div_quotes = response.css('div.quote')

    #     for quotes in all_div_quotes:
    #         title = quotes.css('span.text::text').extract()
    #         author = quotes.css('.author::text').extract()
    #         tag = quotes.css('.tag::text').extract()

    #         items['title'] = title
    #         items['author'] = author
    #         items['tag'] = tag

    #         yield items
