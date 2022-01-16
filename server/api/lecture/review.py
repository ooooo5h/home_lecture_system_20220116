from server import db

def write_review(params):
    
    score = float(params['score'])
    
    if not (1<=score<=5):
        return{
            'code' : 400,
            'message' : '평점은 1 ~ 5 사이로 입력해라'
        }, 400
    
    if len(params['title']) < 5:
        return{
            'code' : 400,
            'meesage' : '제목 최소 5자 이상'
        }, 400
    
    if len(params['content']) < 10:
        return{
        'code' : 400,
        'meesage' : '내용 최소 10자 이상'
    }, 400
    
    sql = f"SELECT * FROM lecture_user WHERE user_id = {params['user_id']} AND lecture_id = {params['lecture_id']}"
    
    query_result = db.executeOne(sql)
    if query_result is None:
        return{
            'code' : 400,
            'message' : '수강 해야지만 리뷰 작성 가능'
        }, 400
    
    sql = f"INSERT INTO lecture_review (lecture_id, user_id, title, content, score) VALUES ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {score})"
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '리뷰작성 완료'
    }