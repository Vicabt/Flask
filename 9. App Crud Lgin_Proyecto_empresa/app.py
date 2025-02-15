import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Crear la aplicación Flask
app = Flask(__name__, template_folder='template')
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para flash messages

# Rutas
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí irá la lógica de autenticación
        flash('Funcionalidad de login en desarrollo')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Aquí irá la lógica de registro
        flash('Funcionalidad de registro en desarrollo')
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/recuperar-password', methods=['GET', 'POST'])
def recuperar_password():
    if request.method == 'POST':
        # Aquí irá la lógica de recuperación
        flash('Funcionalidad de recuperación en desarrollo')
        return redirect(url_for('login'))
    return render_template('recuperacion.html')

if __name__ == '__main__':
    app.run(debug=True) 