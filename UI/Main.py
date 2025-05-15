import sys
from PyQt5 import QtWidgets
from loginui import Ui_MainWindow
from controllers.contLogin import LoginController

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = LoginController()

        # Gắn sự kiện nút đăng nhập
        self.ui.pushButton_2.clicked.connect(self.handle_login)

    def handle_login(self):
        try:
            email = self.ui.lineEdit_2.text()
            passw = self.ui.passw.text()  # Đảm bảo tên widget này đúng với file .ui
            print(f"Email: {email}, Password: {passw}")

            success, role = self.controller.login(email, passw)

            if success:
                QtWidgets.QMessageBox.information(self, "Đăng nhập", f"Thành công ({role})!")
            else:
                QtWidgets.QMessageBox.warning(self, "Thất bại", "Email hoặc mật khẩu sai.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", str(e))
            print("LỖI:", e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())