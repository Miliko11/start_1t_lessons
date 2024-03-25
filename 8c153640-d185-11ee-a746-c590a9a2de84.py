import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QLabel, QVBoxLayout, QHBoxLayout


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Музыкальный плеер")
        self.setGeometry(100,100,400,200)

        self.initUI()

    def initUI(self):
        self.player = QMediaPlayer()

        self.play_button = QPushButton("Воспроизвести")
        self.play_button.clicked.connect(self.play_music)

        self.pause_button = QPushButton("Пауза")
        self.pause_button.clicked.connect(self.pause_music)

        self.stop_button = QPushButton("Стоп")
        self.stop_button.clicked.connect(self.stop_music)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setValue(50)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setToolTip('Громкость')
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setToolTip('Позиция')
        self.position_slider.sliderMoved.connect(self.set_position)

        self.backward_button = QPushButton('<< 10 сек')
        self.backward_button.clicked.connect(self.backward_music)

        self.forward_button = QPushButton('10 сек >>')
        self.forward_button.clicked.connect(self.forward_music)

        self.track_label = QLabel("Название трека")

        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox1.addWidget(self.play_button)
        hbox1.addWidget(self.pause_button)
        hbox1.addWidget(self.stop_button)
        hbox1.addWidget(self.volume_slider)

        hbox2.addWidget(self.backward_button)
        hbox2.addWidget(self.position_slider)
        hbox2.addWidget(self.forward_button)

        vbox.addWidget(self.track_label)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def play_music(self):
        file_name = 'song.mp3'
        url = QUrl.fromLocalFile(file_name)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def pause_music(self):
        self.player.pause()

    def stop_music(self):
        self.player.stop()

    def set_volume(self):
        volume = self.volume_slider.value()
        self.player.setVolume(volume)

    def backward_music(self):
        position_m = max(0,self.player.position()-10000)
        self.player.setPosition(position_m)

    def forward_music(self):
        position_m = min(self.player.duration(),self.player.position()+10000)
        self.player.setPosition(position_m)

    def set_position(self,position):
        self.player.setPosition(position)

app = QApplication(sys.argv)
playerM = MusicPlayer()
playerM.show()
sys.exit(app.exec())