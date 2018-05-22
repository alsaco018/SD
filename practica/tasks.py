from celery import Celery, task
from celery.schedules import crontab, timedelta
import dropbox
import tempfile
import subprocess, shlex


app=Celery("tarea",backend="rpc://", broker="pyamqp://guest@localhost//")

@app.task(name = "subir")

#este metodo ejecuta en linea de comando el spider y guarda los archivos json (que se crea mediante el pipeline) y csv en la carpeta Datos
def ejecutarSpider():
    command_line = 'scrapy crawl ofertas -t csv -o Datos/ofertas_items.csv'
    args = shlex.split(command_line)
    subprocess.call(args)

#este método sube a dropbox los archivos json y csv 
def subirADropbox():
    token = "Yr8Bgt_dfoAAAAAAAAAAE_DXzlI_-u0m7h_a3BOxz31MlvBINCIk9_rxwmTFmkbm"
    dbx = dropbox.Dropbox(token)
    user = dbx.users_get_current_account()

    with open("Datos/ofertas_items.json", "rb") as f2:
        print("Subiendo archivo json...\n")
        dbx.files_upload(f2.read(),'/practica/DatosJson.json', mode=dropbox.files.WriteMode("overwrite"), mute=True)
        print("Archivo subido exitosamente...")

    with open("Datos/ofertas_items.csv", "rb") as f2:
        print("Subiendo archivo csv...\n")
        dbx.files_upload(f2.read(),'/practica/DatosExcel.csv', mode=dropbox.files.WriteMode("overwrite"), mute=True)
        print("Archivo subido exitosamente...")

#este método ejecuta mediante linea de comandos el archivo de bottle, para que al abrir la direccion
# http://localhost:8080/practicas se nos muestre en una interfaz web los datos de las ofertas que cumplen 
# los requistos especificados
def interfazWeb():
    command_line = 'py json-to-html.py'
    args = shlex.split(command_line)
    subprocess.call(args)

