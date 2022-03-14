
'''
crear películas

ejecutar:

python manage.py shell < datos/crear_peliculas.py
'''

from centros.models import Centro
import json
import os

# borrar centros
for p in Centro.objects.all():
    p.delete()

#lista de centros del json
if os.path.exists("datos/Centros.json"):
    pelis = json.load(open("datos/Centros.json"))
else:
    pelis = json.load(open("Centros.json"))


for p1 in pelis:
    p = Centro()
    p.id = p1["objectid"]
    p.nombre = p1["nombreCentro"]
    p.tipo = p1["tipoCentro"]
    p.nat = p1["naturaleza"]
    p.loc = p1["localidad"]
    p.dir = p1["direccion"]
    p.postal = p1["codPostal"]
    p.long = p1["long"]
    p.lat = p1["lat"]
    p.save()