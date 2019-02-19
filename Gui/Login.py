import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PyQt5.QtWidgets import (QLineEdit, QLabel, QMessageBox,
                             QGridLayout, QPushButton, QApplication)
from PyQt5.QtGui import QImage, QPixmap
from Gui import Gui
from PyQt5.QtCore import Qt
import sys
from db.db import *
import Register
from game.main import *


class Login(Gui):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        '''
            初始化窗口
        '''
        self.style = """
            QPushButton{background-color:grey;color:white;}
            #window{ background:pink;margin:0 px }
            """
        self.setObjectName("window")
        self.setStyleSheet(self.style)
        userName = QLabel('用户名')
        passWord = QLabel('密码')
        register = QPushButton("注册")
        login = QPushButton("登入")
        image = QImage('login.jpeg')
        img = QPixmap(image)
        # 缩放图片
        img = img.scaled(500, 500, Qt.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(img)
        self.userEdit = QLineEdit()
        self.passWdEdit = QLineEdit()
        self.passWdEdit.setEchoMode(QLineEdit.Password)
        grid = QGridLayout()
        # 向网格布局中添加组件
        grid.addWidget(image_label, 1, 0, 1, 4)
        grid.addWidget(userName, 2, 0)
        grid.addWidget(self.userEdit, 2, 1)
        grid.addWidget(register, 2, 3)
        grid.addWidget(passWord, 3, 0)
        grid.addWidget(self.passWdEdit, 3, 1)
        grid.addWidget(login, 3, 3)

        # 注册监听者
        login.clicked.connect(self.login)
        register.clicked.connect(self.register)

        self.setLayout(grid)
        self.center()
        self.setWindowTitle('登入')
        self.show()

    def login(self):
        username = self.userEdit.text()
        password = self.passWdEdit.text()
        res = queryData(username, password)
        if res:
            run(username)
        else:
            QMessageBox.question(self, 'Message',
                                 "用户名或者密码错误!")

    def register(self):
        self.reg = Register.Register()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    l = Login()
    sys.exit(app.exec_())
