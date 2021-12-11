import scrapy


class GoodreadsscraperItem(scrapy.Item):
    book_title = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()



