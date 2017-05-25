import sys
from PyQt4 import QtGui, QtCore

num = 0.0
second_num = 0.0
sumX = 0.0
operator = ""
var = False
sum_it = 0

class Calculator(QtGui.QWidget):

    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()

    def initUI(self):

        #Initialize window
        self.setGeometry(0, 0, 306, 353)
        self.setWindowTitle("Basic Calculator")

        #Initialize line edit
        self.line_edit = QtGui.QLineEdit(self)
        self.line_edit.setGeometry(40, 30, 231, 41)
        self.line_edit.setReadOnly(True)

        #Extra accessories
        self.time = QtGui.QDateTimeEdit(self)
        self.time.setGeometry(70, 300, 145, 30)
        self.time.setDateTime(QtCore.QDateTime.currentDateTime())

        #Initialize buttons
        zero = QtGui.QPushButton('0', self)
        one = QtGui.QPushButton('1', self)
        two = QtGui.QPushButton('2', self)
        three = QtGui.QPushButton('3', self)
        four = QtGui.QPushButton('4', self)
        five = QtGui.QPushButton('5', self)
        six = QtGui.QPushButton('6', self)
        seven = QtGui.QPushButton('7', self)
        eight = QtGui.QPushButton('8', self)
        nine = QtGui.QPushButton('9', self)
        clear_button = QtGui.QPushButton('C', self)
        add_button = QtGui.QPushButton('+', self)
        subtract_button = QtGui.QPushButton('-', self)
        multiply_button = QtGui.QPushButton('x', self)
        divide_button = QtGui.QPushButton('/', self)
        square_button = QtGui.QPushButton('^2', self)
        equals_button = QtGui.QPushButton('=', self)
        mod_button = QtGui.QPushButton('%', self)

        #Organize buttons on screen

        zero.setGeometry(40, 240, 81, 27)
        one.setGeometry(40, 190, 31, 27)
        four.setGeometry(40, 140, 31, 27)
        seven.setGeometry(40, 90, 31, 27)
        two.setGeometry(90, 190, 31, 27)
        five.setGeometry(90, 140, 31, 27)
        eight.setGeometry(90, 90, 31, 27)
        square_button.setGeometry(140, 240, 31, 27)
        three.setGeometry(140, 190, 31, 27)
        six.setGeometry(140, 140, 31, 27)
        nine.setGeometry(140, 90, 31, 27)
        equals_button.setGeometry(190, 240, 31, 27)
        multiply_button.setGeometry(190, 190, 31, 27)
        add_button.setGeometry(190, 140, 31, 27)
        mod_button.setGeometry(240, 240, 31, 27)
        divide_button.setGeometry(240, 190, 31, 27)
        subtract_button.setGeometry(240, 140, 31, 27)
        clear_button.setGeometry(190, 90, 81, 27)

        #Handle certain functions

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]
        calculations = [add_button, subtract_button, multiply_button, divide_button, square_button, equals_button, mod_button]

        for x in nums:
            x.setStyleSheet("color:blue;")
            x.clicked.connect(self.Numbers)

        for x in calculations:
            x.setStyleSheet("color:red;")
            x.clicked.connect(self.Calculations)


        #Handle actions when buttons are clicked
        square_button.clicked.connect(self.Squared)
        equals_button.clicked.connect(self.Equal)
        clear_button.clicked.connect(self.Clear)

        self.show()

    def Numbers(self):
        global num
        global second_num
        global var

        sender = self.sender()
        second_num = int(sender.text())
        set_num = str(second_num)

        if var == False:
            self.line_edit.setText(self.line_edit.text() + set_num)
        else:
            self.line_edit.setText(set_num)
            var = False

    def Equal(self):
        global num
        global second_num
        global sumX
        global operator
        global var
        global sum_it

        sum_it = 0

        second_num = self.line_edit.text()

        print(num)
        print(second_num)
        print(operator)

        if operator == "+":
            sumX = float(num) + float(second_num)
        elif operator == "-":
            sumX = float(num) - float(second_num)
        elif operator == "x":
            sumX = float(num) * float(second_num)
        elif operator == "/":
            sumX = float(num) / float(second_num)
        self.line_edit.setText(str(sumX))
        var = True

    def Calculations(self):
        global num
        global var
        global operator
        global sum_it

        sum_it += 1
        if sum_it > 1:
            self.Equal()

        num = self.line_edit.text()
        sender = self.sender()
        operator = sender.text()
        var = True

    def Squared(self):
        global num

        num = float(self.line_edit.text())
        square = num ** 2

        self.line_edit.setText(str(square))

    def Clear(self):
        global second_num
        global sumX
        global operator
        global num

        self.line_edit.clear()
        second_num = 0.0
        sumX = 0.0
        operator = ""
        num = 0.0

def main():

        app = QtGui.QApplication(sys.argv)
        main = Calculator()
        main.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
        main()
