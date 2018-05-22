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

    #Definimos la regla de que se extraiga el enlace de cada una de las ofertas y se llame al método parse_item para cada una de ellas
    rules = {Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="pie_oferta"]/a')),
                               callback = 'parse_item', follow = False)}
    
    

    def parse_item(self, response):

 #declaramos el objeto i que tiene las variables que vamos a almacenar. 
        i = PracticaItem()
        #obetenemos todos los titulos asociados a una oferta
        for node in response.xpath('//div/dl/dt[contains(., "Estudios")]/following-sibling::dd[1]'):
            titulos = node.css('::text').extract()

        print(titulos)
        #incluimos en el objeto i aquellas ofertas que necesiten el grado en ingeniería informática
        if 'Grado en Ingeniería Informática'  in titulos:       
            i['descripcion_ofr'] = response.xpath('//div/dl/dt[contains (.,"Tareas a Realizar")]/following-sibling::dd[1]/text()').extract()
            i['salario_ofr'] = response.xpath('//div/dl/dt[contains (.,"Retribución/Mes")]/following-sibling::dd[1]/text()').extract()
            i['localidad_ofr'] = response.xpath('//div/dl/dt[contains (.,"Localidad")]/following-sibling::dd[1]/text()').extract()
            i['fechaIni_ofr'] = response.xpath('//div/dl/dt[contains (.,"Fecha de Incorporación")]/following-sibling::dd[1]/text()').extract()
            i['duracion_ofr'] = response.xpath('//div/dl/dt[contains (.,"Duración")]/following-sibling::dd[1]/text()').extract()
            i['enlace_ofr'] = response
            yield i

        

   