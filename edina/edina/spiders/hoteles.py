import scrapy

class ExamenSpider(scrapy.Spider):
    name = "hotel"
    start_urls = ['https://www.edina.com.ec/guia-telefonica/hoteles.aspx']

    def parse(self, response):
        # seleccion de tipo de url
        for l in response.css('.grid_2'):
            for i in l.xpath('ul/li'):
                nombre=i.css('a::text').extract_first()
                url=i.xpath('a/@href').extract()[0].strip()
                yield {
                    'nombre': nombre,
                    'url': url,
                        }
