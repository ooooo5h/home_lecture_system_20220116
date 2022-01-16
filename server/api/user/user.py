from server.model.users import Users
from server import db

def login(params):
    sql = f"SELECT * FROM users WHERE email = '{params['email']}' AND password = '{params['password']}'"
    
    login_user = db.executeOne(sql)
    
    if login_user == None:
        return{
            'code' : 400,
            'message' : '이메일 or 비밀번호 잘못됨'
        }
    
    return{
        'code' : 200,
        'message' : '로그인 성공',
        'user' : Users(login_user).get_data_object()
    }
    
def sign_up(params):
       
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    already_user_data = db.executeOne(sql)
    
    if already_user_data:
        return {
            'code' : 400,
            'message' : '이미 가입된 이메일'
        }
    
       
    sql = f"INSERT INTO users (email, password, name) VALUES ('{params['email']}','{params['password']}','{params['name']}')"
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '회원가입 성공'
    }
    
# 이메일을 받아서 사용자 정보 조회하는 기능 추가
def find_user_by_email(params):
    
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    find_user_data = db.executeOne(sql)
    
    if find_user_data :
        find_user = Users(find_user_data)
        return {
            'code' : 200,
            'message' : '사용자 찾음',
            'data' : {
                'user' : find_user.get_data_object()
            }
        }
    else :       
        return{
            'code' : 400,
            'message' : '없음'
        }, 400