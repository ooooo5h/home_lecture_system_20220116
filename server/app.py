# 플라스크 자체를 로딩
from flask import Flask
from server.db_connector import DBConnector
from .api.user import test
from .api.lecture import lecture_test

# db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    @app.post("/user")
    def user_post():
        pass
    
    @app.post("/lecture")
    def lecture_post():
        return lecture_test()
    
    return app