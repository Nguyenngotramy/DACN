
class HomeController:
    def __init__(self, ui):
        self.ui = ui
        self.connect_buttons()

    def connect_buttons(self):
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
        self.ui.stackedWidget.setCurrentIndex(2)

    def handle_user(self):
        print("Nhấn vào user")
        self.ui.stackedWidget.setCurrentIndex(1)
