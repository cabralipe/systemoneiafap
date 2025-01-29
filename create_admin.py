from app import db
from models import Usuario
from werkzeug.security import generate_password_hash

# Criando um Administrador Padrão
admin = Usuario(
    nome="Administrador",
    cpf="000.000.000-00",  # Certifique-se de colocar um CPF válido
    email="admin@exemplo.com",
    senha=generate_password_hash("123456", method='pbkdf2:sha256'),
    formacao="Gestão",
    tipo="admin"
)

# Adicionando ao banco de dados
db.session.add(admin)
db.session.commit()

print("Administrador criado com sucesso!")
