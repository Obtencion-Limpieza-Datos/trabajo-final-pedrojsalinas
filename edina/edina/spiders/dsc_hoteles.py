import scrapy
import pandas as pd

df=pd.read_csv('hoteles.csv')
df['url'] ='https://www.edina.com.ec/'+df['url']


class DetalleSpider(scrapy.Spider):
    name = "detalle"
    start_urls = df['url']

    def parse(self, response):
        lista = response.css('#ctl00')
        for l in lista.css('.box_cntN'):
            nombre = l.xpath('strong/a/h2/text()').extract()[0]
            direccion =l.xpath('p[1]/text()').extract()[0].replace('Dirección: ','')
            ubicacion =l.xpath('p[2]/text()').extract()[0].replace('Ubicación: Ecuador, ','')
            telefono=l.xpath('p[3]/strong/text()').extract()[0]
            yield {
                'nombre': nombre,
                'direccion': direccion,
                'ubicacion': ubicacion,
                'telefono': telefono,
                    }
        #pagina siguiente
        next_page = response.css('.estcajaBotonF').xpath('a/@href').extract()[0]
        if next_page is not None:
            print(response.urljoin(next_page))
            next_page = 'https://www.edina.com.ec/'+next_page
            yield scrapy.Request(next_page, callback=self.parse)
