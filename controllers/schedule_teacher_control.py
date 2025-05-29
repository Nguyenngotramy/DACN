from database.connBD import connectDB
from models.TeachingSchedule import TeachingSchedule

class ScheduleController:
    def __init__(self):
        self.connection = connectDB()
        if self.connection:
            print("Đã kết nối CSDL trong controller.")
        else:
            print("Không thể kết nối tới CSDL.")

    def get_schedule(self, teacher_id):
        """Truy vấn thời khóa biểu hôm nay của giảng viên theo mã giảng viên (ma_gv)."""
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.id_hoc_phan,
                    hp.ten_hoc_phan,
                    tkb.phong,
                    tkb.thu,
                    tkb.so_tiet,
                    tkb.tuan_hoc
                FROM 
                    giang_vien gv
                JOIN 
                    hoc_phan hp ON gv.id_gv = hp.id_gv
                JOIN 
                    thoi_khoa_bieu tkb ON hp.id_hoc_phan = tkb.id_hoc_phan
                WHERE 
                    gv.ma_gv = %s
                    AND tkb.thu = DAYOFWEEK(CURDATE()) - 1
                    AND hp.ngay_ket_thuc >= CURDATE()
                ORDER BY 
                    hp.ten_hoc_phan, tkb.thu, tkb.tiet_bat_dau;
            """
            print(f"Đang thực hiện truy vấn thời khóa biểu hôm nay cho giảng viên mã: {teacher_id}")
            cursor.execute(query, (teacher_id,))
            results = cursor.fetchall()

            print("Kết quả truy vấn hôm nay:")
            if not results:
                print("Không có dữ liệu thời khóa biểu hôm nay.")

            schedule_items = []
            for row in results:
                item = TeachingSchedule(*row)
                print("Đối tượng TeachingSchedule tạo ra:", item.__dict__)
                schedule_items.append(item)

            return schedule_items

        except Exception as e:
            print("Lỗi khi truy vấn thời khóa biểu hôm nay:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def get_all_schedule(self, teacher_id):
        """Truy vấn toàn bộ thời khóa biểu của giảng viên theo mã giảng viên (ma_gv)."""
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.id_hoc_phan,
                    hp.ten_hoc_phan,
                    tkb.phong,
                    tkb.thu,
                    tkb.so_tiet,
                    tkb.tuan_hoc
                FROM 
                    giang_vien gv
                JOIN 
                    hoc_phan hp ON gv.id_gv = hp.id_gv
                JOIN 
                    thoi_khoa_bieu tkb ON hp.id_hoc_phan = tkb.id_hoc_phan
                WHERE 
                    gv.ma_gv = %s
                ORDER BY 
                    hp.ten_hoc_phan, tkb.thu, tkb.tiet_bat_dau;
            """
            print(f"Đang thực hiện truy vấn thời khóa biểu cho giảng viên mã: {teacher_id}")
            cursor.execute(query, (teacher_id,))
            results = cursor.fetchall()

            print("Kết quả truy vấn:")
            if not results:
                print("Không có dữ liệu thời khóa biểu.")

            schedule_items = []
            for row in results:
                item = TeachingSchedule(*row)
                print("Đối tượng TeachingSchedule tạo ra:", item.__dict__)
                schedule_items.append(item)

            return schedule_items

        except Exception as e:
            print("Lỗi khi truy vấn thời khóa biểu:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Đã ngắt kết nối CSDL.")
