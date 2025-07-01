from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import mysql.connector
import os


aplication = Flask(__name__)
Talisman(application, content_security_policy=None)

limiter = Limiter(
    get_remote_address,
    app=aplication,
    default_limits=[]
)
csp = {
    'default-src': [
        '\'self\''
    ],
    'script-src': [
        '\'self\'', 
        'https://cdn.jsdelivr.net', 
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js'
    ],
    'style-src': [
        '\'self\'', 
        'https://cdn.jsdelivr.net', 
        'https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css'
    ],
    'img-src': [
        '\'self\'', 
        'data:', 
        'https://cdn.jsdelivr.net'
    ]
}

aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
aplication.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CostadoMarfimrx8*10@localhost:3306/info_dados_db'


aplication.config['SECRET_KEY'] = 'secret'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload') # constante do endereço para armazenar a imagem


login_manager = LoginManager(aplication)
db = SQLAlchemy(aplication)
