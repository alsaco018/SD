# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv
from scrapy.exporters import JsonItemExporter
import json
#from sqlalchemy.orm import sessionmaker
#from practica.Models import QuoteSB, db_connect, create_table

class PracticaPipeline(object):
    
    @classmethod
    #crea un archivo json con los datos obtenidos por la spider al abrirse y cerrarse
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        
        return pipeline

    def spider_opened(self, spider):
        self.file2 = open('Datos/%s_items.json' % spider.name, 'w+b')
        self.exporter = JsonItemExporter(self.file2, encoding='utf-8',ensure_ascii = False)
        self.exporter.fields_to_export = ['descripcion_ofr', 'salario_ofr', 'localidad_ofr','fechaIni_ofr', 'duracion_ofr', 'enlace_ofr']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file2.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
