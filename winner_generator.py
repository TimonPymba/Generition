from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
#подключение библиотек

app = QApplication([])
main_win = QWidget()

#создание элементов интерфейса
text = QLabel("Нажми чтобы узнать победителя")
winner = QLabel("?")
button = QPushButton("Сгенерировать")
#привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText("Победитель")
button.clicked.connect(show_winner)
#обработка событий
main_win.show()
#запуск приложения
app.exec_()