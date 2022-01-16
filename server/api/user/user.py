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