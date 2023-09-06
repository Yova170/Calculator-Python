import sys
import re
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

# Main class
class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.show()
        ui, _ = uic.loadUiType("calc.ui")
        self.ui = ui()
        self.ui.setupUi(self)
        self.show()
        self.setWindowIcon(QIcon('icono.ico'))
        self.ui.screen.textChanged.connect(self.validate_text)
        self.ui.screen.setMaxLength(13)

        #Clicked action button (number)
        self.ui.number1.clicked.connect(self.n1)
        self.ui.number2.clicked.connect(self.n2)
        self.ui.number3.clicked.connect(self.n3)
        self.ui.number4.clicked.connect(self.n4)
        self.ui.number5.clicked.connect(self.n5)
        self.ui.number6.clicked.connect(self.n6)
        self.ui.number7.clicked.connect(self.n7)
        self.ui.number8.clicked.connect(self.n8)
        self.ui.number9.clicked.connect(self.n9)
        self.ui.number0.clicked.connect(self.n0)
        self.ui.np.clicked.connect(self.np)

         #Clicked action button (sign)
        self.ui.igual.clicked.connect(self.res)
        self.ui.suma.clicked.connect(self.sum)
        self.ui.resta.clicked.connect(self.rest)
        self.ui.multiplicacion.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.ui.porciento.clicked.connect(self.porc)

    #Action sign button
    def sum(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + '+')
    
    def rest(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + '-')

    def mul(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + '*')

    def div(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + '/')

    def porc(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + '%')



    #Action numbers button
    def n2(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "2")
    
    def n3(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "3")
    
    def n4(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "4")
    
    def n5(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "5")
    
    def n6(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "6")
    
    def n7(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "7")
    
    def n8(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "8")
    
    def n9(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "9")
    
    def n0(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "0")
    
    def n1(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "1")

    def np(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + ".")

    #Results
    def res(self):
        equation = self.ui.screen.text()
        try:
            ans = eval(equation)
            self.ui.screen.setText(str(ans))
        except:
            self.ui.screen.setText("Error Syntax")


    #Validate Only number and signs predefined
    def validate_text(self):
        text = self.ui.screen.text()
        valid = True
        for char in text:
            if not re.match(r"^[0-9.+-.*./.%. . .=]+$", char):
                valid = False
                break
        if not valid:
            text = text.replace(char, "")
            self.ui.screen.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_()) 

#In the file "calc.iu" is all the data of the graphical interface, it was developed with PyQt5. If you have the extension you can make the changes you want.