import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Cambia esto si tu servidor está en otro host
            user="root",  # Cambia por tu usuario de MySQL
            password="123456",  # Cambia por tu contraseña de MySQL
            database="tablas"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
