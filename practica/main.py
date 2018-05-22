from tasks import subirADropbox, ejecutarSpider, interfazWeb
import celery
from celery import chain
from celery.schedules import crontab, timedelta
import tempfile
"""
app.conf.beat_schedule = {
    "every-day":{
        "task": "subir",
        "schedule": timedelta(minutes = 30),
         "args": (),
       },
    }
app.conf.timezone = "Europe/Madrid"
"""
#estabamos haciendo la practica en windows y no funciona el comando -B de celery
#encadena la ejecución de los métodos de tasks

test = chain(ejecutarSpider(),subirADropbox(), interfazWeb())
print('Tarea realizada exitosamente.')

