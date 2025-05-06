import mysql.connector
from mysql.connector import errorcode

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="diem_danh_faceid"
            )
            print("Connect succeeded!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
def connectDB():
    db = DatabaseConnection()
    db.connect()
    return db.connection