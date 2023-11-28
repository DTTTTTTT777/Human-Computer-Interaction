from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QObject, pyqtSignal

import sys
import speech_recognition as sr
import threading
import win32api
import webbrowser
import socket
import difflib
import threading
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 1024)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 560, 402, 102))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 500, 402, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(140, 100, 321, 241))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 360, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 670, 402, 102))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 360, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 780, 412, 132))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.label_5.setText(_translate("MainWindow", "3. Surf internet by saying \"Open a webpage\""))

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myThread=None

    def showEvent(self, e): #注意这是框架中预定义的用于处理特定的事件类型的函数，名字不能改变
        try:
            print("start")
            self.myThread=MyThread()
            #self.myThread.command_signal.connect(self.update_command)  # 连接信号
            self.myThread.start()
        except:
            print("thread start failed")

    def closeEvent(self, e):
        self.myThread.stop()
        print("closed")

    #def update_command(self, command):
        #self.ui.commandLabel.setText(command)  # 更新UI界面

def isNetConnected():
    try:
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False

class MyThread(threading.Thread):#, QObject):

    #command_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()
        self._stop=False

    def run(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        while self._stop == False:
            response = self.recognize_speech_from_mic(recognizer, microphone)
            if response["error"]:
                print("ERROR: {}".format(response["error"]))
                continue
            command = response["transcription"]
            if self._stop == False:
                print(command)
                self.execute_command(command)
                #self.command_signal.emit(command)
            else:
                break

    def execute_command(self, command):
        music_keywords=["music", "using", "you may", "moving", "you mean the", "meaning", "you think"]
        notepad_keywords=["notepad", "no pad", "no impact", "no that", "note pad", "note", "notes"]
        webpage_keywords=["web page", "webpage", "web", "lap pads", "google"]

        if any(keyword in command.lower() for keyword in music_keywords):
            win32api.ShellExecute(0, 'open', 'wmplayer.exe', '', '', 1)
        elif any(keyword in command.lower() for keyword in notepad_keywords):
            win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
        elif any(keyword in command.lower() for keyword in webpage_keywords):
            webbrowser.open("https://www.google.com")


    def recognize_speech_from_mic(self, recognizer, microphone):
        """Transcribe speech from recorded from `microphone`.
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occurred, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            #audio = recognizer.listen(source)
            print("Listening")
            audio=recognizer.record(source,duration=5)
        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            if isNetConnected():
            #if 1:
                print("Google Recognizing")
                response["transcription"]=recognizer.recognize_google(audio)
                if response["transcription"]=="":
                    print("NULL")
            else:
                print("Sphinx Recognizing")
                response["transcription"] = recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

    def stop(self):
        self._stop = True
        #print(self._stop)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())
