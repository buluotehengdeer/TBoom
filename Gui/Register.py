from PyQt5.QtWidgets import (QLineEdit, QLabel, QMessageBox,
                             QGridLayout, QPushButton)
from PyQt5.QtGui import QImage, QPixmap
from Gui import Gui
from PyQt5.QtCore import Qt
# import sys
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from db.db import *


class Register(Gui):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.style = """
            QPushButton{background-color:grey;color:white;}
            #window{ background:pink;margin:0 px }
            """
        self.setObjectName("window")
        self.setStyleSheet(self.style)
        userName = QLabel('用户名')
        passWord = QLabel('密码')
        submit = QPushButton("提交")
        image = QImage('register.jpeg')
        img = QPixmap(image)
        img = img.scaled(500, 500, Qt.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(img)
        self.userEdit = QLineEdit()
        self.passWdEdit = QLineEdit()
        self.passWdEdit.setEchoMode(QLineEdit.Password)

        grid = QGridLayout()
        grid.addWidget(image_label, 1, 0, 1, 4)
        grid.addWidget(userName, 2, 0)
        grid.addWidget(self.userEdit, 2, 1)
        grid.addWidget(passWord, 3, 0)
        grid.addWidget(self.passWdEdit, 3, 1)
        grid.addWidget(submit, 3, 3)
        self.setLayout(grid)
        self.setWindowTitle('注册')
        self.show()

        submit.clicked.connect(self.submit)

    def submit(self):
        username = self.userEdit.text()
        password = self.passWdEdit.text()
        res = isExist(username)
        if res:
            QMessageBox.question(self, 'Message',
                                 "用户名已存在！")
        else:
            insertData(username, password)
            QMessageBox.question(self, 'Message',
                                 "Success!")
