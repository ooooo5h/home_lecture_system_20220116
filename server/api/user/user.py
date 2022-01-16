from server.db_connector import DBConnector
from server.model.users import Users

db = DBConnector()

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
    