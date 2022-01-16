from server.db_connector import DBConnector

db = DBConnector()

def test():

    sql = "SELECT * FROM users"
    db.cursor.execute(sql)
    all_list = db.cursor.fetchall()
    
    print(all_list)
    
    return {
        '임시' : '테스트'
    }