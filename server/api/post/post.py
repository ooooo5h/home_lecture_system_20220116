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
    
    sql = f"SELECT * FROM posts WHERE id = {post_id}"
    
    post_data = db.executeOne(sql)
        
    return{
        'code' : 200,
        'message' : '특정 게시글 상세 조회',
        'data' : {
            'post' : Posts(post_data).get_data_object()
        }
    }
    
def add_post(params):
    
    sql = f"INSERT INTO posts (user_id, title, content) VALUES ({params['user_id']}, '{params['title']}', '{params['content']}')"
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '게시글 등록'
    }
    
def modify_post(params):
    return{
    '임시' : '게시글 수정'
}
        
def delete_post(params):
    return{
        '임시' : '게시글 삭제'
    }