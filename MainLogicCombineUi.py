# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import solver_oop
import UA_oop_2

import MainUi


class MainApp(QtGui.QMainWindow, MainUi.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

        self.setupUi(self)

        self.frame.setStyleSheet("QFrame { background-color: #f2f2f2}")

        self.pushButton_puzzle_to_grid.clicked.connect(self.initial_puz_set_cell)
        self.pushButton_grid_to_puzzle.clicked.connect(self.cell_set_initial_puz)
        self.pushButton_solution_to_grid.clicked.connect(self.solution_set_cell)
        self.pushButton_grid_to_solution.clicked.connect(self.cell_set_solution)

        self.pushButton_solve.clicked.connect(self.solving_puzzle)
        self.pushButton_clear_all.clicked.connect(self.delete_all_cells)

        self.pushButton_UA_prev_4.hide()
        self.pushButton_UA_next_4.hide()
        self.label_3_UA_set_no_4.hide()
        self.pushButton_UA_prev_6.hide()
        self.pushButton_UA_next_6.hide()
        self.label_3_UA_set_no_6.hide()

        self.pushButton_multiple_solutions_prev.hide() ##
        self.pushButton_multiple_solutions_next.hide() ##
        self.label_multiple_solutions.hide()            ##

        self.lineEdit_multiple_solution.hide()
        self.label_multiple_solution_contain.hide()

        self.comboBox_UA_size.addItems(["UA Size", "4", "6"])

        #self.connect(self.comboBox_UA_size,QtCore.SIGNAL("activated(const QString&)"),self.magic_try)
        self.connect(self.comboBox_UA_size,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.magic_try)

        self.pushButton_UA_next_4.clicked.connect(self.counter_next_4)
        self.pushButton_UA_prev_4.clicked.connect(self.counter_prev_4)

        self.pushButton_UA_next_6.clicked.connect(self.counter_next_6)
        self.pushButton_UA_prev_6.clicked.connect(self.counter_prev_6)

        ###self.pushButton_multiple_solutions_next.clicked.connect(self.counter_sol_next)
        ###self.pushButton_multiple_solutions_prev.clicked.connect(self.counter_sol_prev)

    def return_zero_if_empty(self, cell_text):
        if cell_text == "":
            return "0"
        else:
            return cell_text

    def generate_keys(self,cell_definition,cell_definition1):
    # "Cross product of elements in A and elements in B. 81 items in a list"
        return [a+b for a in cell_definition for b in cell_definition1]

    def delete_all_cells(self):
        self.lineEdit_multiple_solution.hide()
        self.label_multiple_solution_contain.hide()
        self.pushButton_multiple_solutions_next.hide()  ##
        self.pushButton_multiple_solutions_prev.hide()  ##
        self.label_multiple_solutions.hide()            ##
        self.cell_0_0.setText("")
        self.cell_0_1.setText("")
        self.cell_0_2.setText("")
        self.cell_0_3.setText("")
        self.cell_0_4.setText("")
        self.cell_0_5.setText("")
        self.cell_0_6.setText("")
        self.cell_0_7.setText("")
        self.cell_0_8.setText("")

        self.cell_1_0.setText("")
        self.cell_1_1.setText("")
        self.cell_1_2.setText("")
        self.cell_1_3.setText("")
        self.cell_1_4.setText("")
        self.cell_1_5.setText("")
        self.cell_1_6.setText("")
        self.cell_1_7.setText("")
        self.cell_1_8.setText("")

        self.cell_2_0.setText("")
        self.cell_2_1.setText("")
        self.cell_2_2.setText("")
        self.cell_2_3.setText("")
        self.cell_2_4.setText("")
        self.cell_2_5.setText("")
        self.cell_2_6.setText("")
        self.cell_2_7.setText("")
        self.cell_2_8.setText("")

        self.cell_3_0.setText("")
        self.cell_3_1.setText("")
        self.cell_3_2.setText("")
        self.cell_3_3.setText("")
        self.cell_3_4.setText("")
        self.cell_3_5.setText("")
        self.cell_3_6.setText("")
        self.cell_3_7.setText("")
        self.cell_3_8.setText("")

        self.cell_4_0.setText("")
        self.cell_4_1.setText("")
        self.cell_4_2.setText("")
        self.cell_4_3.setText("")
        self.cell_4_4.setText("")
        self.cell_4_5.setText("")
        self.cell_4_6.setText("")
        self.cell_4_7.setText("")
        self.cell_4_8.setText("")

        self.cell_5_0.setText("")
        self.cell_5_1.setText("")
        self.cell_5_2.setText("")
        self.cell_5_3.setText("")
        self.cell_5_4.setText("")
        self.cell_5_5.setText("")
        self.cell_5_6.setText("")
        self.cell_5_7.setText("")
        self.cell_5_8.setText("")

        self.cell_6_0.setText("")
        self.cell_6_1.setText("")
        self.cell_6_2.setText("")
        self.cell_6_3.setText("")
        self.cell_6_4.setText("")
        self.cell_6_5.setText("")
        self.cell_6_6.setText("")
        self.cell_6_7.setText("")
        self.cell_6_8.setText("")

        self.cell_7_0.setText("")
        self.cell_7_1.setText("")
        self.cell_7_2.setText("")
        self.cell_7_3.setText("")
        self.cell_7_4.setText("")
        self.cell_7_5.setText("")
        self.cell_7_6.setText("")
        self.cell_7_7.setText("")
        self.cell_7_8.setText("")

        self.cell_8_0.setText("")
        self.cell_8_1.setText("")
        self.cell_8_2.setText("")
        self.cell_8_3.setText("")
        self.cell_8_4.setText("")
        self.cell_8_5.setText("")
        self.cell_8_6.setText("")
        self.cell_8_7.setText("")
        self.cell_8_8.setText("")

        self.cell_0_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_0_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_1_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_1_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_2_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_2_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_3_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_3_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_4_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_4_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_5_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_5_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_6_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_6_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_7_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_7_8.setStyleSheet("QLineEdit { background-color: white}")

        self.cell_8_0.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_1.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_2.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_3.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_4.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_5.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_6.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_7.setStyleSheet("QLineEdit { background-color: white}")
        self.cell_8_8.setStyleSheet("QLineEdit { background-color: white}")

    def cell_set_initial_puz(self):
        result_string = []

        result_string = result_string + [self.return_zero_if_empty(self.cell_0_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_1_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_2_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_3_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_4_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_5_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_6_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_7_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_8_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_8.text())]

        result_string1 = ''.join(str(v) for v in result_string)
        if result_string1 == '':
            return
        self.lineEdit_initial_puzzle.setText(result_string1)

    def initial_puz_set_cell(self):

        puzzle = []
        puzzle1 = list(self.lineEdit_initial_puzzle.text())

        if puzzle1 == []:
            return
        for i in puzzle1:
            if i == '0':
                i = ""
            puzzle = puzzle + [i]

        self.cell_0_0.setText(puzzle[0])
        self.cell_0_1.setText(puzzle[1])
        self.cell_0_2.setText(puzzle[2])
        self.cell_0_3.setText(puzzle[3])
        self.cell_0_4.setText(puzzle[4])
        self.cell_0_5.setText(puzzle[5])
        self.cell_0_6.setText(puzzle[6])
        self.cell_0_7.setText(puzzle[7])
        self.cell_0_8.setText(puzzle[8])

        self.cell_1_0.setText(puzzle[9])
        self.cell_1_1.setText(puzzle[10])
        self.cell_1_2.setText(puzzle[11])
        self.cell_1_3.setText(puzzle[12])
        self.cell_1_4.setText(puzzle[13])
        self.cell_1_5.setText(puzzle[14])
        self.cell_1_6.setText(puzzle[15])
        self.cell_1_7.setText(puzzle[16])
        self.cell_1_8.setText(puzzle[17])

        self.cell_2_0.setText(puzzle[18])
        self.cell_2_1.setText(puzzle[19])
        self.cell_2_2.setText(puzzle[20])
        self.cell_2_3.setText(puzzle[21])
        self.cell_2_4.setText(puzzle[22])
        self.cell_2_5.setText(puzzle[23])
        self.cell_2_6.setText(puzzle[24])
        self.cell_2_7.setText(puzzle[25])
        self.cell_2_8.setText(puzzle[26])

        self.cell_3_0.setText(puzzle[27])
        self.cell_3_1.setText(puzzle[28])
        self.cell_3_2.setText(puzzle[29])
        self.cell_3_3.setText(puzzle[30])
        self.cell_3_4.setText(puzzle[31])
        self.cell_3_5.setText(puzzle[32])
        self.cell_3_6.setText(puzzle[33])
        self.cell_3_7.setText(puzzle[34])
        self.cell_3_8.setText(puzzle[35])

        self.cell_4_0.setText(puzzle[36])
        self.cell_4_1.setText(puzzle[37])
        self.cell_4_2.setText(puzzle[38])
        self.cell_4_3.setText(puzzle[39])
        self.cell_4_4.setText(puzzle[40])
        self.cell_4_5.setText(puzzle[41])
        self.cell_4_6.setText(puzzle[42])
        self.cell_4_7.setText(puzzle[43])
        self.cell_4_8.setText(puzzle[44])

        self.cell_5_0.setText(puzzle[45])
        self.cell_5_1.setText(puzzle[46])
        self.cell_5_2.setText(puzzle[47])
        self.cell_5_3.setText(puzzle[48])
        self.cell_5_4.setText(puzzle[49])
        self.cell_5_5.setText(puzzle[50])
        self.cell_5_6.setText(puzzle[51])
        self.cell_5_7.setText(puzzle[52])
        self.cell_5_8.setText(puzzle[53])

        self.cell_6_0.setText(puzzle[54])
        self.cell_6_1.setText(puzzle[55])
        self.cell_6_2.setText(puzzle[56])
        self.cell_6_3.setText(puzzle[57])
        self.cell_6_4.setText(puzzle[58])
        self.cell_6_5.setText(puzzle[59])
        self.cell_6_6.setText(puzzle[60])
        self.cell_6_7.setText(puzzle[61])
        self.cell_6_8.setText(puzzle[62])

        self.cell_7_0.setText(puzzle[63])
        self.cell_7_1.setText(puzzle[64])
        self.cell_7_2.setText(puzzle[65])
        self.cell_7_3.setText(puzzle[66])
        self.cell_7_4.setText(puzzle[67])
        self.cell_7_5.setText(puzzle[68])
        self.cell_7_6.setText(puzzle[69])
        self.cell_7_7.setText(puzzle[70])
        self.cell_7_8.setText(puzzle[71])

        self.cell_8_0.setText(puzzle[72])
        self.cell_8_1.setText(puzzle[73])
        self.cell_8_2.setText(puzzle[74])
        self.cell_8_3.setText(puzzle[75])
        self.cell_8_4.setText(puzzle[76])
        self.cell_8_5.setText(puzzle[77])
        self.cell_8_6.setText(puzzle[78])
        self.cell_8_7.setText(puzzle[79])
        self.cell_8_8.setText(puzzle[80])

        return self.lineEdit_initial_puzzle.text()

    def cell_set_solution(self):
        result_string = []

        result_string = result_string + [self.return_zero_if_empty(self.cell_0_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_0_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_1_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_1_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_2_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_2_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_3_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_3_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_4_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_4_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_5_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_5_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_6_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_6_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_7_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_7_8.text())]

        result_string = result_string + [self.return_zero_if_empty(self.cell_8_0.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_1.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_2.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_3.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_4.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_5.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_6.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_7.text())]
        result_string = result_string + [self.return_zero_if_empty(self.cell_8_8.text())]

        result_string1 = ''.join(str(v) for v in result_string)
        if result_string1 == '':
            return
        self.lineEdit_solved_puzzle.setText(result_string1)

    def solution_set_cell(self):

        puzzle = []
        puzzle1 = list(self.lineEdit_solved_puzzle.text())

        if puzzle1 == []:
            return
        for i in puzzle1:
            if i == '0':
                i = ""
            puzzle = puzzle + [i]

        self.cell_0_0.setText(puzzle[0])
        self.cell_0_1.setText(puzzle[1])
        self.cell_0_2.setText(puzzle[2])
        self.cell_0_3.setText(puzzle[3])
        self.cell_0_4.setText(puzzle[4])
        self.cell_0_5.setText(puzzle[5])
        self.cell_0_6.setText(puzzle[6])
        self.cell_0_7.setText(puzzle[7])
        self.cell_0_8.setText(puzzle[8])

        self.cell_1_0.setText(puzzle[9])
        self.cell_1_1.setText(puzzle[10])
        self.cell_1_2.setText(puzzle[11])
        self.cell_1_3.setText(puzzle[12])
        self.cell_1_4.setText(puzzle[13])
        self.cell_1_5.setText(puzzle[14])
        self.cell_1_6.setText(puzzle[15])
        self.cell_1_7.setText(puzzle[16])
        self.cell_1_8.setText(puzzle[17])

        self.cell_2_0.setText(puzzle[18])
        self.cell_2_1.setText(puzzle[19])
        self.cell_2_2.setText(puzzle[20])
        self.cell_2_3.setText(puzzle[21])
        self.cell_2_4.setText(puzzle[22])
        self.cell_2_5.setText(puzzle[23])
        self.cell_2_6.setText(puzzle[24])
        self.cell_2_7.setText(puzzle[25])
        self.cell_2_8.setText(puzzle[26])

        self.cell_3_0.setText(puzzle[27])
        self.cell_3_1.setText(puzzle[28])
        self.cell_3_2.setText(puzzle[29])
        self.cell_3_3.setText(puzzle[30])
        self.cell_3_4.setText(puzzle[31])
        self.cell_3_5.setText(puzzle[32])
        self.cell_3_6.setText(puzzle[33])
        self.cell_3_7.setText(puzzle[34])
        self.cell_3_8.setText(puzzle[35])

        self.cell_4_0.setText(puzzle[36])
        self.cell_4_1.setText(puzzle[37])
        self.cell_4_2.setText(puzzle[38])
        self.cell_4_3.setText(puzzle[39])
        self.cell_4_4.setText(puzzle[40])
        self.cell_4_5.setText(puzzle[41])
        self.cell_4_6.setText(puzzle[42])
        self.cell_4_7.setText(puzzle[43])
        self.cell_4_8.setText(puzzle[44])

        self.cell_5_0.setText(puzzle[45])
        self.cell_5_1.setText(puzzle[46])
        self.cell_5_2.setText(puzzle[47])
        self.cell_5_3.setText(puzzle[48])
        self.cell_5_4.setText(puzzle[49])
        self.cell_5_5.setText(puzzle[50])
        self.cell_5_6.setText(puzzle[51])
        self.cell_5_7.setText(puzzle[52])
        self.cell_5_8.setText(puzzle[53])

        self.cell_6_0.setText(puzzle[54])
        self.cell_6_1.setText(puzzle[55])
        self.cell_6_2.setText(puzzle[56])
        self.cell_6_3.setText(puzzle[57])
        self.cell_6_4.setText(puzzle[58])
        self.cell_6_5.setText(puzzle[59])
        self.cell_6_6.setText(puzzle[60])
        self.cell_6_7.setText(puzzle[61])
        self.cell_6_8.setText(puzzle[62])

        self.cell_7_0.setText(puzzle[63])
        self.cell_7_1.setText(puzzle[64])
        self.cell_7_2.setText(puzzle[65])
        self.cell_7_3.setText(puzzle[66])
        self.cell_7_4.setText(puzzle[67])
        self.cell_7_5.setText(puzzle[68])
        self.cell_7_6.setText(puzzle[69])
        self.cell_7_7.setText(puzzle[70])
        self.cell_7_8.setText(puzzle[71])

        self.cell_8_0.setText(puzzle[72])
        self.cell_8_1.setText(puzzle[73])
        self.cell_8_2.setText(puzzle[74])
        self.cell_8_3.setText(puzzle[75])
        self.cell_8_4.setText(puzzle[76])
        self.cell_8_5.setText(puzzle[77])
        self.cell_8_6.setText(puzzle[78])
        self.cell_8_7.setText(puzzle[79])
        self.cell_8_8.setText(puzzle[80])

        return self.lineEdit_initial_puzzle.text()

    def solving_puzzle(self):
        self.pushButton_UA_prev_4.hide()
        self.pushButton_UA_next_4.hide()
        self.label_3_UA_set_no_4.hide()
        self.pushButton_UA_prev_6.hide()
        self.pushButton_UA_next_6.hide()
        self.label_3_UA_set_no_6.hide()
        self.comboBox_UA_size.setCurrentIndex(0)
        self.lineEdit_multiple_solution.hide()
        self.label_multiple_solution_contain.hide()
        self.count_sol = 1
        choices = [1,2,3,4,5,6,7,8,9]
        puzzle = str(self.lineEdit_initial_puzzle.text())
        if puzzle == '' or puzzle == '000000000000000000000000000000000000000000000000000000000000000000000000000000000':
            return
        else:
            result = solver_oop.Solver(3,choices,puzzle).trans_str(puzzle)

            if len(result) == 1:
               #self.pushButton_multiple_solutions_next.show()
               #self.pushButton_multiple_solutions_prev.show()
               #self.label_multiple_solutions.show()
               #self.pushButton_multiple_solutions_next.setEnabled(False)
               #self.pushButton_multiple_solutions_prev.setEnabled(False)
               self.lineEdit_solved_puzzle.setText(result[0])
               self.cell_0_0.setText(result[0][0])
               self.cell_0_1.setText(result[0][1])
               self.cell_0_2.setText(result[0][2])
               self.cell_0_3.setText(result[0][3])
               self.cell_0_4.setText(result[0][4])
               self.cell_0_5.setText(result[0][5])
               self.cell_0_6.setText(result[0][6])
               self.cell_0_7.setText(result[0][7])
               self.cell_0_8.setText(result[0][8])

               self.cell_1_0.setText(result[0][9])
               self.cell_1_1.setText(result[0][10])
               self.cell_1_2.setText(result[0][11])
               self.cell_1_3.setText(result[0][12])
               self.cell_1_4.setText(result[0][13])
               self.cell_1_5.setText(result[0][14])
               self.cell_1_6.setText(result[0][15])
               self.cell_1_7.setText(result[0][16])
               self.cell_1_8.setText(result[0][17])

               self.cell_2_0.setText(result[0][18])
               self.cell_2_1.setText(result[0][19])
               self.cell_2_2.setText(result[0][20])
               self.cell_2_3.setText(result[0][21])
               self.cell_2_4.setText(result[0][22])
               self.cell_2_5.setText(result[0][23])
               self.cell_2_6.setText(result[0][24])
               self.cell_2_7.setText(result[0][25])
               self.cell_2_8.setText(result[0][26])

               self.cell_3_0.setText(result[0][27])
               self.cell_3_1.setText(result[0][28])
               self.cell_3_2.setText(result[0][29])
               self.cell_3_3.setText(result[0][30])
               self.cell_3_4.setText(result[0][31])
               self.cell_3_5.setText(result[0][32])
               self.cell_3_6.setText(result[0][33])
               self.cell_3_7.setText(result[0][34])
               self.cell_3_8.setText(result[0][35])

               self.cell_4_0.setText(result[0][36])
               self.cell_4_1.setText(result[0][37])
               self.cell_4_2.setText(result[0][38])
               self.cell_4_3.setText(result[0][39])
               self.cell_4_4.setText(result[0][40])
               self.cell_4_5.setText(result[0][41])
               self.cell_4_6.setText(result[0][42])
               self.cell_4_7.setText(result[0][43])
               self.cell_4_8.setText(result[0][44])

               self.cell_5_0.setText(result[0][45])
               self.cell_5_1.setText(result[0][46])
               self.cell_5_2.setText(result[0][47])
               self.cell_5_3.setText(result[0][48])
               self.cell_5_4.setText(result[0][49])
               self.cell_5_5.setText(result[0][50])
               self.cell_5_6.setText(result[0][51])
               self.cell_5_7.setText(result[0][52])
               self.cell_5_8.setText(result[0][53])

               self.cell_6_0.setText(result[0][54])
               self.cell_6_1.setText(result[0][55])
               self.cell_6_2.setText(result[0][56])
               self.cell_6_3.setText(result[0][57])
               self.cell_6_4.setText(result[0][58])
               self.cell_6_5.setText(result[0][59])
               self.cell_6_6.setText(result[0][60])
               self.cell_6_7.setText(result[0][61])
               self.cell_6_8.setText(result[0][62])

               self.cell_7_0.setText(result[0][63])
               self.cell_7_1.setText(result[0][64])
               self.cell_7_2.setText(result[0][65])
               self.cell_7_3.setText(result[0][66])
               self.cell_7_4.setText(result[0][67])
               self.cell_7_5.setText(result[0][68])
               self.cell_7_6.setText(result[0][69])
               self.cell_7_7.setText(result[0][70])
               self.cell_7_8.setText(result[0][71])

               self.cell_8_0.setText(result[0][72])
               self.cell_8_1.setText(result[0][73])
               self.cell_8_2.setText(result[0][74])
               self.cell_8_3.setText(result[0][75])
               self.cell_8_4.setText(result[0][76])
               self.cell_8_5.setText(result[0][77])
               self.cell_8_6.setText(result[0][78])
               self.cell_8_7.setText(result[0][79])
               self.cell_8_8.setText(result[0][80])

               #self.label_multiple_solutions.setText(str(self.count_sol)+ ' of ' + str(len(result)))

            if len(result) > 1:
                self.lineEdit_multiple_solution.show()
                self.label_multiple_solution_contain.show()
                self.lineEdit_multiple_solution.setText(str(result))
                self.label_multiple_solution_contain.setText(str(len(result))+' '+'Solutions')
                self.lineEdit_solved_puzzle.setText("")

                '''self.pushButton_multiple_solutions_next.show()
                self.pushButton_multiple_solutions_prev.show()
                self.label_multiple_solutions.show()

                if self.count_sol == 1:
                    self.pushButton_multiple_solutions_next.setEnabled(True)
                    self.lineEdit_solved_puzzle.setText(result[0])
                    self.cell_0_0.setText(result[0][0])
                    self.cell_0_1.setText(result[0][1])
                    self.cell_0_2.setText(result[0][2])
                    self.cell_0_3.setText(result[0][3])
                    self.cell_0_4.setText(result[0][4])
                    self.cell_0_5.setText(result[0][5])
                    self.cell_0_6.setText(result[0][6])
                    self.cell_0_7.setText(result[0][7])
                    self.cell_0_8.setText(result[0][8])

                    self.cell_1_0.setText(result[0][9])
                    self.cell_1_1.setText(result[0][10])
                    self.cell_1_2.setText(result[0][11])
                    self.cell_1_3.setText(result[0][12])
                    self.cell_1_4.setText(result[0][13])
                    self.cell_1_5.setText(result[0][14])
                    self.cell_1_6.setText(result[0][15])
                    self.cell_1_7.setText(result[0][16])
                    self.cell_1_8.setText(result[0][17])

                    self.cell_2_0.setText(result[0][18])
                    self.cell_2_1.setText(result[0][19])
                    self.cell_2_2.setText(result[0][20])
                    self.cell_2_3.setText(result[0][21])
                    self.cell_2_4.setText(result[0][22])
                    self.cell_2_5.setText(result[0][23])
                    self.cell_2_6.setText(result[0][24])
                    self.cell_2_7.setText(result[0][25])
                    self.cell_2_8.setText(result[0][26])

                    self.cell_3_0.setText(result[0][27])
                    self.cell_3_1.setText(result[0][28])
                    self.cell_3_2.setText(result[0][29])
                    self.cell_3_3.setText(result[0][30])
                    self.cell_3_4.setText(result[0][31])
                    self.cell_3_5.setText(result[0][32])
                    self.cell_3_6.setText(result[0][33])
                    self.cell_3_7.setText(result[0][34])
                    self.cell_3_8.setText(result[0][35])

                    self.cell_4_0.setText(result[0][36])
                    self.cell_4_1.setText(result[0][37])
                    self.cell_4_2.setText(result[0][38])
                    self.cell_4_3.setText(result[0][39])
                    self.cell_4_4.setText(result[0][40])
                    self.cell_4_5.setText(result[0][41])
                    self.cell_4_6.setText(result[0][42])
                    self.cell_4_7.setText(result[0][43])
                    self.cell_4_8.setText(result[0][44])

                    self.cell_5_0.setText(result[0][45])
                    self.cell_5_1.setText(result[0][46])
                    self.cell_5_2.setText(result[0][47])
                    self.cell_5_3.setText(result[0][48])
                    self.cell_5_4.setText(result[0][49])
                    self.cell_5_5.setText(result[0][50])
                    self.cell_5_6.setText(result[0][51])
                    self.cell_5_7.setText(result[0][52])
                    self.cell_5_8.setText(result[0][53])

                    self.cell_6_0.setText(result[0][54])
                    self.cell_6_1.setText(result[0][55])
                    self.cell_6_2.setText(result[0][56])
                    self.cell_6_3.setText(result[0][57])
                    self.cell_6_4.setText(result[0][58])
                    self.cell_6_5.setText(result[0][59])
                    self.cell_6_6.setText(result[0][60])
                    self.cell_6_7.setText(result[0][61])
                    self.cell_6_8.setText(result[0][62])

                    self.cell_7_0.setText(result[0][63])
                    self.cell_7_1.setText(result[0][64])
                    self.cell_7_2.setText(result[0][65])
                    self.cell_7_3.setText(result[0][66])
                    self.cell_7_4.setText(result[0][67])
                    self.cell_7_5.setText(result[0][68])
                    self.cell_7_6.setText(result[0][69])
                    self.cell_7_7.setText(result[0][70])
                    self.cell_7_8.setText(result[0][71])

                    self.cell_8_0.setText(result[0][72])
                    self.cell_8_1.setText(result[0][73])
                    self.cell_8_2.setText(result[0][74])
                    self.cell_8_3.setText(result[0][75])
                    self.cell_8_4.setText(result[0][76])
                    self.cell_8_5.setText(result[0][77])
                    self.cell_8_6.setText(result[0][78])
                    self.cell_8_7.setText(result[0][79])
                    self.cell_8_8.setText(result[0][80])

                    self.label_multiple_solutions.setText(str(self.count_sol)+ ' of ' + str(len(result)))

                self.pushButton_multiple_solutions_next.clicked.connect(lambda: self.sol_next_button(result))
                self.pushButton_multiple_solutions_prev.clicked.connect(lambda: self.sol_prev_button(result))
        #return self.lineEdit_solved_puzzle.text()'''

    ## Multiple Solution Prev/Next Buttons here
    '''def counter_sol_next(self):
        self.comboBox_UA_size.setCurrentIndex(0)
        self.count_sol += 1
    def counter_sol_prev(self):
        self.comboBox_UA_size.setCurrentIndex(0)
        if self.count_sol == 1:
            return
        else:
            self.count_sol -= 1

    def sol_prev_button(self,result):

        if self.count_sol == 1:
            self.pushButton_multiple_solutions_prev.setEnabled(False)
            self.pushButton_multiple_solutions_next.setEnabled(True)
            self.lineEdit_solved_puzzle.setText(result[0])
            self.cell_0_0.setText(result[0][0])
            self.cell_0_1.setText(result[0][1])
            self.cell_0_2.setText(result[0][2])
            self.cell_0_3.setText(result[0][3])
            self.cell_0_4.setText(result[0][4])
            self.cell_0_5.setText(result[0][5])
            self.cell_0_6.setText(result[0][6])
            self.cell_0_7.setText(result[0][7])
            self.cell_0_8.setText(result[0][8])

            self.cell_1_0.setText(result[0][9])
            self.cell_1_1.setText(result[0][10])
            self.cell_1_2.setText(result[0][11])
            self.cell_1_3.setText(result[0][12])
            self.cell_1_4.setText(result[0][13])
            self.cell_1_5.setText(result[0][14])
            self.cell_1_6.setText(result[0][15])
            self.cell_1_7.setText(result[0][16])
            self.cell_1_8.setText(result[0][17])

            self.cell_2_0.setText(result[0][18])
            self.cell_2_1.setText(result[0][19])
            self.cell_2_2.setText(result[0][20])
            self.cell_2_3.setText(result[0][21])
            self.cell_2_4.setText(result[0][22])
            self.cell_2_5.setText(result[0][23])
            self.cell_2_6.setText(result[0][24])
            self.cell_2_7.setText(result[0][25])
            self.cell_2_8.setText(result[0][26])

            self.cell_3_0.setText(result[0][27])
            self.cell_3_1.setText(result[0][28])
            self.cell_3_2.setText(result[0][29])
            self.cell_3_3.setText(result[0][30])
            self.cell_3_4.setText(result[0][31])
            self.cell_3_5.setText(result[0][32])
            self.cell_3_6.setText(result[0][33])
            self.cell_3_7.setText(result[0][34])
            self.cell_3_8.setText(result[0][35])

            self.cell_4_0.setText(result[0][36])
            self.cell_4_1.setText(result[0][37])
            self.cell_4_2.setText(result[0][38])
            self.cell_4_3.setText(result[0][39])
            self.cell_4_4.setText(result[0][40])
            self.cell_4_5.setText(result[0][41])
            self.cell_4_6.setText(result[0][42])
            self.cell_4_7.setText(result[0][43])
            self.cell_4_8.setText(result[0][44])

            self.cell_5_0.setText(result[0][45])
            self.cell_5_1.setText(result[0][46])
            self.cell_5_2.setText(result[0][47])
            self.cell_5_3.setText(result[0][48])
            self.cell_5_4.setText(result[0][49])
            self.cell_5_5.setText(result[0][50])
            self.cell_5_6.setText(result[0][51])
            self.cell_5_7.setText(result[0][52])
            self.cell_5_8.setText(result[0][53])

            self.cell_6_0.setText(result[0][54])
            self.cell_6_1.setText(result[0][55])
            self.cell_6_2.setText(result[0][56])
            self.cell_6_3.setText(result[0][57])
            self.cell_6_4.setText(result[0][58])
            self.cell_6_5.setText(result[0][59])
            self.cell_6_6.setText(result[0][60])
            self.cell_6_7.setText(result[0][61])
            self.cell_6_8.setText(result[0][62])

            self.cell_7_0.setText(result[0][63])
            self.cell_7_1.setText(result[0][64])
            self.cell_7_2.setText(result[0][65])
            self.cell_7_3.setText(result[0][66])
            self.cell_7_4.setText(result[0][67])
            self.cell_7_5.setText(result[0][68])
            self.cell_7_6.setText(result[0][69])
            self.cell_7_7.setText(result[0][70])
            self.cell_7_8.setText(result[0][71])

            self.cell_8_0.setText(result[0][72])
            self.cell_8_1.setText(result[0][73])
            self.cell_8_2.setText(result[0][74])
            self.cell_8_3.setText(result[0][75])
            self.cell_8_4.setText(result[0][76])
            self.cell_8_5.setText(result[0][77])
            self.cell_8_6.setText(result[0][78])
            self.cell_8_7.setText(result[0][79])
            self.cell_8_8.setText(result[0][80])
        else:
             self.pushButton_multiple_solutions_prev.setEnabled(True)
             self.pushButton_multiple_solutions_next.setEnabled(True)
             self.lineEdit_solved_puzzle.setText(result[self.count_sol-1])
             self.cell_0_0.setText(result[self.count_sol-1][0])
             self.cell_0_1.setText(result[self.count_sol-1][1])
             self.cell_0_2.setText(result[self.count_sol-1][2])
             self.cell_0_3.setText(result[self.count_sol-1][3])
             self.cell_0_4.setText(result[self.count_sol-1][4])
             self.cell_0_5.setText(result[self.count_sol-1][5])
             self.cell_0_6.setText(result[self.count_sol-1][6])
             self.cell_0_7.setText(result[self.count_sol-1][7])
             self.cell_0_8.setText(result[self.count_sol-1][8])

             self.cell_1_0.setText(result[self.count_sol-1][9])
             self.cell_1_1.setText(result[self.count_sol-1][10])
             self.cell_1_2.setText(result[self.count_sol-1][11])
             self.cell_1_3.setText(result[self.count_sol-1][12])
             self.cell_1_4.setText(result[self.count_sol-1][13])
             self.cell_1_5.setText(result[self.count_sol-1][14])
             self.cell_1_6.setText(result[self.count_sol-1][15])
             self.cell_1_7.setText(result[self.count_sol-1][16])
             self.cell_1_8.setText(result[self.count_sol-1][17])

             self.cell_2_0.setText(result[self.count_sol-1][18])
             self.cell_2_1.setText(result[self.count_sol-1][19])
             self.cell_2_2.setText(result[self.count_sol-1][20])
             self.cell_2_3.setText(result[self.count_sol-1][21])
             self.cell_2_4.setText(result[self.count_sol-1][22])
             self.cell_2_5.setText(result[self.count_sol-1][23])
             self.cell_2_6.setText(result[self.count_sol-1][24])
             self.cell_2_7.setText(result[self.count_sol-1][25])
             self.cell_2_8.setText(result[self.count_sol-1][26])

             self.cell_3_0.setText(result[self.count_sol-1][27])
             self.cell_3_1.setText(result[self.count_sol-1][28])
             self.cell_3_2.setText(result[self.count_sol-1][29])
             self.cell_3_3.setText(result[self.count_sol-1][30])
             self.cell_3_4.setText(result[self.count_sol-1][31])
             self.cell_3_5.setText(result[self.count_sol-1][32])
             self.cell_3_6.setText(result[self.count_sol-1][33])
             self.cell_3_7.setText(result[self.count_sol-1][34])
             self.cell_3_8.setText(result[self.count_sol-1][35])

             self.cell_4_0.setText(result[self.count_sol-1][36])
             self.cell_4_1.setText(result[self.count_sol-1][37])
             self.cell_4_2.setText(result[self.count_sol-1][38])
             self.cell_4_3.setText(result[self.count_sol-1][39])
             self.cell_4_4.setText(result[self.count_sol-1][40])
             self.cell_4_5.setText(result[self.count_sol-1][41])
             self.cell_4_6.setText(result[self.count_sol-1][42])
             self.cell_4_7.setText(result[self.count_sol-1][43])
             self.cell_4_8.setText(result[self.count_sol-1][44])

             self.cell_5_0.setText(result[self.count_sol-1][45])
             self.cell_5_1.setText(result[self.count_sol-1][46])
             self.cell_5_2.setText(result[self.count_sol-1][47])
             self.cell_5_3.setText(result[self.count_sol-1][48])
             self.cell_5_4.setText(result[self.count_sol-1][49])
             self.cell_5_5.setText(result[self.count_sol-1][50])
             self.cell_5_6.setText(result[self.count_sol-1][51])
             self.cell_5_7.setText(result[self.count_sol-1][52])
             self.cell_5_8.setText(result[self.count_sol-1][53])

             self.cell_6_0.setText(result[self.count_sol-1][54])
             self.cell_6_1.setText(result[self.count_sol-1][55])
             self.cell_6_2.setText(result[self.count_sol-1][56])
             self.cell_6_3.setText(result[self.count_sol-1][57])
             self.cell_6_4.setText(result[self.count_sol-1][58])
             self.cell_6_5.setText(result[self.count_sol-1][59])
             self.cell_6_6.setText(result[self.count_sol-1][60])
             self.cell_6_7.setText(result[self.count_sol-1][61])
             self.cell_6_8.setText(result[self.count_sol-1][62])

             self.cell_7_0.setText(result[self.count_sol-1][63])
             self.cell_7_1.setText(result[self.count_sol-1][64])
             self.cell_7_2.setText(result[self.count_sol-1][65])
             self.cell_7_3.setText(result[self.count_sol-1][66])
             self.cell_7_4.setText(result[self.count_sol-1][67])
             self.cell_7_5.setText(result[self.count_sol-1][68])
             self.cell_7_6.setText(result[self.count_sol-1][69])
             self.cell_7_7.setText(result[self.count_sol-1][70])
             self.cell_7_8.setText(result[self.count_sol-1][71])

             self.cell_8_0.setText(result[self.count_sol-1][72])
             self.cell_8_1.setText(result[self.count_sol-1][73])
             self.cell_8_2.setText(result[self.count_sol-1][74])
             self.cell_8_3.setText(result[self.count_sol-1][75])
             self.cell_8_4.setText(result[self.count_sol-1][76])
             self.cell_8_5.setText(result[self.count_sol-1][77])
             self.cell_8_6.setText(result[self.count_sol-1][78])
             self.cell_8_7.setText(result[self.count_sol-1][79])
             self.cell_8_8.setText(result[self.count_sol-1][80])

        self.label_multiple_solutions.setText(str(self.count_sol)+ ' of ' + str(len(result)))
        #return result[self.count_sol-1]
    def sol_next_button(self,result):
        #self.comboBox_UA_size.setCurrentIndex(0)
        #self.count_4 = 1
        #self.count_6 = 1
        if self.count_sol >= len(result):
            self.pushButton_multiple_solutions_prev.setEnabled(True)
            self.pushButton_multiple_solutions_next.setEnabled(False)
            self.lineEdit_solved_puzzle.setText(result[len(result)-1])
            self.cell_0_0.setText(result[len(result)-1][0])
            self.cell_0_1.setText(result[len(result)-1][1])
            self.cell_0_2.setText(result[len(result)-1][2])
            self.cell_0_3.setText(result[len(result)-1][3])
            self.cell_0_4.setText(result[len(result)-1][4])
            self.cell_0_5.setText(result[len(result)-1][5])
            self.cell_0_6.setText(result[len(result)-1][6])
            self.cell_0_7.setText(result[len(result)-1][7])
            self.cell_0_8.setText(result[len(result)-1][8])

            self.cell_1_0.setText(result[len(result)-1][9])
            self.cell_1_1.setText(result[len(result)-1][10])
            self.cell_1_2.setText(result[len(result)-1][11])
            self.cell_1_3.setText(result[len(result)-1][12])
            self.cell_1_4.setText(result[len(result)-1][13])
            self.cell_1_5.setText(result[len(result)-1][14])
            self.cell_1_6.setText(result[len(result)-1][15])
            self.cell_1_7.setText(result[len(result)-1][16])
            self.cell_1_8.setText(result[len(result)-1][17])

            self.cell_2_0.setText(result[len(result)-1][18])
            self.cell_2_1.setText(result[len(result)-1][19])
            self.cell_2_2.setText(result[len(result)-1][20])
            self.cell_2_3.setText(result[len(result)-1][21])
            self.cell_2_4.setText(result[len(result)-1][22])
            self.cell_2_5.setText(result[len(result)-1][23])
            self.cell_2_6.setText(result[len(result)-1][24])
            self.cell_2_7.setText(result[len(result)-1][25])
            self.cell_2_8.setText(result[len(result)-1][26])

            self.cell_3_0.setText(result[len(result)-1][27])
            self.cell_3_1.setText(result[len(result)-1][28])
            self.cell_3_2.setText(result[len(result)-1][29])
            self.cell_3_3.setText(result[len(result)-1][30])
            self.cell_3_4.setText(result[len(result)-1][31])
            self.cell_3_5.setText(result[len(result)-1][32])
            self.cell_3_6.setText(result[len(result)-1][33])
            self.cell_3_7.setText(result[len(result)-1][34])
            self.cell_3_8.setText(result[len(result)-1][35])

            self.cell_4_0.setText(result[len(result)-1][36])
            self.cell_4_1.setText(result[len(result)-1][37])
            self.cell_4_2.setText(result[len(result)-1][38])
            self.cell_4_3.setText(result[len(result)-1][39])
            self.cell_4_4.setText(result[len(result)-1][40])
            self.cell_4_5.setText(result[len(result)-1][41])
            self.cell_4_6.setText(result[len(result)-1][42])
            self.cell_4_7.setText(result[len(result)-1][43])
            self.cell_4_8.setText(result[len(result)-1][44])

            self.cell_5_0.setText(result[len(result)-1][45])
            self.cell_5_1.setText(result[len(result)-1][46])
            self.cell_5_2.setText(result[len(result)-1][47])
            self.cell_5_3.setText(result[len(result)-1][48])
            self.cell_5_4.setText(result[len(result)-1][49])
            self.cell_5_5.setText(result[len(result)-1][50])
            self.cell_5_6.setText(result[len(result)-1][51])
            self.cell_5_7.setText(result[len(result)-1][52])
            self.cell_5_8.setText(result[len(result)-1][53])

            self.cell_6_0.setText(result[len(result)-1][54])
            self.cell_6_1.setText(result[len(result)-1][55])
            self.cell_6_2.setText(result[len(result)-1][56])
            self.cell_6_3.setText(result[len(result)-1][57])
            self.cell_6_4.setText(result[len(result)-1][58])
            self.cell_6_5.setText(result[len(result)-1][59])
            self.cell_6_6.setText(result[len(result)-1][60])
            self.cell_6_7.setText(result[len(result)-1][61])
            self.cell_6_8.setText(result[len(result)-1][62])

            self.cell_7_0.setText(result[len(result)-1][63])
            self.cell_7_1.setText(result[len(result)-1][64])
            self.cell_7_2.setText(result[len(result)-1][65])
            self.cell_7_3.setText(result[len(result)-1][66])
            self.cell_7_4.setText(result[len(result)-1][67])
            self.cell_7_5.setText(result[len(result)-1][68])
            self.cell_7_6.setText(result[len(result)-1][69])
            self.cell_7_7.setText(result[len(result)-1][70])
            self.cell_7_8.setText(result[len(result)-1][71])

            self.cell_8_0.setText(result[len(result)-1][72])
            self.cell_8_1.setText(result[len(result)-1][73])
            self.cell_8_2.setText(result[len(result)-1][74])
            self.cell_8_3.setText(result[len(result)-1][75])
            self.cell_8_4.setText(result[len(result)-1][76])
            self.cell_8_5.setText(result[len(result)-1][77])
            self.cell_8_6.setText(result[len(result)-1][78])
            self.cell_8_7.setText(result[len(result)-1][79])
            self.cell_8_8.setText(result[len(result)-1][80])
        else:
            self.pushButton_multiple_solutions_prev.setEnabled(True)
            self.lineEdit_solved_puzzle.setText(result[self.count_sol-1])
            self.cell_0_0.setText(result[self.count_sol-1][0])
            self.cell_0_1.setText(result[self.count_sol-1][1])
            self.cell_0_2.setText(result[self.count_sol-1][2])
            self.cell_0_3.setText(result[self.count_sol-1][3])
            self.cell_0_4.setText(result[self.count_sol-1][4])
            self.cell_0_5.setText(result[self.count_sol-1][5])
            self.cell_0_6.setText(result[self.count_sol-1][6])
            self.cell_0_7.setText(result[self.count_sol-1][7])
            self.cell_0_8.setText(result[self.count_sol-1][8])

            self.cell_1_0.setText(result[self.count_sol-1][9])
            self.cell_1_1.setText(result[self.count_sol-1][10])
            self.cell_1_2.setText(result[self.count_sol-1][11])
            self.cell_1_3.setText(result[self.count_sol-1][12])
            self.cell_1_4.setText(result[self.count_sol-1][13])
            self.cell_1_5.setText(result[self.count_sol-1][14])
            self.cell_1_6.setText(result[self.count_sol-1][15])
            self.cell_1_7.setText(result[self.count_sol-1][16])
            self.cell_1_8.setText(result[self.count_sol-1][17])

            self.cell_2_0.setText(result[self.count_sol-1][18])
            self.cell_2_1.setText(result[self.count_sol-1][19])
            self.cell_2_2.setText(result[self.count_sol-1][20])
            self.cell_2_3.setText(result[self.count_sol-1][21])
            self.cell_2_4.setText(result[self.count_sol-1][22])
            self.cell_2_5.setText(result[self.count_sol-1][23])
            self.cell_2_6.setText(result[self.count_sol-1][24])
            self.cell_2_7.setText(result[self.count_sol-1][25])
            self.cell_2_8.setText(result[self.count_sol-1][26])

            self.cell_3_0.setText(result[self.count_sol-1][27])
            self.cell_3_1.setText(result[self.count_sol-1][28])
            self.cell_3_2.setText(result[self.count_sol-1][29])
            self.cell_3_3.setText(result[self.count_sol-1][30])
            self.cell_3_4.setText(result[self.count_sol-1][31])
            self.cell_3_5.setText(result[self.count_sol-1][32])
            self.cell_3_6.setText(result[self.count_sol-1][33])
            self.cell_3_7.setText(result[self.count_sol-1][34])
            self.cell_3_8.setText(result[self.count_sol-1][35])

            self.cell_4_0.setText(result[self.count_sol-1][36])
            self.cell_4_1.setText(result[self.count_sol-1][37])
            self.cell_4_2.setText(result[self.count_sol-1][38])
            self.cell_4_3.setText(result[self.count_sol-1][39])
            self.cell_4_4.setText(result[self.count_sol-1][40])
            self.cell_4_5.setText(result[self.count_sol-1][41])
            self.cell_4_6.setText(result[self.count_sol-1][42])
            self.cell_4_7.setText(result[self.count_sol-1][43])
            self.cell_4_8.setText(result[self.count_sol-1][44])

            self.cell_5_0.setText(result[self.count_sol-1][45])
            self.cell_5_1.setText(result[self.count_sol-1][46])
            self.cell_5_2.setText(result[self.count_sol-1][47])
            self.cell_5_3.setText(result[self.count_sol-1][48])
            self.cell_5_4.setText(result[self.count_sol-1][49])
            self.cell_5_5.setText(result[self.count_sol-1][50])
            self.cell_5_6.setText(result[self.count_sol-1][51])
            self.cell_5_7.setText(result[self.count_sol-1][52])
            self.cell_5_8.setText(result[self.count_sol-1][53])

            self.cell_6_0.setText(result[self.count_sol-1][54])
            self.cell_6_1.setText(result[self.count_sol-1][55])
            self.cell_6_2.setText(result[self.count_sol-1][56])
            self.cell_6_3.setText(result[self.count_sol-1][57])
            self.cell_6_4.setText(result[self.count_sol-1][58])
            self.cell_6_5.setText(result[self.count_sol-1][59])
            self.cell_6_6.setText(result[self.count_sol-1][60])
            self.cell_6_7.setText(result[self.count_sol-1][61])
            self.cell_6_8.setText(result[self.count_sol-1][62])

            self.cell_7_0.setText(result[self.count_sol-1][63])
            self.cell_7_1.setText(result[self.count_sol-1][64])
            self.cell_7_2.setText(result[self.count_sol-1][65])
            self.cell_7_3.setText(result[self.count_sol-1][66])
            self.cell_7_4.setText(result[self.count_sol-1][67])
            self.cell_7_5.setText(result[self.count_sol-1][68])
            self.cell_7_6.setText(result[self.count_sol-1][69])
            self.cell_7_7.setText(result[self.count_sol-1][70])
            self.cell_7_8.setText(result[self.count_sol-1][71])

            self.cell_8_0.setText(result[self.count_sol-1][72])
            self.cell_8_1.setText(result[self.count_sol-1][73])
            self.cell_8_2.setText(result[self.count_sol-1][74])
            self.cell_8_3.setText(result[self.count_sol-1][75])
            self.cell_8_4.setText(result[self.count_sol-1][76])
            self.cell_8_5.setText(result[self.count_sol-1][77])
            self.cell_8_6.setText(result[self.count_sol-1][78])
            self.cell_8_7.setText(result[self.count_sol-1][79])
            self.cell_8_8.setText(result[self.count_sol-1][80])
        self.label_multiple_solutions.setText(str(self.count_sol)+ ' of ' + str(len(result)))
        #return result[self.count_sol-1]'''

    def get_cell(self,cell):

        if cell == '00':
            return self.cell_0_0
        if cell == '01':
            return self.cell_0_1
        if cell == '02':
            return self.cell_0_2
        if cell == '03':
            return self.cell_0_3
        if cell == '04':
            return self.cell_0_4
        if cell == '05':
            return self.cell_0_5
        if cell == '06':
            return self.cell_0_6
        if cell == '07':
            return self.cell_0_7
        if cell == '08':
            return self.cell_0_8


        if cell == '10':
            return self.cell_1_0
        if cell == '11':
            return self.cell_1_1
        if cell == '12':
            return self.cell_1_2
        if cell == '13':
            return self.cell_1_3
        if cell == '14':
            return self.cell_1_4
        if cell == '15':
            return self.cell_1_5
        if cell == '16':
            return self.cell_1_6
        if cell == '17':
            return self.cell_1_7
        if cell == '18':
            return self.cell_1_8

        if cell == '20':
            return self.cell_2_0
        if cell == '21':
            return self.cell_2_1
        if cell == '22':
            return self.cell_2_2
        if cell == '23':
            return self.cell_2_3
        if cell == '24':
            return self.cell_2_4
        if cell == '25':
            return self.cell_2_5
        if cell == '26':
            return self.cell_2_6
        if cell == '27':
            return self.cell_2_7
        if cell == '28':
            return self.cell_2_8

        if cell == '30':
            return self.cell_3_0
        if cell == '31':
            return self.cell_3_1
        if cell == '32':
            return self.cell_3_2
        if cell == '33':
            return self.cell_3_3
        if cell == '34':
            return self.cell_3_4
        if cell == '35':
            return self.cell_3_5
        if cell == '36':
            return self.cell_3_6
        if cell == '37':
            return self.cell_3_7
        if cell == '38':
            return self.cell_3_8

        if cell == '40':
            return self.cell_4_0
        if cell == '41':
            return self.cell_4_1
        if cell == '42':
            return self.cell_4_2
        if cell == '43':
            return self.cell_4_3
        if cell == '44':
            return self.cell_4_4
        if cell == '45':
            return self.cell_4_5
        if cell == '46':
            return self.cell_4_6
        if cell == '47':
            return self.cell_4_7
        if cell == '48':
            return self.cell_4_8

        if cell == '50':
            return self.cell_5_0
        if cell == '51':
            return self.cell_5_1
        if cell == '52':
            return self.cell_5_2
        if cell == '53':
            return self.cell_5_3
        if cell == '54':
            return self.cell_5_4
        if cell == '55':
            return self.cell_5_5
        if cell == '56':
            return self.cell_5_6
        if cell == '57':
            return self.cell_5_7
        if cell == '58':
            return self.cell_5_8

        if cell == '60':
            return self.cell_6_0
        if cell == '61':
            return self.cell_6_1
        if cell == '62':
            return self.cell_6_2
        if cell == '63':
            return self.cell_6_3
        if cell == '64':
            return self.cell_6_4
        if cell == '65':
            return self.cell_6_5
        if cell == '66':
            return self.cell_6_6
        if cell == '67':
            return self.cell_6_7
        if cell == '68':
            return self.cell_6_8

        if cell == '70':
            return self.cell_7_0
        if cell == '71':
            return self.cell_7_1
        if cell == '72':
            return self.cell_7_2
        if cell == '73':
            return self.cell_7_3
        if cell == '74':
            return self.cell_7_4
        if cell == '75':
            return self.cell_7_5
        if cell == '76':
            return self.cell_7_6
        if cell == '77':
            return self.cell_7_7
        if cell == '78':
            return self.cell_7_8

        if cell == '80':
            return self.cell_8_0
        if cell == '81':
            return self.cell_8_1
        if cell == '82':
            return self.cell_8_2
        if cell == '83':
            return self.cell_8_3
        if cell == '84':
            return self.cell_8_4
        if cell == '85':
            return self.cell_8_5
        if cell == '86':
            return self.cell_8_6
        if cell == '87':
            return self.cell_8_7
        if cell == '88':
            return self.cell_8_8
    ##############################################################

    def counter_next_4(self):
        self.count_4 += 1
    def counter_prev_4(self):
        if self.count_4 == 1:
            return
        else:
            self.count_4 -= 1
            #return self.count
    def counter_next_6(self):
        self.count_6 += 1
        #return self.count
    def counter_prev_6(self):
        if self.count_6 == 1:
            return
        else:
            self.count_6 -= 1
            #return self.count

    def prev_button_4(self,list_UA):
        all_cell_keys = self.generate_keys('012345678','012345678')
        if self.count_4 == 1:
             self.pushButton_UA_prev_4.setEnabled(False)
             self.pushButton_UA_next_4.setEnabled(True)
             for a in list_UA[self.count_4]:
                self.get_cell(a).setStyleSheet("QLineEdit { background-color: white}")
             #for b in all_cell_keys:
             #   self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
             for i in list_UA[0]:
                self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")
        else:
            self.pushButton_UA_prev_4.setEnabled(True)
            self.pushButton_UA_next_4.setEnabled(True)
            for k in list_UA[self.count_4]:
                self.get_cell(k).setStyleSheet("QLineEdit { background-color: white}")
            #for b in all_cell_keys:
            #    self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
            for j in list_UA[int(self.count_4-1)]:
                self.get_cell(j).setStyleSheet("QLineEdit { background-color: #00BFFF}")

        self.label_3_UA_set_no_4.setText(str(self.count_4)+ ' of ' + str(len(list_UA)))
    def next_button_4(self,list_UA):
        all_cell_keys = self.generate_keys('012345678','012345678')
        if self.count_4 >= len(list_UA):
            self.pushButton_UA_prev_4.setEnabled(True)
            self.pushButton_UA_next_4.setEnabled(False)
            for j in list_UA[len(list_UA)-2]:
                self.get_cell(j).setStyleSheet("QLineEdit { background-color: white}")
            #for b in all_cell_keys:
            #    self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
            for i in list_UA[len(list_UA)-1]:
                self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")
            #print 'Whiten count greater: ' + str(list_UA[len(list_UA)-2])
            #print 'Blue count greater: ' + str(list_UA[len(list_UA)-1])
        else:
            self.pushButton_UA_prev_4.setEnabled(True)
            for k in list_UA[self.count_4-2]:
                self.get_cell(k).setStyleSheet("QLineEdit { background-color: white}")
            #for b in all_cell_keys:
            #    self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
            for h in list_UA[self.count_4-1]:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: #00BFFF}")
            #print 'Whiten count lesser: ' + str(list_UA[self.count_4-2])
            #print 'Blue count lesser: ' + str(list_UA[self.count_4-1])


        self.label_3_UA_set_no_4.setText(str(self.count_4)+ ' of ' + str(len(list_UA)))

    def prev_button_6(self,list_UA):
        all_cell_keys = self.generate_keys('012345678','012345678')
        if self.count_6 == 1:
             self.pushButton_UA_prev_6.setEnabled(False)
             self.pushButton_UA_next_6.setEnabled(True)
             #for a in list_UA[self.count_6]:
             #   self.get_cell(a).setStyleSheet("QLineEdit { background-color: white}")
             for b in all_cell_keys:
                self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
             for i in list_UA[0]:
                self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")
        else:
            self.pushButton_UA_prev_6.setEnabled(True)
            self.pushButton_UA_next_6.setEnabled(True)

            #for k in list_UA[self.count_6]:
            #    self.get_cell(k).setStyleSheet("QLineEdit { background-color: white}")
            for h in all_cell_keys:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: white}")
            for j in list_UA[int(self.count_6-1)]:
                self.get_cell(j).setStyleSheet("QLineEdit { background-color: #00BFFF}")

        self.label_3_UA_set_no_6.setText(str(self.count_6)+ ' of ' + str(len(list_UA)))
    def next_button_6(self,list_UA):
        all_cell_keys = self.generate_keys('012345678','012345678')
        if self.count_6 >= len(list_UA):
            self.pushButton_UA_prev_6.setEnabled(True)
            self.pushButton_UA_next_6.setEnabled(False)
            #for j in list_UA[len(list_UA)-2]:
            #    self.get_cell(j).setStyleSheet("QLineEdit { background-color: white}")
            for b in all_cell_keys:
                self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
            for i in list_UA[len(list_UA)-1]:
                self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")

        else:

            self.pushButton_UA_prev_6.setEnabled(True)
            #for k in list_UA[self.count_6-2]:
            #    self.get_cell(k).setStyleSheet("QLineEdit { background-color: white}")
            for b in all_cell_keys:
                self.get_cell(b).setStyleSheet("QLineEdit { background-color: white}")
            for h in list_UA[self.count_6-1]:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: #00BFFF}")

        self.label_3_UA_set_no_6.setText(str(self.count_6)+ ' of ' + str(len(list_UA)))

    def get_updated_solution(self):
        self.hi = self.lineEdit_solved_puzzle.text()
        self.lineEdit_solved_puzzle.setText(self.hi)

    def magic_try(self):
        self.count_4 = 1
        self.count_6 = 1

        all_cell_keys = self.generate_keys('012345678','012345678')
        self.lineEdit_solved_puzzle.textChanged.connect(self.get_updated_solution)
        puzzle = str(self.lineEdit_solved_puzzle.text())
        if puzzle == '' or puzzle == '000000000000000000000000000000000000000000000000000000000000000000000000000000000':
            return

        elif self.comboBox_UA_size.currentIndex() == 0:
            self.pushButton_UA_prev_6.hide()
            self.pushButton_UA_next_6.hide()
            self.label_3_UA_set_no_6.hide()
            for h in all_cell_keys:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: white}")
            self.pushButton_UA_prev_4.hide()
            self.pushButton_UA_next_4.hide()
            self.label_3_UA_set_no_4.hide()

        elif self.comboBox_UA_size.currentIndex() == 1:
            self.pushButton_UA_prev_6.hide()
            self.pushButton_UA_next_6.hide()
            self.label_3_UA_set_no_6.hide()
            for h in all_cell_keys:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: white}")
            self.pushButton_UA_prev_4.show()
            self.pushButton_UA_next_4.show()
            self.label_3_UA_set_no_4.show()

            list_UA = UA_oop_2.UA4(puzzle).check_element2()

            if len(list_UA) == 0:
                return
            else:
                #self.count_4 = 1
                if self.count_4 == 1:
                    self.pushButton_UA_prev_4.setEnabled(False)
                    for i in list_UA[0]:
                        self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")
                    self.label_3_UA_set_no_4.setText(str(self.count_4)+ ' of ' + str(len(list_UA)))
                    self.pushButton_UA_next_4.setEnabled(True)

                self.pushButton_UA_next_4.clicked.connect(lambda: self.next_button_4(list_UA))
                self.pushButton_UA_prev_4.clicked.connect(lambda: self.prev_button_4(list_UA))

        elif self.comboBox_UA_size.currentIndex() == 2:
            self.pushButton_UA_prev_4.hide()
            self.pushButton_UA_next_4.hide()
            self.label_3_UA_set_no_4.hide()
            for h in all_cell_keys:
                self.get_cell(h).setStyleSheet("QLineEdit { background-color: white}")
            self.pushButton_UA_prev_6.show()
            self.pushButton_UA_next_6.show()
            self.label_3_UA_set_no_6.show()

            list_UA = UA_oop_2.BandStackPure(puzzle,3).finding_UA_band_stack_pure() + UA_oop_2.BandStackMix(6,puzzle,3).finding_UA_band_stack_mixed()

            if len(list_UA) == 0:
                return
            else:
                #self.count_6 = 1
                if self.count_6 == 1:
                    self.pushButton_UA_prev_6.setEnabled(False)
                    for i in list_UA[0]:
                        self.get_cell(i).setStyleSheet("QLineEdit { background-color: #00BFFF}")
                    self.label_3_UA_set_no_6.setText(str(self.count_6)+ ' of ' + str(len(list_UA)))
                    self.pushButton_UA_next_6.setEnabled(True)

                self.pushButton_UA_next_6.clicked.connect(lambda: self.next_button_6(list_UA))
                self.pushButton_UA_prev_6.clicked.connect(lambda: self.prev_button_6(list_UA))


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

# test_puz = '003198070890370600007004893030087009079000380508039040726940508905800000380756900'
