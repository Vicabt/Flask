'''
CRUD FLASK PYTHON + MYSQL
Desarrollado por: Victor Cabas
'''
#Realizamos la importacion de las librerias flask requeridas
from flask import Flask, render_template, request, redirect, flash
#Importamos el controlador
import controlador_juegos

#Iniciamos creando una aplicacion flask
app = Flask(__name__)

#Ruta /ruta principal /juego lista de juegos
@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)


#Ruta:agregar_juego
@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")

#Ruta:guardar_juego
@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    #recibe los datos del formulario
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    #Guarda los datos en la base de datos ingresando a la funcion inserta_juego del controlador
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    # De cualquier modo y su todo fue bien redireccionar
    return redirect("/juegos")

# Iniciar el servidor para ejecutar la aplicacion flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)