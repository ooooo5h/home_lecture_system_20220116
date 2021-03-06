# 플라스크 자체를 로딩
from operator import mod
from flask import Flask, request
from server.db_connector import DBConnector


db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lectures, apply_lecture, cancel_apply, write_review, view_lecture_detail, modify_review
    from .api.post import view_post,get_all_posts,add_post,modify_post,delete_post
    
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
    
    @app.patch("/lecture/review")
    def review_patch():
        return modify_review(request.form.to_dict())
    
    @app.get("/post")
    def post_get():
        return get_all_posts(request.args.to_dict())
    
    @app.get("/post/<post_id>")
    def post_get_detail(post_id):
        return view_lecture_detail(post_id, request.args.to_dict())
    
    @app.post("/post")
    def post_post():
        return add_post(request.form.to_dict())
    
    @app.put("/post")
    def post_put():
        return modify_post(request.form.to_dict())
    
    @app.delete("/post")
    def post_delete():
        return delete_post(request.args.to_dict())
    
    return app