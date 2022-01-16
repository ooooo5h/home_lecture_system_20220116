from server import db
from server.model import Posts

def get_all_posts(params):
    
    sql = f"SELECT * FROM posts ORDER BY created_at DESC"
    
    post_data_list = db.executeAll(sql)
    
    posts = [Posts(row).get_data_object() for row in post_data_list]
    
    return{
        'code' : 200,
        'message' : '모든 게시글 가져오기',
        'data' : {
            'posts' : posts,
        }
    }
    
# 특정 게시글 상세 조회 -/post/5
def view_post(post_id, params):
    return{
        '임시' : '특정 게시글 상세 조회'
    }
    
def add_post(params):
    return{
        '임시' : '게시글 등록'
    }
    
def modify_post(params):
    return{
    '임시' : '게시글 수정'
}
        
def delete_post(params):
    return{
        '임시' : '게시글 삭제'
    }