# 플라스크 자체를 로딩
from flask import Flask, request
from server.db_connector import DBConnector


db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lectures, apply_lecture, cancel_apply, write_review, view_lecture_detail
    
    @app.post("/user")
    def user_post():
        return login(request.form.to_dict())
    
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    @app.get("/lecture")
    def lecture_get():
        return get_all_lectures(request.args.to_dict())
    
    @app.get("/lecture/<lecture_id>")
    def lecture_detail(lecture_id):
        return view_lecture_detail(lecture_id, request.args.to_dict())
    
    @app.post("/lecture")
    def lecture_post():
        return apply_lecture(request.form.to_dict())
    
    @app.delete("/lecture")
    def lecture_delete():
        return cancel_apply(request.args.to_dict())
    
    @app.post("/lecture/review")
    def review_post():
        return write_review(request.form.to_dict())
    
    
    return app