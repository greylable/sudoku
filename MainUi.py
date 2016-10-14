from PyQt4 import QtGui
import sys

import MainUiDesign

class MainApp(QtGui.QMainWindow, MainUiDesign.Ui_MainWindow):
	playerTurn = 1

	def __init__(self, parent=None):
		super(MainApp, self).__init__(parent)
		self.setupUi(self)

		self.confirm_button.clicked.connect(self.confirm_clicked)

	def return_zero_if_empty(self, cell_text):
		if(cell_text == ""):
			return "0"
		else:
			return cell_text

	def confirm_clicked(self):
		result_string = ""

		result_string = result_string + self.return_zero_if_empty(self.cell_1_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_1_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_2_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_2_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_3_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_3_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_4_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_4_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_5_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_5_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_6_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_6_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_7_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_7_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_8_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_8_9.text())

		result_string = result_string + self.return_zero_if_empty(self.cell_9_1.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_2.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_3.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_4.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_5.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_6.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_7.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_8.text())
		result_string = result_string + self.return_zero_if_empty(self.cell_9_9.text())

		print result_string

def main():
	app = QtGui.QApplication(sys.argv)
	form = MainApp()
	form.show()
	app.exec_()



if __name__ == '__main__':
	main()