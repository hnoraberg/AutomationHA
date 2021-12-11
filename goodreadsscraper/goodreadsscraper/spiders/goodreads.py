import scrapy
from ..items import GoodreadsscraperItem

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/shelf/show/fiction']

    def parse(self, response):
        try:
            items = GoodreadsscraperItem()

            author = response.css('a.authorName span::text').getall(),
            book_title = response.css('.bookTitle::text').getall(),
            rating = response.css('.greyText::text').getall()

            items['author'] = author
            items['book_title'] = book_title
            items['rating'] = rating

            yield items
        except Exception as e:
            print(e)
            return

