from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import mongo

class User(UserMixin):
    def __init__(self, id, password_hash, name, type):
        self.id = id
        self.password_hash = password_hash
        self.name = name
        self.type = type

    @staticmethod
    def get(id):
        user = mongo.db.users.find_one({'id': id})
        if user:
            return User(
                user['id'],
                user['password_hash'],
                user['name'],
                user['type']
            )
        else:
            return None

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        update = {
            '$set': {
                'id': self.id,
                'password_hash': self.password_hash,
                'name': self.name,
                'type': self.type,
            },
        }

        mongo.db.users.find_one_and_update({'id': self.id}, update, upsert=True)

    @staticmethod
    def generate_password_hash(password, method='pbkdf2:sha512:20000'):
        return generate_password_hash(password, method=method)