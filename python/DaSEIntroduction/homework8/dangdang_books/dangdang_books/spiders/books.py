import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        books = response.css('.con li')
        for book in books:
            title = book.css('.name a::text').get()
            author = book.css('.publisher_info a::text').get()
            price = book.css('.price span::text').get()
            yield {
                'title': title,
                'author': author,
                'price': price
            }
