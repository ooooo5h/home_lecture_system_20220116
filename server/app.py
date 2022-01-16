# 플라스크 자체를 로딩
from flask import Flask, request
from server.db_connector import DBConnector
from .api.user import login, sign_up
from .api.lecture import lecture_test

# db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    @app.post("/user")
    def user_post():
        return login(request.form.to_dict())
    
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    @app.post("/lecture")
    def lecture_post():
        return lecture_test()
    
    return app