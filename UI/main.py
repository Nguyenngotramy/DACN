import sys
from PyQt5 import QtWidgets
from test import Ui_MainWindow 

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Tạo instance giao diện
        self.ui.setupUi(self)      # Thiết lập giao diện lên MainWindow

        # Bắt đầu viết code xử lý sự kiện, logic tại đây
        self.ui
        self.ui.timetabebtn2.clicked.connect(self.handle_timetable)
        self.ui.timetablebtn.clicked.connect(self.handle_timetable)

        self.ui.logoutbtn_2.clicked.connect(self.handle_logout)
        self.ui.logoutbtn.clicked.connect(self.handle_logout)
        
        self.ui.historybtn_2.clicked.connect(self.handle_history)
        self.ui.historybtn.clicked.connect(self.handle_history)
        
        self.ui.userbtn_2.clicked.connect(self.handle_user)
        self.ui.userbtn.clicked.connect(self.handle_user)
    def handle_timetable(self):
        print("Nhấn vào nút Thời khóa biểu!")
        self.ui.stackedWidget.setCurrentIndex(0)

    def handle_logout(self):
        print("Đăng xuất!")
    def handle_history(self):
        print("history")
        self.ui.stackedWidget.setCurrentIndex(1)
    def handle_user(self):
        print("Nhấn vào user")
        self.ui.stackedWidget.setCurrentIndex(2)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
