from server.db_connector import DBConnector
from server.model.users import Users

db = DBConnector()

def test():

    sql = "SELECT * FROM users"
    db.cursor.execute(sql)
    all_list = db.cursor.fetchall()
    
    all_users = [Users(row).get_data_object() for row in all_list]
    
    return {
        'users' : all_users
    }