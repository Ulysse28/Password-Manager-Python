"""
Passwords Manager in Python
By Ulysse Valdenaire
Main Python File
11/08/2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import crypte
import pymysql.cursors
import database

"""
Class of the main window
"""
class MyWindow(QMainWindow):

    #Constructor
    def __init__(self, connection):
        #Mother class
        super(MyWindow, self).__init__()
        #function who build the part "crypte password"
        self.initUI_CryptePwd()
        #function who builds the part "find password"
        self.initUI_FindPwd()
        #properties of the window
        self.setGeometry(200, 100, 1500, 900)
        self.setWindowTitle("Password Manager")
        self.connection = connection
       
    def initUI_CryptePwd(self):
        """
        Function who builds the part "crypte password"
        :return: nothing
        """
        #Label of the title 'PASSWORD MANAGER'
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setText("PASSWORD MANAGER")
        self.label_title.move(525, 50)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_title.setFont(font)
        self.update_size(self.label_title)

        #Label for "Crypte password"
        self.label_crypte = QtWidgets.QLabel(self)
        self.label_crypte.setText('CRYPTE PASSWORD')
        self.label_crypte.move(200, 150)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_crypte.setFont(font)
        self.update_size(self.label_crypte)

        #Label "for what ?"
        self.label_what = QtWidgets.QLabel(self)
        self.label_what.setText('For what ? ')
        self.label_what.move(150, 250)
        font=QtGui.QFont()
        font.setPointSize(13)
        self.label_what.setFont(font)
        self.update_size(self.label_what)

        #line edit for the websute's name (or appli etc)
        self.edit_name_password = QtWidgets.QLineEdit(self)
        self.edit_name_password.setGeometry(400, 250, 175, 25)

        #label for password
        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setText('Your password')
        self.label_password.move(150, 350)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_password.setFont(font)
        self.update_size(self.label_password)

        #line edit for the password
        self.edit_password = QtWidgets.QLineEdit(self)
        self.edit_password.setGeometry(400, 350, 175, 25)

        #label "key"
        self.label_key = QtWidgets.QLabel(self)
        self.label_key.setText('Your key')
        self.label_key.move(150, 450)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_key.setFont(font)
        self.update_size(self.label_key)

        #line edit for the key
        self.edit_key = QtWidgets.QLineEdit(self)
        self.edit_key.setGeometry(400, 450, 175, 25)

        #label "security level"
        self.label_security = QtWidgets.QLabel(self)
        self.label_security.setText('Security level ')
        self.label_security.move(150, 550)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_security.setFont(font)
        self.update_size(self.label_security)

        #line edit for the security level
        self.edit_security = QtWidgets.QLineEdit(self)
        self.edit_security.setGeometry(400, 550, 175, 25)

        #label "crypte password"
        self.label_crypte_pwd = QtWidgets.QLabel(self)
        self.label_crypte_pwd.setText("Crypte Password ? ")
        self.label_crypte_pwd.move(150, 650)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_crypte_pwd.setFont(font)
        self.update_size(self.label_crypte_pwd)

        #button 'ok' to crypte the password
        self.crypted_button = QtWidgets.QPushButton(self)
        self.crypted_button.setText('OK')
        self.crypted_button.move(400, 650)
        self.crypted_button.clicked.connect(self.createPwd)

        #label to see the crypted password or a message
        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setText('')
        self.label_password.move(150, 750)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_password.setFont(font)
        self.update_size(self.label_password)

    def initUI_FindPwd(self):
        """
        Build the part 'Find your password'
        :return: nothing
        """
        #label 'find your password'
        self.label_find_pwd = QtWidgets.QLabel(self)
        self.label_find_pwd.setText('FIND YOUR PASSWORD')
        self.label_find_pwd.move(1000, 150)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_find_pwd.setFont(font)
        self.update_size(self.label_find_pwd)

        #label 'for what ?'
        self.label_what2 = QtWidgets.QLabel(self)
        self.label_what2.setText('For what ? ')
        self.label_what2.move(825, 250)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_what2.setFont(font)
        self.update_size(self.label_what2)

        #line edit for what
        self.edit_name_find = QtWidgets.QLineEdit(self)
        self.edit_name_find.setGeometry(1100, 250, 175, 25)

        #label 'search for it'
        self.label_search = QtWidgets.QLabel(self)
        self.label_search.setText('Search fot it ? ')
        self.label_search.move(825, 450)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_search.setFont(font)
        self.update_size(self.label_search)

        #button ok
        self.button_go_search = QtWidgets.QPushButton(self)
        self.button_go_search.setText('OK')
        self.button_go_search.move(1100,450)
        self.button_go_search.clicked.connect(self.getPwd)

        #label key
        self.label_key_find = QtWidgets.QLabel(self)
        self.label_key_find.setText('Enter your key')
        self.label_key_find.move(825, 350)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_key_find.setFont(font)
        self.update_size(self.label_key_find)

        #line edit key
        self.edit_key_find = QtWidgets.QLineEdit(self)
        self.edit_key_find.move(1100, 350)

        #label 'your password'
        self.label_password_find = QtWidgets.QLabel(self)
        self.label_password_find.setText('Your password : ')
        self.label_password_find.move(825, 650)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_password_find.setFont(font)
        self.update_size(self.label_password_find)

        #label to display the password
        self.label_display_pwd = QtWidgets.QLabel(self)
        self.label_display_pwd.setText("          ")
        self.label_display_pwd.move(1100, 650)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_display_pwd.setFont(font)

    def update_size(self, label):
        """
        Adjust the size of a element
        :param label: what is the element to adjust the size
        :return: nothing
        """
        label.adjustSize()

    def createPwd(self):
        """
        Create a crypted password with the name of the platform, the real password, a key to access the real password
        and a security levem
        """
        name = self.edit_name_password.text()
        password = self.edit_password.text()
        key = self.edit_key.text()
        security_level = self.edit_security.text()
        self.update_size(self.label_password)
        crypted_password = crypte.code_cesar(password, key, security_level)
        database.createBook2(self.connection, name, crypted_password, key, security_level)
       
    def getPwd(self):
        """
        Get a crypted password from the database
        and decrypt it and display it
        """
        name = self.edit_name_find.text()
        key = self.edit_key_find.text()
        cryptedPwd, security = database.getBook(self.connection, name)
        print("Mot de passe : ", cryptedPwd, " securité  ", security)
        decryptPWD = crypte.decode_cesar(cryptedPwd, key, security)
        self.label_display_pwd.setText(decryptPWD)
           
def window(connection):
    """
    run the window with the instance of MyWindow class
    """
    app = QApplication(sys.argv)
    win = MyWindow(connection)
    win.show()
    #Exit the application
    sys.exit(app.exec_())

def app():
    try:
        connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='',
                                    db="books")

        print("----------CONNECTION SUCCESFULL----------")
      
        window(connection) 

    except:
        print('Error, connection impossible, please try again')



connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='',
                                    db="books")
window(connection)