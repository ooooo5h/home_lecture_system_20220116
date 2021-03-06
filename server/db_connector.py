import pymysql
from pymysql.cursors import DictCursor

class DBConnector:
    
    def __init__(self):
        self.db = pymysql.connect(
            host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            passwd='Vmfhwprxm!123',
            db='test_202112_python',
            charset='utf8',
            cursorclass=DictCursor
        )
        
        self.cursor = self.db.cursor()
        
    # 쿼리를 실행하고 목록을 리턴하는 메쏘드 추가
    def executeAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def executeOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    # 하나의 데이터를 추가/변경/삭제하고 DB에 실제 기록하는 메쏘드 추가
    def executeQueryAndCommit(self, sql):
        self.cursor.execute(sql)
        self.db.commit()