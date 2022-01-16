from server import db

def get_all_posts(params):
    return{
        '임시' : '모든 게시글 조회'
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