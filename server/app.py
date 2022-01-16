# 플라스크 자체를 로딩
from flask import Flask
from server.db_connector import DBConnector

db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    return app