# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticaItem(scrapy.Item):
    
    descripcion_ofr = scrapy.Field()
    salario_ofr = scrapy.Field()
    localidad_ofr = scrapy.Field()
    fechaIni_ofr = scrapy.Field()
    duracion_ofr = scrapy.Field()
    enlace_ofr = scrapy.Field()
    titulos_ofr = scrapy.Field()
