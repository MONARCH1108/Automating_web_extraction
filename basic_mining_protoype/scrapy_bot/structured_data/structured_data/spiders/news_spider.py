import scrapy


class NewsSpiderSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/"]

    def parse(self, response):
        news_items = response.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[2]/div/div/div/ul/li')

        for news in news_items:
            yield {
                'news_title': news.xpath('.//section/div/a/h3/text()').get()
            }
