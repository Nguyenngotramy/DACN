import socket
import threading
import json

class TCPServer:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.server = None
        self.clients = []
        self.running = False

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.running = True
        print(f"[TCPServer] Đang lắng nghe tại {self.host}:{self.port} ...")

        # Bắt đầu luồng chính nhận kết nối
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        while self.running:
            try:
                client_sock, addr = self.server.accept()
                print(f"[TCPServer] Sinh viên kết nối từ {addr}")
                self.clients.append(client_sock)
                threading.Thread(target=self.handle_client, args=(client_sock,), daemon=True).start()
            except Exception as e:
                print(f"[TCPServer] Lỗi accept: {e}")

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"[TCPServer] Dữ liệu nhận từ client: {data}")
        except:
            print("[TCPServer] Client ngắt kết nối.")
        finally:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            client_socket.close()

    def notify_checkin_start(self, course_id, lecture_name):
        print("[TCPServer] Gửi tín hiệu CHECKIN_START đến tất cả sinh viên...")
        message = {
            "type": "CHECKIN_START",
            "course_id": course_id,
            "lecture_name": lecture_name
        }
        encoded_msg = json.dumps(message).encode()
        print(encoded_msg)

        for client in self.clients:
            try:
                client.sendall(encoded_msg)
            except:
                print("[TCPServer] Lỗi khi gửi tín hiệu đến một client.")

    def stop_server(self):
        self.running = False
        if self.server:
            self.server.close()
        for client in self.clients:
            client.close()
        self.clients.clear()
        print("[TCPServer] Server đã dừng.")
