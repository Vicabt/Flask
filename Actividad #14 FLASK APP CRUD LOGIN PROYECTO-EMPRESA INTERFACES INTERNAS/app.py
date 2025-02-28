import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session

# Crear la aplicación Flask
app = Flask(__name__, template_folder='templates')
app.secret_key = 'tu_clave_secreta_123'  # Cambiado por una clave más segura

# Usuario de prueba (en producción usar base de datos)
USERS = {
    "admin": {
        "password": "admin123",
        "name": "Administrador"
    }
}

# Decorator para requerir login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor inicia sesión para acceder.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

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
        flash('Mensaje enviado con éxito. Nos pondremos en contacto contigo pronto.')
        return redirect(url_for('contacto'))
    return render_template('contacto.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username]["password"] == password:
            session['user_id'] = username
            session['user_name'] = USERS[username]["name"]
            flash('Has iniciado sesión exitosamente!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión exitosamente', 'success')
    return redirect(url_for('login'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/recuperar-password', methods=['GET', 'POST'])
def recuperar_password():
    return render_template('recuperacion.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/categorias', methods=['GET', 'POST'])
@login_required
def categorias():
    return render_template('categorias.html')

@app.route('/subcategorias', methods=['GET', 'POST'])
@login_required
def subcategorias():
    return render_template('subcategorias.html')

@app.route('/configuracion_usuario')
@login_required
def configuracion_usuario():
    return render_template('configuracion_usuario.html')

@app.route('/empleados')
@login_required
def empleados():
    return render_template('empleados.html')

@app.route('/clientes')
@login_required
def clientes():
    return render_template('clientes.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/ventas')
@login_required
def ventas():
    return render_template('ventas.html')

@app.route('/productos')
@login_required
def productos():
    return render_template('productos.html')

@app.route('/proveedores', methods=['GET', 'POST'])
@login_required
def proveedores():
    return render_template('proveedores.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


if __name__ == '__main__':
    app.run(debug=True)