from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import mysql.connector
import os


aplication = Flask(__name__)

aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
aplication.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CostadoMarfimrx8*10@localhost:3306/info_dados_db'


aplication.config['SECRET_KEY'] = 'secret'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload') # constante do endereço para armazenar a imagem


login_manager = LoginManager(aplication)
db = SQLAlchemy(aplication)

# Initialize Flask-Limiter for rate limiting
limiter = Limiter(
    app=aplication,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Initialize Flask-Talisman for security headers and CSP
talisman = Talisman(
    aplication,
    force_https=False,  # Set to True in production with HTTPS
    strict_transport_security=True,
    strict_transport_security_preload=True,
    strict_transport_security_max_age=31536000,  # 1 year
    frame_options='DENY',
    content_security_policy={
        'default-src': "'self'",
        'script-src': [
            "'self'",
            'https://cdn.jsdelivr.net',
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/',
            'https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/'
        ],
        'style-src': [
            "'self'",
            'https://cdn.jsdelivr.net',
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/'
        ],
        'img-src': [
            "'self'",
            'data:'
        ],
        'font-src': [
            "'self'",
            'https://cdn.jsdelivr.net'
        ]
    }
)

# Custom 429 error handler for rate limiting
@aplication.errorhandler(429)
def ratelimit_handler(e):
    return "Rate limit exceeded. Too many requests. Please try again later.", 429
