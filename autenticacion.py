from conexionbd import get_db_connection

class Auth:
    def __init__(self):
        self.conn = get_db_connection()

    def autenticar(self, username, password):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

    def autorizar(self, usuario):
        if usuario["es_admin"]:
            return "Bienvenido administrador. Aquí está la lista de todos los perros de la guardería."
        else:
            return f"Hola {usuario['username']}, bienvenido a la guardería."
        
        
