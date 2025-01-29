import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
import os

class Config:
    SECRET_KEY = os.urandom(24)  # Gera uma chave aleatória
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

