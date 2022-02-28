from peliculas.models import Coche
import json
import os

# borrar coches
for p in Coche.objects.all():
    p.delete()

#lista de coches del json
if os.path.exists("datos/listacoches.json"):
    car = json.load(open("datos/listacoches.json"))
else:
    car = json.load(open("listacoches.json"))


for p1 in car:
    p = Coche()
    p.iden = p1["iden"]
    p.marca = p1["marca"]
    p.modelo = p1["modelo"]
    p.save()