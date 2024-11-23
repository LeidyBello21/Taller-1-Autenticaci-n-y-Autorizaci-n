class Usuario:
    def __init__(self, user_id, username, password, es_admin=False):
        self.id = user_id
        self.username = username
        self.password = password
        self.es_admin = es_admin

    def __repr__(self):
        return f"Usuario(id={self.id}, username={self.username}, es_admin={self.es_admin})"
