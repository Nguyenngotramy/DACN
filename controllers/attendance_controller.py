from database.connBD import connectDB
from models.AttendanceRecord import AttendanceRecord
from typing import List, Tuple

class AttendanceController:
    def __init__(self):
        self.connection = connectDB()
        if self.connection:
            print("Đã kết nối CSDL trong AttendanceController.")
        else:
            print("Không thể kết nối tới CSDL.")

    def get_attendance_by_student(self, student_id):
        """
        Truy vấn lịch sử điểm danh của sinh viên dựa trên mã số sinh viên.
        """
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.ten_hoc_phan,
                    bdd.ngay_hoc,
                    bdd.gio_bat_dau,
                    bdd.gio_ket_thuc,
                    dd.thoi_gian_vao,
                    dd.thoi_gian_ra,
                    dd.trang_thai
                FROM 
                    diem_danh_faceid.diem_danh dd
                JOIN 
                    diem_danh_faceid.buoi_diem_danh bdd ON dd.id_buoi = bdd.id_buoi
                JOIN 
                    diem_danh_faceid.sinh_vien sv ON dd.id_sv = sv.id_sv
                JOIN 
                    diem_danh_faceid.hoc_phan hp ON bdd.id_hoc_phan = hp.id_hoc_phan
                WHERE 
                    sv.ma_sv = %s
                ORDER BY 
                    bdd.ngay_hoc DESC;
            """
            print(f"Thực hiện truy vấn điểm danh cho sinh viên mã: {student_id}")
            cursor.execute(query, (student_id,))
            results = cursor.fetchall()

            if not results:
                print("Không có dữ liệu điểm danh.")
                return []

            attendance_records = []
            for row in results:
                record = AttendanceRecord(*row)
                attendance_records.append(record)

            return attendance_records

        except Exception as e:
            print("Lỗi khi truy vấn dữ liệu điểm danh:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def get_current_courses_by_student(self, student_id):
        """
        Lấy danh sách học phần mà sinh viên đang tham gia trong kỳ hiện tại.
        """
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT 
                    hp.ten_hoc_phan
                FROM 
                    diem_danh_faceid.sinh_vien_hoc_phan svhp
                JOIN 
                    diem_danh_faceid.hoc_phan hp ON svhp.id_hoc_phan = hp.id_hoc_phan
                JOIN
                    diem_danh_faceid.sinh_vien sv ON svhp.id_sv = sv.id_sv
                WHERE 
                    sv.ma_sv = %s
                    AND CURDATE() BETWEEN hp.ngay_bat_dau AND hp.ngay_ket_thuc
            """
            print(f"Thực hiện truy vấn các học phần đang học cho sinh viên mã: {student_id}")
            cursor.execute(query, (student_id,))
            results = cursor.fetchall()

            if not results:
                print("Sinh viên không tham gia học phần nào trong kỳ hiện tại.")
                return []

            courses = [row[0] for row in results]
            return courses

        except Exception as e:
            print("Lỗi khi truy vấn học phần hiện tại:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def get_enum_values_for_column(self, table_name, column_name):
        """
        Lấy danh sách các giá trị enum của một cột trong bảng.
        """
        try:
            cursor = self.connection.cursor()
            query = f"SHOW COLUMNS FROM {table_name} LIKE '{column_name}'"
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                type_str = result[1]  # enum('A','B','C',...)
                start = type_str.find("(") + 1
                end = type_str.find(")")
                enums = type_str[start:end].replace("'", "").split(",")
                return [e.strip() for e in enums]
            return []
        except Exception as e:
            print("Lỗi khi lấy enum values:", e)
            return []
        finally:
            if self.connection.is_connected():
                cursor.close()

    def get_attendance_history_byfilter(self, student_code: str, subject: str, date: str, status: str) -> List[Tuple]:
        """
        Truy vấn lịch sử điểm danh có lọc theo học phần, ngày và trạng thái.
        Nếu date là None hoặc 'All' thì không lọc theo ngày.
        """
        base_query = """
            SELECT 
                hp.ten_hoc_phan,
                bdd.ngay_hoc,
                bdd.gio_bat_dau,
                bdd.gio_ket_thuc,
                dd.thoi_gian_vao,
                dd.thoi_gian_ra,
                dd.trang_thai
            FROM 
                diem_danh_faceid.diem_danh dd
            JOIN 
                diem_danh_faceid.buoi_diem_danh bdd ON dd.id_buoi = bdd.id_buoi
            JOIN 
                diem_danh_faceid.sinh_vien sv ON dd.id_sv = sv.id_sv
            JOIN 
                diem_danh_faceid.hoc_phan hp ON bdd.id_hoc_phan = hp.id_hoc_phan
            WHERE 
                sv.ma_sv = %s
                AND (%s = 'All' OR hp.ten_hoc_phan = %s)
                AND (%s = 'All' OR dd.trang_thai = %s)
        """

        params = [student_code, subject, subject, status, status]

        # Thêm điều kiện lọc ngày nếu date khác None và khác 'All'
        if date and date != 'All':
            base_query += " AND DATE(bdd.ngay_hoc) = %s"
            params.append(date)

        base_query += " ORDER BY bdd.ngay_hoc DESC"

        print("Thực thi truy vấn với các tham số:")
        print(f"  Mã sinh viên: {student_code}")
        print(f"  Môn học: {subject}")
        print(f"  Trạng thái: {status}")
        print(f"  Ngày: {date if date else 'Tất cả ngày'}")

        try:
            cursor = self.connection.cursor()
            cursor.execute(base_query, tuple(params))
            result = cursor.fetchall()
            print(f"Truy vấn trả về {len(result)} dòng.")
            return result

        except Exception as e:
            print("Lỗi khi truy vấn dữ liệu có lọc:", e)
            return []

        finally:
            if self.connection.is_connected():
                cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Đã ngắt kết nối CSDL.")
