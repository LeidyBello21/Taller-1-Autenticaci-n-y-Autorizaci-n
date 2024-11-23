from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import Usuario, Guarderia  # Tu modelo de Usuario y lógica para Guarderías
from conexionbd import get_db_connection

app = Flask(__name__)
app.secret_key = 'tu_secreto_aqui'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

@app.route('/')
def index():
    # Redirige automáticamente al login
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.get_by_username(username)
        if user and user.password == password:  # Valida la contraseña
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.es_admin:
        # Renderiza el dashboard del administrador
        guarderias = Guarderia.obtener_guarderias()
        return render_template('admin_dashboard.html', guarderias=guarderias)
    else:
        # Renderiza el dashboard del usuario común
        return render_template('user_dashboard.html', username=current_user.username)



if __name__ == '__main__':
    app.run(debug=True)
