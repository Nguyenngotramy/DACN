import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import connectDB

class LoginController:
    def __init__(self):
        pass  # chỗ để bạn mở rộng sau này

    def login(self, email, passw):
        conn = None
        cursor = None
        try:
            conn = connectDB.connectDB()  # gọi connectDB() trong module connectDB.py
            if conn is None:
                print("Không thể kết nối database.")
                return False, None

            cursor = conn.cursor()

            user_tables = ['giang_vien', 'sinh_vien']

            for table in user_tables:
                sql = f"SELECT email, password FROM {table} WHERE email = %s AND password = %s"
                cursor.execute(sql, (email, passw))
                user = cursor.fetchone()

                if user:
                    print(f"Đăng nhập thành công ({table}): {email}")
                    return True, table

            print("Email hoặc mật khẩu không đúng.")
            return False, None

        except Exception as e:
            print("Lỗi khi đăng nhập:", e)
            return False, None

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
