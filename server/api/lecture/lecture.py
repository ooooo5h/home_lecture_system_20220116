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
    
# 수강신청 기능
def apply_lecture(params):
    
    sql = f"SELECT * FROM lecture_user WHERE user_id ={params['user_id']} AND lecture_id = {params['lecture_id']}"
    
    already_apply = db.executeOne(sql)
    
    if already_apply:
        return{
            'code' : 400,
            'mesasge' : '이미 수강신청 완료',
        }, 400
    
    sql = f"INSERT INTO lecture_user VALUES ({params['lecture_id']}, {params['user_id']})"
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '수강 신청 완료'
    }
    
# 수강 취소
def cancel_apply(params):
    
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    already_apply = db.executeOne(sql)
    
    if already_apply is None:
        return{
            'code' : 400,
            'message' : '신청 부터 하세요'
        }, 400
        
    sql = f"DELETE FROM lecture_user WHERE lecture_id={params['lecture_id']} AND user_id = {params['user_id']}"
    
    db.cursor.execute(sql)
    db.db.commit()
    
    return{
        'code' : 200,
        'message' : '수강취소 성공'
    }
    
# 특정 강의 상세보기
def view_lecture_detail(id, params):
    
    sql = f"SELECT * FROM lectures WHERE id = {id}"
    
    lecture_data = db.executeOne(sql)
    lecture = Lectures(lecture_data)
    
    return{
        'code' : 200,
        'message' : '강의 상세 조회',
        'data' : {
            'lecture' : lecture.get_data_object()
        }
    }