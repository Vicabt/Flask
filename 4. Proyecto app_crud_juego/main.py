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

#Ruta:eliminar_juego
@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_juegos.eliminar_juego(request.form["id"])
    return redirect("/juegos")

#Ruta: Formulario_editar_juego
@app.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    #Obtener el juego por ID
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

#Ruta:actualizar _juego
@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juegos")

# Iniciar el servidor para ejecutar la aplicacion flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)