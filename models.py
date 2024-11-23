from flask_login import UserMixin
from conexionbd import get_db_connection

class Usuario(UserMixin):
    def __init__(self, id, username, es_admin, password=None):
        self.id = id
        self.username = username
        self.es_admin = es_admin
        self.password = password  # Nuevo atributo para almacenar la contraseña

    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            return Usuario(
                id=user_data["id"],
                username=user_data["username"],
                es_admin=user_data["es_admin"],
                password=user_data["password"]
            )
        return None

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            return Usuario(
                id=user_data["id"],
                username=user_data["username"],
                es_admin=user_data["es_admin"],
                password=user_data["password"]
            )
        return None


class Guarderia:
    @staticmethod
    def obtener_guarderias():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM tablas.guarderias"
        cursor.execute(query)
        guarderias = cursor.fetchall()
        cursor.close()
        conn.close()
        return guarderias

