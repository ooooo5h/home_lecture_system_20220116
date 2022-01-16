# 플라스크 자체를 로딩
from flask import Flask, request
from server.db_connector import DBConnector


db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lectures
    
    @app.post("/user")
    def user_post():
        return login(request.form.to_dict())
    
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    @app.post("/lecture")
    def lecture_post():
        return get_all_lectures()
    
    return app