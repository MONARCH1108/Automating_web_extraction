import scrapy


class TagspiderSpider(scrapy.Spider):
    name = "tagspider"
    allowed_domains = ["geeksforgeeks.org"]
    start_urls = ["https://www.geeksforgeeks.org/html-tags-a-to-z-list/"]

    def parse(self, response):
        tags = response.xpath('//*[@id="post-315322"]/div[3]/table/tbody/tr')
        for tag in tags:
            yield {
                'name': tag.xpath('./td[1]/a/span/text()').get(),
                'description': tag.xpath('./td[2]/span/text()').get(),
                'tag': tag.xpath('./td[3]/span/text()').get(),
            }

