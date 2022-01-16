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
        
        
    sql = f"SELECT * FROM lecture_review WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    already_review_data = db.executeOne(sql)
    if already_review_data:
        return{
            'code' : 400,
            'message' : '이미 리뷰를 등록했자나'
        }, 400
    
    
    sql = f"INSERT INTO lecture_review (lecture_id, user_id, title, content, score) VALUES ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {score})"
    
    db.executeQueryAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '리뷰작성 완료'
    }
    
def modify_review(params):
    
    column_name = params['field']
    
    sql = f"SELECT * FROM lecture_review WHERE id={params['review_id']}"
    
    review_data = db.executeOne(sql)
    
    if review_data == None:
        return{
            'code' : 400,
            'message' : '해당 리뷰는 존재하지 않음'
        }, 400
    
    # DB에서 가져온 user_id는 int로 받아옴 / 파라미터에서 가져온 user_id는 str로 받아옴
    if int(review_data['user_id']) != int(params['user_id']):
        return{
            'code' : 400,
            'message' : '니가쓴거만 수정해'
        }, 400
    
    if column_name == 'title':
        sql = f"UPDATE lecture_review SET title='{params['value']}' WHERE id = {params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return{
            'code' : 200,
            'message' : '제목 수정 완료'
        }
        
        
    if column_name == 'content':
        sql = f"UPDATE lecture_review SET content = '{params['value']}' WHERE id = {params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return{
            'code' : 200,
            'message' : '내용 수정 완료'
        }  
        
    
    if column_name == 'score':
        
        score = float(params['value'])
        
        if not (1<=score<=5):
            return{
                'code' : 400,
                'message' : '점수는 1 ~5 사이만 입력가능합니다.'
            }, 400
        
        sql = f"UPDATE lecture_review SET score = {params['value']} WHERE id ={params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return{
            'code' : 200,
            'message' : '점수 수정 완료'
        }  
        
    
    return{
        'code' : 400,
        'message' : '필드에 잘못된 값 입력했음'
    }, 400