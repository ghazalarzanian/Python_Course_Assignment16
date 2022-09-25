import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class calculator(QMainWindow):
   def __init__(self):
      super().__init__()
      loader = QUiLoader()
      self.ui=loader.load('Cal.ui',None)
      self.ui.show()
      self.temp=''
      self.ui.equal.clicked.connect(self.equal)
      self.ui.btn_1.clicked.connect(self.fun1)
      self.ui.btn_2.clicked.connect(self.fun2)
      self.ui.btn_3.clicked.connect(self.fun3)
      self.ui.btn_4.clicked.connect(self.fun4)
      self.ui.btn_5.clicked.connect(self.fun5)
      self.ui.btn_6.clicked.connect(self.fun6)
      self.ui.btn_7.clicked.connect(self.fun7)
      self.ui.btn_8.clicked.connect(self.fun8)
      self.ui.btn_9.clicked.connect(self.fun9)
      self.ui.btn_0.clicked.connect(self.fun0)
      self.ui.btn_dot.clicked.connect(self.dot)
      self.ui.ac.clicked.connect(self.ac)
      self.ui.sum.clicked.connect(self.sum)
      self.ui.minus.clicked.connect(self.minus)
      self.ui.mul.clicked.connect(self.mul)
      self.ui.division.clicked.connect(self.division)
      self.ui.percent.clicked.connect(self.percent)
      self.ui.sqrt.clicked.connect(self.sqrt)
      self.ui.log.clicked.connect(self.log)
      self.ui.cos.clicked.connect(self.cos)
      self.ui.sin.clicked.connect(self.sin)
      self.ui.tan.clicked.connect(self.tan)
      self.ui.cot.clicked.connect(self.cot)
      self.ui.sign.clicked.connect(self.sign)
   def fun1(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'1')
   def fun2(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'2')
   def fun3(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'3')
   def fun4(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'4')
   def fun5(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'5')
   def fun6(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'6')
   def fun7(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'7')
   def fun8(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'8')
   def fun9(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'9')
   def fun0(self):
      self.ui.textbox.setText(self.ui.textbox.text()+'0')
   def dot(self):
      text=self.ui.textbox.text()
      if text[-1]!='.':
         self.ui.textbox.setText(self.ui.textbox.text()+'.')
   def ac(self):
      self.ui.textbox.setText('')
   def sum(self):
      self.num1=float(self.ui.textbox.text())
      self.ui.textbox.setText('')
      self.temp='+'
   def minus(self):
      self.num1=float(self.ui.textbox.text())
      self.ui.textbox.setText('')
      self.temp='-'
   def mul(self):
      self.num1=float(self.ui.textbox.text())
      self.ui.textbox.setText('')
      self.temp='*'
   def log(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.log(self.num1)
      self.ui.textbox.setText(str(self.num1))
   def sqrt(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.sqrt(self.num1)
      self.ui.textbox.setText(str(self.num1))
   def division(self):
      self.num1=float(self.ui.textbox.text())
      self.ui.textbox.setText('')
      self.temp='/'
   def cos(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.cos(math.radians(self.num1))
      self.ui.textbox.setText(str(self.num1))
   def sin(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.sin(math.radians(self.num1))
      self.ui.textbox.setText(str(self.num1))
   def cot(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.cot(math.radians(self.num1))
      self.ui.textbox.setText(str(self.num1))
   def tan(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=math.tan(math.radians(self.num1))
      self.ui.textbox.setText(str(self.num1))
   def percent(self):
      self.num1=float(self.ui.textbox.text())
      self.num1=self.num1*0.01
      self.ui.textbox.setText(str(self.num1))
   def sign(self):
      self.num1=float(self.ui.textbox.text())*-1
      self.ui.textbox.setText(str(self.num1))
   def equal(self):
      self.num2=float(self.ui.textbox.text())
      if self.temp=='+':
         result=float(self.num1+self.num2)
      if self.temp=='-':
         result=float(self.num1-self.num2)
      if self.temp=='*':
         result=float(self.num1*self.num2)
      if self.temp=='/':
         result=float(self.num1/self.num2)
      self.ui.textbox.setText(str(result))
#chon yel application mitoune chand to safhe dashte bashe 
#pas Application yek Shei hast Harsafe yek Shei
#pyside6-designer
#str ro mishe setText konim
app = QApplication([])
window=calculator()
app.exec()