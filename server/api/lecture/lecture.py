import sqlite3
from server.db_connector import DBConnector

db = DBConnector()

def lecture_test():
    sql = "SELECT * FROM lectures"
    
    db.cursor.execute(sql)
    lecture_list = db.cursor.fetchall()
    
    print(lecture_list)
    
    return{
        '강의 임시' : '강의 테스트'
    }