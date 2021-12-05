import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/shelf/show/fiction']

    def parse(self, name, **kwargs):
        print(response.css('bookData').getall())

    def parse_books(self, response):
        title = response.css('#itemTitle::text').getall()[0]
        yield {
          "title": title,
          "author": response.css('author::text').getall()[0],
          "rating": response.css('rating::text').getall()[1]
        }


