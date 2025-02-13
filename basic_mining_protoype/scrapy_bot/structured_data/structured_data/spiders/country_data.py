import scrapy


class CountryDataSpider(scrapy.Spider):
    name = "country_data"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ['https://www.scrapethissite.com/pages/simple/']

    def parse(self, response):
        # Select all country containers
        countries = response.css('div.col-md-4.country')
        for country in countries:
            # Extract all text from the h3 tag and join it to handle whitespace or nested elements
            country_name = country.xpath('./h3[@class="country-name"]/text()').getall()
            country_name = ''.join(country_name).strip() if country_name else None

            yield {
                'country': country_name,
                'capital': country.css('span.country-capital::text').get(),
                'population': country.css('span.country-population::text').get(),
                'area': country.css('span.country-area::text').get(),
            }
