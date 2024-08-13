from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(20), nullable=False)
    service_name = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    message = db.Column(db.String(200), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/logs', methods=['POST'])
def recibir_log():
    token = request.headers.get('Authorization')
    if not es_token_valido(token):
        return jsonify({'error': 'Token no válido'}), 403
    
    data = request.json
    nuevo_log = Log(
        timestamp=data['timestamp'],
        service_name=data['service_name'],
        severity=data['severity'],
        message=data['message']
    )
    db.session.add(nuevo_log)
    db.session.commit()
    return jsonify({'mensaje': 'Log recibido'}), 200

def es_token_valido(token):
    tokens_validos = ['token_service1', 'token_service2', 'token_service3']
    return token in tokens_validos

if __name__ == '__main__':
    app.run(port=5000)
