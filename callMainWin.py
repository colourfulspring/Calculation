import sys
import random
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MainWin import *

class MyMainWindow(QMainWindow,  Ui_MainWindow):
    number = 300
    numRange = 100
    have_remainder = False
    first_num = []
    second_num = []
    answer = []
    operator_list = []
    reminder_list = []
    flag = False
    first = True
    
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.numberLineEdit.editingFinished.connect(self.setNumber)
        self.rangeLineEdit.editingFinished.connect(self.setRange)
        self.checkBox.stateChanged.connect(self.setReminder)
        self.getQuestionButton.clicked.connect(self.produceQuestion)
        self.getAnswerButton.clicked.connect(self.writeAnswer)
        self.exportQuestionButton.clicked.connect(self.exportQuestion)
        self.exportAnswerButton.clicked.connect(self.exportAnswer)
        
    def __checkNumber(self, str):
        lenNum = len(str)
        if lenNum == 0:
            return -2
        for i in range(0,  lenNum):
            if str[i:i+1] <"0" or str[i:i+1] >"9":
                return -1
        return 0
        
    def setNumber(self):
        t = self.__checkNumber(self.numberLineEdit.text())
        if  t== 0:
            if(int(self.numberLineEdit.text()) > 1000):
                self.__msg("警告", "一次作业超过1000题了，孩子们需要减负")
                self.numberLineEdit.setText("300")
            else:
                self.number = int(self.numberLineEdit.text())
                self.flag = False
        elif t == -1:
            self.__msg("警告", "请不要输入非数字字符")
            self.numberLineEdit.setText("300")
        else:
            self.__msg("警告", "出题数未输入")
            self.numberLineEdit.setText("300")
    
    def __msg(self,  title, message):
        QMessageBox.warning(self, title, message, QMessageBox.Ok)
    
    def setRange(self):
        t = self.__checkNumber(self.rangeLineEdit.text())
        if t == 0 :
            if(int(self.rangeLineEdit.text()) > 1000):
                self.__msg("警告", "数字太大了，孩子们会觉得题目很难")
                self.rangeLineEdit.setText("100")
            else:
                self.numRange = int(self.rangeLineEdit.text())
                self.flag = False
        elif t == -1:
            self.__msg("警告", "请不要输入非数字字符")
            self.rangeLineEdit.setText("100")
        else:
            self.__msg("警告", "运算数范围未输入")
            self.rangeLineEdit.setText("100")
    
    def setReminder(self):
        self.have_remainder = self.checkBox.isChecked()
        self.flag = False
    
    def produceQuestion(self):
        if self.__checkNumber(self.rangeLineEdit.text()) == 0:
            if self.__checkNumber(self.numberLineEdit.text()) == 0 :
                self.first_num.clear()
                self.second_num.clear()
                self.answer.clear()
                self.operator_list.clear()
                self.questionTextEdit.clear()
                self.answerTextEdit.clear()
                if self.have_remainder:
                    self.reminder_list.clear()
                for i in range(0, self.number):
                    temp = random.randint(1, 4)
                    if temp == 1:
                        self.first_num.append(random.randint(0, self.numRange))
                        self.second_num.append(random.randint(0, self.numRange))
                        self.operator_list.append("+")
                        self.answer.append(self.first_num[i] + self.second_num[i])
                        self.reminder_list.append(-1);
                    elif temp == 2:
                        self.answer.append(random.randint(0, self.numRange))
                        self.second_num.append(random.randint(0, self.numRange))
                        self.operator_list.append("-")
                        self.first_num.append(self.answer[i] + self.second_num[i]);
                        self.reminder_list.append(-1)
                    elif temp == 3:
                        self.first_num.append(random.randint(0, self.numRange))
                        self.second_num.append(random.randint(0, self.numRange))
                        self.operator_list.append("*")
                        self.answer.append(self.first_num[i] * self.second_num[i])
                        self.reminder_list.append(-1)
                    else:
                        self.operator_list.append("÷")
                        if self.have_remainder :
                            self.first_num.append(random.randint(0, self.numRange))
                            self.second_num.append(random.randint(1, self.numRange))
                            self.answer.append(self.first_num[i] // self.second_num[i])
                            self.reminder_list.append(self.first_num[i] % self.second_num[i])
                        else:
                            self.second_num.append(random.randint(1, self.numRange // 10))
                            self.answer.append(random.randint(1, self.numRange //self.second_num[i]));
                            self.first_num.append(self.answer[i] * self.second_num[i])
                            self.reminder_list.append(-1)
                    self.questionTextEdit.append(str(i+1)+"  "+str(self.first_num[i])+self.operator_list[i]+str(self.second_num[i])+"=")
                self.flag = True
                self.first = False
    
    def writeAnswer(self):
        if(not self.flag):
            if self.first :
                self.__msg("警告", "请先单击出题按钮")
            else:
                self.__msg("警告", "您刚才编辑了属性，请再次单击出题按钮")
        else:
            self.answerTextEdit.clear()
            for i in range(0,  self.number):
                if self.reminder_list[i] == -1:
                    self.answerTextEdit.append(str(i+1)+"  "+str(self.answer[i]))
                else:
                    self.answerTextEdit.append(str(i+1)+"  "+str(self.answer[i])+"······"+str(self.reminder_list[i]))

    def createFile(self, str):
        fname =QFileDialog.getSaveFileName(self, "导出题目文件", "c:\\", "Normal Text Files (*.txt)")
        try:
            f = open(fname[0], "w")
        except FileNotFoundError:
            f = ""
        if(f != ""):
            f.write(str)
            f.close
        
    def exportQuestion(self):
        if(self.questionTextEdit.toPlainText() != ""):
            self.createFile(self.questionTextEdit.toPlainText())
        else:
            self.__msg("警告", "现在列表框中没有题目！请先单击出题按钮")
            
    def exportAnswer(self):
        if(self.answerTextEdit.toPlainText() != ""):
            self.createFile(self.answerTextEdit.toPlainText())
        else:
            self.__msg("警告", "现在列表框中没有答案！请先单击显示答案按钮")

if __name__=="__main__" :
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
