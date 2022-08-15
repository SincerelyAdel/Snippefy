from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget)
from PyQt5.QtCore import QSize
import sys
import os

class prototype():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.string_input = QTextEdit()
        self.string_result = QTextEdit()
        self.layout_V0 = QVBoxLayout()
        self.layout_H1 = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm")
        self.clear_button = QPushButton("Clear")
        self.main_widget = QWidget()

        self.confirm_button.clicked.connect(self.confirm_pressed)
        self.clear_button.clicked.connect(self.clear_pressed)

        self.main_window.setFixedSize(QSize(1000, 700))
        self.main_window.setWindowTitle("Snippefy")
        self.main_window.setContentsMargins(3, 3, 3, 3)
        self.main_window.setWindowIcon(QtGui.QIcon("camera.png"))
        self.string_input.setPlaceholderText("Input Something To Snippefy...")
        self.string_result.setPlaceholderText("Your Result Will Pop Up Here...")
        self.string_result.setFixedHeight(100)

        self.layout_V0.addWidget(self.string_input)
        self.layout_V0.addWidget(self.string_result)
        self.layout_H1.addWidget(self.confirm_button)
        self.layout_H1.addWidget(self.clear_button)
        self.layout_V0.addLayout(self.layout_H1)
        self.main_widget.setLayout(self.layout_V0)
        self.main_window.setCentralWidget(self.main_widget)
        
    def execute(self) -> None:
        self.main_window.show()
        sys.exit(self.app.exec_())

    def confirm_pressed(self):
        container = self.string_input.toPlainText()
        new_snippet = r""
        tab_switch = "    "
        for i in container:
            new_snippet += i

        new_snippet  = new_snippet.replace(tab_switch, "\t")
        new_snippet = repr(new_snippet)
        self.string_result.setPlainText(new_snippet)
    
    def clear_pressed(self):
        self.string_input.setPlainText('')
        self.string_result.setPlainText("")


if __name__ == "__main__":
    instance = prototype()
    instance.execute()