from server.model import Lectures
from server.db_connector import DBConnector

db = DBConnector()

def lecture_test():
    sql = "SELECT * FROM lectures"
    
    lecture_list = db.executeAll(sql)
    
    lectures = [Lectures(row).get_data_object() for row in lecture_list]
    
    return{
        'lectures' : lectures
    }