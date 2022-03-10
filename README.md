# Wagtail

## Descripción
Web de datos realizada con Wagtail. En ella podemos ver el listado de las 250 mejores películas (extraidas de la web de IMDb: https://www.imdb.com/chart/top/), un listado de diferentes modelos de coches.


¿Cómo lo instalo y hago funcionar?
### Windows
(ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo y Python, para que el cmd reconozca los comandos correspondientes.

1. Nos posicionamos donde queramos tener la capeta en el cmd (con cd).
2. Copiamos el enlace del repositorio git donde está el trabajo.
3. En el cmd escribimos: git clone https://github.com/Rares7/Wagtail.git
4. Nos posicionamos dentro del proyecto.
5. Creamos el entorno virtual (py -m venv env).
6. Activamos el entorno virtual (env\Scripts\activate.bat).
7. Instalamos los requisitos (pip install -r requirements.txt).
8. Dentro del entorno: py manage.py runserver
9. En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000).
10. Cuando queramos pararlo: Ctrl + c (en el cmd).

