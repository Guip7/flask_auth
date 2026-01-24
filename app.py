from flask import Flask, request, jsonify
from database import db
from login import *
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login' # rota de login origin

# carregar sessão do usuario, e retornar o Id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:

        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            # autenticar usuario
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message": "Usuario ou senha invalido"}), 401

@app.route('/logout', methods=['GET'])
@login_required # Verifica se o usuario ja foi autenticado
def logout():
    logout_user() # Os cookies são limpados do servidor
    return jsonify({"message": "Usuario desconectado"})


    return "Hello World"

@app.route('/user', methods=['POST'])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Adicionando novo usuario no meu banco
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso"})

    return jsonify({"message": "Credencias invalidas"}), 401

@app.route('/user/<int:id>', methods=['GET'])
@login_required
def read_user(id):
    user = User.query.get(id) # Achar o usuario pelo numero de Id
    if user:
        return jsonify({"username": user.username})

    return jsonify({"message": "Usuario nao encontrado"}), 404

@app.route('/user/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    data = request.json
    user = User.query.get(id) # Achar o usuario pelo numero de Id
    
    if user.username and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"username": f"Usuario {id} atualizado com sucesso"})

    return jsonify({"message": "Usuario nao encontrado"}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)

    if id == current_user.id: # Usuario autorizado não pode se auto deletar
        return jsonify({"message": "Não autorizado"}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuario {id} deletado com sucesso"})
    
    return jsonify({"message": "Usuario nao encontrado"}), 404
    
    

@app.route('/hello-world', methods=['GET'])
def hello_world():
    pass

if __name__ == '__main__':
    app.run(debug=True)