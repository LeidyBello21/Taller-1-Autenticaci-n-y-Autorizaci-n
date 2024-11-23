from autenticacion import Auth

# Inicializar sistema de autenticación
auth_system = Auth()

# Simulación de inicio de sesión
print("Bienvenido al sistema de la guardería")
username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

usuario_autenticado = auth_system.autenticar(username, password)
if usuario_autenticado:
    print("Autenticación exitosa.")
    mensaje = auth_system.autorizar(usuario_autenticado)
    print(mensaje)
else:
    print("Credenciales incorrectas. Inténtelo nuevamente.")
