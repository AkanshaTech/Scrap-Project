from typing import Any
import scrapy
from requests import Response
from .items import QuotetorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        #'https://quotes.toscrape.com/page/1/'
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1701075152&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = QuotetorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = 'https://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
