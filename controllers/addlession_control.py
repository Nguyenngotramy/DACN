from database.connBD import connectDB
from datetime import date
from models.lessonModel import LessonModel  

class Lession_control:
    def __init__(self):
        self.connection = connectDB()
        if self.connection:
            print("Đã kết nối CSDL trong controller.")
        else:
            print("Không thể kết nối tới CSDL.")

    def insert_lession(self, id_hoc_phan, ngay_hoc, ten_bai_giang):
        try:
            cursor = self.connection.cursor()
            check_sql = """
                SELECT COUNT(*) FROM diem_danh_faceid.buoi_diem_danh 
                WHERE id_hoc_phan = %s AND ngay_hoc = %s
            """
            cursor.execute(check_sql, (id_hoc_phan, ngay_hoc))
            count = cursor.fetchone()[0]

            if count > 0:
                print("Buổi học đã tồn tại, không thể thêm trùng.")
                return False

            insert_sql = """
                INSERT INTO diem_danh_faceid.buoi_diem_danh 
                (id_hoc_phan, ngay_hoc, ten_bai_giang)
                VALUES (%s, %s, %s)
            """
            values = (id_hoc_phan, ngay_hoc, ten_bai_giang)
            cursor.execute(insert_sql, values)
            self.connection.commit()
            print("Đã thêm buổi học mới.")
            return True

        except Exception as e:
            print("Lỗi khi thêm buổi học:", e)
            return False

    def get_lesson_by_idteacher(self, teacher_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = """
                SELECT 
                    h.id_hoc_phan,
                    h.ten_hoc_phan,
                    b.ten_bai_giang,
                    b.ngay_hoc
                FROM 
                    diem_danh_faceid.hoc_phan h
                JOIN 
                    diem_danh_faceid.buoi_diem_danh b ON h.id_hoc_phan = b.id_hoc_phan
                JOIN 
                    diem_danh_faceid.giang_vien gv ON h.id_gv = gv.id_gv
                WHERE 
                    gv.ma_gv = %s
                    AND b.ngay_hoc = CURDATE();
            """
            cursor.execute(sql, (teacher_id,))
            rows = cursor.fetchall()

            lessons = []
            for row in rows:
                lesson = LessonModel(
                    course_id=row['id_hoc_phan'],
                    course_name=row['ten_hoc_phan'],
                    lecture_name=row['ten_bai_giang'],
                    study_date=row['ngay_hoc']
                )
                lessons.append(lesson)

            return lessons

        except Exception as e:
            print("Error fetching lessons:", e)
            return []

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Đã ngắt kết nối CSDL.")
