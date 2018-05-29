from bottle import get,post,run,route,request
import dropbox
import csv
import tempfile
import io
import json
import io
import sys

@get('/practicas')
def do_hello():
	s =""
    #obtiene de dropbox el archivo json para mostrar los datos de las ofertas seleccionadas
	token = "Yr8Bgt_dfoAAAAAAAAAABkznS8pe-ow3Uh-ouk4pApmqPy8p0l8_XPkZR3k1S1Ev"
	dbx = dropbox.Dropbox(token)
	file_temp = tempfile.NamedTemporaryFile(suffix=".json")
	dbx.files_download_to_file("DatosJson.json","/practica/DatosJson.json")
					
	with io.open('DatosJson.json',encoding='utf8') as f:
		data = json.load(f)
				
	data=json.dumps(data)
	s = data.replace(',','<br>')
	s = rep(s)
	return s
	#reemplaza caracteres que no queremos mostrar. Esta al estilo compare, porque el utf-8 no nos funciona bien,
	# hemos probado con encoding, encode, etc. y hemos terminado haciendo un apaño gitano
def rep(s):
	s = s.replace("<HtmlResponse 200 ","")
	s = s.replace(r'>"}',"")
	s = s.replace('descripcion_ofr','Descripcion de la oferta')
	s = s.replace('salario_ofr','Salario de la oferta')
	s = s.replace('localidadn_ofr','Localidad de la oferta')
	s = s.replace('fechaIni_ofr','Fecha de inicio de la oferta')
	s = s.replace('duracion_ofr','Duracion de la oferta')
	s = s.replace('enlace_ofr','Enlace de la oferta')
	s = s.replace('{','<p>')
	s = s.replace('}','</p>')
	s = s.replace('"',' ')
	s = s.replace("["," ")
	s = s.replace("]"," ")
	s = s.replace(r'\r\n',r"<br>")
	s = s.replace(r'\u00f3','ó')
	s = s.replace(r'\u00fa','ú')
	s = s.replace(r'\u00e1','á')
	s = s.replace(r'\u00e9','é')
	s = s.replace(r'\u00ed','í')
	s = s.replace(r'\u00f1','ñ')
	s = s.replace(r'\u00bf','¿')
	
	return s
	
run(host='localhost',port=8080,debug=True)


