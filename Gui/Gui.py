from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QGridLayout, QPushButton, QDesktopWidget, QApplication



class Gui(QWidget):
    '''
        A Gui base class 
    '''

    def __init__(self):

        super().__init__()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
