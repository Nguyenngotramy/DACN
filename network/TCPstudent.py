import socket
import threading
import json

class StudentClient:
    def __init__(self, server_ip='192.168.10.123', port=12345):
        self.server_ip = server_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_teacher(self):
        try:
            self.socket.connect((self.server_ip, self.port))
            print("Kết nối tới giáo viên thành công.")
            threading.Thread(target=self.listen_server, daemon=True).start()
        except Exception as e:
            print("Không thể kết nối:", e)

    def listen_server(self):
        while True:
            try:
                data = self.socket.recv(1024).decode()
                if not data:
                    break 

                try:
                    message = json.loads(data)
                    if message.get("type") == "CHECKIN_START":
                        course_id = message.get("course_id", "N/A")
                        lecture_name = message.get("lecture_name", "N/A")
                        print(f"Được phép điểm danh id {course_id}, môn {lecture_name}.")
                        self.enable_checkin_button(course_id, lecture_name)
                except json.JSONDecodeError:
                    print("Không thể giải mã dữ liệu nhận được:", data)

            except Exception as e:
                print("Lỗi khi nhận dữ liệu từ server:", e)
                break

    def enable_checkin_button(self, course_id, lecture_name):
        print(f"[GUI] Nút điểm danh đã được bật cho môn {course_id}, giảng viên {lecture_name}.")
