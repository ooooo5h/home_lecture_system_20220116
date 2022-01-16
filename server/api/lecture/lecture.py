from server.model import Lectures
from server import db

def get_all_lectures(params):
    
    sql = f"SELECT * FROM lectures ORDER BY name"
    
    db_list = db.executeAll(sql)
    
    lectures = [Lectures(row).get_data_object() for row in db_list]
        
    return {
        'code' : 200,
        'message' : '수강 목록 성공',
        'data' : {
            'lectures' : lectures,
        }
    }