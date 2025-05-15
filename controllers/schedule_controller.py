# controllers/schedule_controller.py

from database.connBD import connectDB
from models.schedule_item import ScheduleItem

class ScheduleController:
    def __init__(self):
        self.connection = connectDB()
        if self.connection:
            print("Đã kết nối CSDL trong controller.")
        else:
            print("Không thể kết nối tới CSDL.")

    def get_today_schedule(self, student_id):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.ten_hoc_phan,
                    gv.ten_gv,
                    tkb.tuan_hoc,
                    tkb.phong,
                    CONCAT('Thứ ', tkb.thu, ' / Tiết ', tkb.tiet_bat_dau, '-', tkb.tiet_bat_dau + tkb.so_tiet - 1),
                    CONCAT('Tiết ', tkb.tiet_bat_dau, '-', tkb.tiet_bat_dau + tkb.so_tiet - 1, ' tại ', tkb.phong)
                FROM 
                    sinh_vien_hoc_phan svhp
                JOIN sinh_vien sv ON svhp.id_sv = sv.id_sv
                JOIN hoc_phan hp ON svhp.id_hoc_phan = hp.id_hoc_phan
                JOIN giang_vien gv ON hp.id_gv = gv.id_gv
                JOIN thoi_khoa_bieu tkb ON hp.id_hoc_phan = tkb.id_hoc_phan
                WHERE 
                    sv.ma_sv = %s
                    AND tkb.thu = DAYOFWEEK(CURDATE())
                ORDER BY tkb.tiet_bat_dau;
            """
            print(f"Đang thực hiện truy vấn thời khóa biểu cho sinh viên mã = {student_id}")
            cursor.execute(query, (student_id,))
            results = cursor.fetchall()

            print("Kết quả truy vấn thời khóa biểu hôm nay:")
            if not results:
                print("Không có dữ liệu thời khóa biểu cho hôm nay.")
            for i, row in enumerate(results, start=1):
                print(f"{i}. {row}")

            schedule_items = []
            for row in results:
                item = ScheduleItem(*row)
                print("Đối tượng ScheduleItem tạo ra:", item.__dict__)
                schedule_items.append(item)

            return schedule_items

        except Exception as e:
            print("Lỗi khi truy vấn thời khóa biểu hôm nay:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def get_all_schedule(self, student_id):
        """Truy vấn toàn bộ thời khóa biểu (không giới hạn ngày) của sinh viên."""
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.ten_hoc_phan,
                    gv.ten_gv,
                    tkb.tuan_hoc,
                    tkb.phong,
                    CONCAT('Thứ ', tkb.thu, ' / Tiết ', tkb.tiet_bat_dau, '-', tkb.tiet_bat_dau + tkb.so_tiet - 1),
                    CONCAT('Tiết ', tkb.tiet_bat_dau, '-', tkb.tiet_bat_dau + tkb.so_tiet - 1, ' tại ', tkb.phong)
                FROM 
                    sinh_vien_hoc_phan svhp
                JOIN sinh_vien sv ON svhp.id_sv = sv.id_sv
                JOIN hoc_phan hp ON svhp.id_hoc_phan = hp.id_hoc_phan
                JOIN giang_vien gv ON hp.id_gv = gv.id_gv
                JOIN thoi_khoa_bieu tkb ON hp.id_hoc_phan = tkb.id_hoc_phan
                WHERE 
                    sv.ma_sv = %s
                ORDER BY tkb.thu, tkb.tiet_bat_dau;
            """
            print(f"Đang thực hiện truy vấn toàn bộ thời khóa biểu cho sinh viên mã = {student_id}")
            cursor.execute(query, (student_id,))
            results = cursor.fetchall()

            print("Kết quả truy vấn toàn bộ thời khóa biểu:")
            if not results:
                print("Không có dữ liệu thời khóa biểu.")
            for i, row in enumerate(results, start=1):
                print(f"{i}. {row}")

            schedule_items = []
            for row in results:
                item = ScheduleItem(*row)
                print("Đối tượng ScheduleItem tạo ra:", item.__dict__)
                schedule_items.append(item)

            return schedule_items

        except Exception as e:
            print("Lỗi khi truy vấn toàn bộ thời khóa biểu:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Đã ngắt kết nối CSDL.")
