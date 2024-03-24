import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QListWidget

class BruteforceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Bruteforce"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel("Login Status: ", self)
        self.label.setGeometry(10, 10, 200, 20)

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(10, 40, 80, 20)
        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(100, 40, 200, 20)

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(10, 70, 80, 20)
        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(100, 70, 200, 20)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(100, 100, 80, 20)
        self.login_button.clicked.connect(self.login)

        self.logout_button = QPushButton("Logout", self)
        self.logout_button.setGeometry(200, 100, 80, 20)
        self.logout_button.clicked.connect(self.logout)

        self.options_button = QPushButton("Options", self)
        self.options_button.setGeometry(100, 130, 80, 20)
        self.options_button.clicked.connect(self.show_options)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(200, 130, 80, 20)
        self.exit_button.clicked.connect(self.close)

        self.login_attempts = {}
        self.max_Login_attempts_known_account = 3
        self.max_Login_attempts_unknown_account = 2

        self.login_status = "Logged Out"
        self.login_status_label = QLabel(self.login_status, self)
        self.login_status_label.setGeometry(10, 220, 200, 20)

        self.login_attempts_label = QLabel("Login Attempts:", self)
        self.login_attempts_label.setGeometry(10, 240, 100, 20)

        self.login_attempts_list = QListWidget(self)
        self.login_attempts_list.setGeometry(100, 240, 200, 150)

        self.show()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        known_accounts = {
            "admin": "LookForTheWindInThe18THArea()",
            "user1": "BUSstop.0.0.1>@halo3",
            "user2": "CountArthurDwell_76Cv=@",
            "user3": "The_Great_Hammer_Of_Olympus"
        }

        if username in known_accounts:
            if password == known_accounts[username]:
                self.login_status = "Logged In"
                self.login_status_label.setText(self.login_status)
                self.login_attempts[username] = 0
            else:
                if username not in self.login_attempts:
                    self.login_attempts[username] = 1

                self.login_attempts[username] += 1

                if self.login_attempts[username] >= self.max_Login_attempts_known_account:
                    self.login_status = "Locked Out"
                    self.login_status_label.setText(self.login_status)

            self.update_login_attempts_list()

    def logout(self):
        self.login_status = "Logged Out"
        self.login_status_label.setText(self.login_status)
        self.login_attempts.clear()
        self.update_login_attempts_list()

    def update_login_attempts_list(self):
        self.login_attempts_list.clear()
        for account, attempts in self.login_attempts.items():
            self.login_attempts_list.addItem(f"{account}: {attempts} attempts")

    def show_options(self):
        print("Options button clicked")
        # Implement option window creation here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BruteforceApp()
    sys.exit(app.exec_())

