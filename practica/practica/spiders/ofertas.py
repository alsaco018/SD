# -*- coding: utf-8 -*-
import scrapy
from practica.items import PracticaItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider



class OfertasSpider(CrawlSpider):
    name = 'ofertas'
    allowed_domains = ['icaro.ual.es', 'icaro.ual.es/Portal']
    start_urls = ['http://icaro.ual.es/']

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="pie_oferta"]/a')),
             callback = 'parse_item', follow = False)
        }
    def parse_item(self, response):
        enlace = response.css('::attr(href)').extract_first()
        #titulo = response.xpath('//div[3]/dl[1]/dt[constains(., "Estudios")]/following-sibling::dd[1]/ul[contains(., "Informática")]').extract()
        #if titulo is not None:
        i = PracticaItem()
        i['descripcion_ofr'] = response.xpath('//div[3]/dl[1]/dt[contains (.,"Tareas a Realizar")]/following-sibling::dd[1]/text()').extract()
        i['salario_ofr'] = response.xpath('//div[3]/dl[1]/dt[contains (.,"Retribución/Mes")]/following-sibling::dd[1]/text()').extract()
        i['localidad_ofr'] = response.xpath('//div[3]/dl[1]/dt[contains (.,"Localidad")]/following-sibling::dd[1]/text()').extract()
        i['fechaIni_ofr'] = response.xpath('//div[3]/dl[1]/dt[contains (.,"Fecha de Incorporación")]/following-sibling::dd[1]/text()').extract()
        i['duracion_ofr'] = response.xpath('//div[3]/dl[1]/dt[contains (.,"Duración")]/following-sibling::dd[1]/text()').extract()
        i['enlace_ofr'] = response.extract()
            
        yield i

            
"""
    def parse(self, response):
        anuncios = response.xpath('//div[@class="cluster_capsule"]')
        enlace = response.css('div.cluster_capsule::attr(href)').extract_first()

        for anuncio in anuncios:
            descripcion = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Tareas a Realizar")]/following-sibling::dd[1]/text()').extract()
            salario = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Retribución/Mes")]/following-sibling::dd[1]/text()').extract()
            localidad = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Localidad")]/following-sibling::dd[1]/text()').extract()
            fechaInicio = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Fecha de Incorporación")]/following-sibling::dd[1]/text()').extract()
            duracion = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Duración")]/following-sibling::dd[1]/text()').extract()
               
            yield{"Descripcion": descripcion, "Salario": salario, "Localidad": localidad, "Fecha de inicio": fechaInicio, "Duracion": duracion, "Oferta": enlace}

       # page_num = get_page(response)

        #next = response.xpath('//a[text()="Siguiente"]')

        if enlace is not None :
            next_page = enlace
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    

    def parse(self, response):
        practicas = response.xpath('//div[@class="cluster_capsule"]')

        for practica in practicas:
            enlace = response.css('div.cluster_capsule::attr(href)').extract_first()
            titulo = enlace.xpath('div[3]/dl[1]/dt[constains(., "Estudios")]/following-sibling::dd[1]/ul[contains(., "Informática")]').extract()
            if titulo is not None:
               descripcion = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Tareas a Realizar")]/following-sibling::dd[1]/text()').extract()
               salario = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Retribución/Mes")]/following-sibling::dd[1]/text()').extract()
               localidad = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Localidad")]/following-sibling::dd[1]/text()').extract()
               fechaInicio = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Fecha de Incorporación")]/following-sibling::dd[1]/text()').extract()
               duracion = enlace.xpath('//div[3]/dl[1]/dt[contains (.,"Duración")]/following-sibling::dd[1]/text()').extract()
               
               yield{"Descripcion": descripcion, "Salario": salario, "Localidad": localidad, "Fecha de inicio": fechaInicio, "Duracion": duracion, "Oferta": enlace}
               
               """
