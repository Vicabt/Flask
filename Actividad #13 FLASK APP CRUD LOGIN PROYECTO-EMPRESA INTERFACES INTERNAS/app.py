import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


# Crear la aplicación Flask
app = Flask(__name__, template_folder='templates')
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave secreta real

# Configuración de la aplicación
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/DB_vcbikes'

# Desactiva el rastreo de modificaciones
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#se usa para inicializar SQLAlchemy en una aplicacion Flask


# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Aquí podrías agregar lógica para enviar el mensaje por correo electrónico o guardarlo en una base de datos
        
        flash('Mensaje enviado con éxito. Nos pondremos en contacto contigo pronto.')
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticación
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simulación de autenticación
        if username == "admin" and password == "password":  # Cambia esto por tu lógica real
            return redirect(url_for('dashboard'))  # Redirige a la página de dashboard
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.')
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Lógica de registro
        pass
    return render_template('registro.html')

@app.route('/recuperar-password', methods=['GET', 'POST'])
def recuperar_password():
    if request.method == 'POST':
        # Lógica de recuperación de contraseña
        pass
    return render_template('recuperacion.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        # Lógica para manejar el formulario de categorías
        pass
    return render_template('categorias.html')

@app.route('/subcategorias', methods=['GET', 'POST'])
def subcategorias():
    if request.method == 'POST':
        # Lógica para manejar el formulario de subcategorías
        pass
    return render_template('subcategorias.html')

@app.route('/configuracion_usuario')
def configuracion_usuario():
    return render_template('configuracion_usuario.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
    if request.method == 'POST':
        # Lógica para manejar el formulario de proveedores
        provider_name = request.form.get('provider_name')
        provider_contact = request.form.get('provider_contact')
        provider_email = request.form.get('provider_email')
        provider_phone = request.form.get('provider_phone')
        provider_description = request.form.get('provider_description')
        provider_address = request.form.get('provider_address')
        
        # Aquí podrías agregar lógica para guardar el proveedor en una base de datos
        
        flash('Proveedor agregado con éxito.')
        return redirect(url_for('proveedores'))
    
    return render_template('proveedores.html')

if __name__ == '__main__':
    app.run(debug=True)