import sys
import os
import hashlib
from database.connBD import connectDB
from models.Teacher import Teacher
from models.Student import Student

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class LoginController:
    def __init__(self):
        pass

    # def hash_password(self, password):
    #     """Hash the password using SHA256 for security."""
    #     return hashlib.sha256(password.encode()).hexdigest()

    def login(self, email, passw):
        conn = None
        cursor = None
        try:
            conn = connectDB()
            if conn is None:
                print("Không thể kết nối database.")
                return False, None, None

            cursor = conn.cursor()

            # Kiểm tra giảng viên
            cursor.execute(
                "SELECT ma_gv, ten_gv, Ngaysinh, sdt, password, email, khoa FROM giang_vien WHERE email = %s AND password = %s",
                (email, passw)
            )
            result = cursor.fetchone()
            if result:
                teacher = Teacher(*result)
                return True, "teacher", teacher

            # Kiểm tra sinh viên
            cursor.execute(
                "SELECT Ma_sv, Ten_sv, Ngay_sinh, Sdt, password, Email, Nien_khoa, Lop_sinh_hoat, Chuyen_nganh, khoacn FROM sinh_vien WHERE Email = %s AND password = %s",
                (email, passw)
            )
            result = cursor.fetchone()
            print("Result:", result)
            if result:
                student = Student(*result)
                return True, "student", student

            print("Email hoặc mật khẩu không đúng.")
            return False, None, None

        except Exception as e:
            print("Lỗi khi đăng nhập:", e)
            return False, None, None

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
