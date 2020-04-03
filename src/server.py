from flask import Flask
from controllers import teste
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = Flask(__name__)
app.secret_key = getenv('APP_SECRET_KEY')
app.register_blueprint(teste.controller)
