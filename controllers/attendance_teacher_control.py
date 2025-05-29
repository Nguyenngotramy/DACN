import mysql.connector
from datetime import datetime
from database.connBD import connectDB

class AttendanceController:
    def __init__(self):
        self.connection = connectDB()
        if self.connection:
            print("Đã kết nối CSDL trong AttendanceController.")
        else:
            print("Không thể kết nối tới CSDL.")

    def check_in(self, id_hoc_phan: int) -> bool:
        try:
            cursor = self.connection.cursor()

            sql = """
            UPDATE diem_danh_faceid.buoi_diem_danh
            SET 
                gio_bat_dau = CURRENT_TIME,
                cho_phep_diem_danh = TRUE
            WHERE 
                id_hoc_phan = %s
                AND ngay_hoc = CURRENT_DATE;
            """

            cursor.execute(sql, (id_hoc_phan,))
            self.connection.commit()

            print(f"Check-in thành công cho học phần ID: {id_hoc_phan}")
            return True
        except mysql.connector.Error as err:
            print(f"Lỗi khi check-in: {err}")
            return False
        finally:
            cursor.close()
