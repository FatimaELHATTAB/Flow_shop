import sys

from PyQt5 import QtWidgets, uic
import solve_problem

class Ui(QtWidgets.QMainWindow):
    type = 0

    def __init__(self):
        super(Ui, self).__init__()
        w = uic.loadUi('app.ui', self)
        self.w = w
        w.btn_0.clicked.connect(lambda: self.clicked(0))
        w.btn_1.clicked.connect(lambda: self.clicked(1))
        w.btn_2.clicked.connect(lambda: self.clicked(2))
        w.btn_3.clicked.connect(lambda: self.clicked(3))
        w.btn_4.clicked.connect(lambda: self.clicked(4))
        w.btn_5.clicked.connect(lambda: self.clicked(5))
        w.btn_6.clicked.connect(lambda: self.clicked(6))
        w.btn_7.clicked.connect(lambda: self.clicked(7))
        w.bestInstance.clicked.connect(lambda: self.clicked(8))
        w.runButton.clicked.connect(lambda: self.run_algorithm())

    def clicked(self, id):
        self.type = id
        print(type)
        print('Button {0} clicked'.format(id))


    def run_algorithm(self):
        val_0 = int(self.w.val_0.value())
        val_1 = int(self.w.val_1.value())
        val_2 = int(self.w.val_2.value())
        val_3 = int(self.w.val_3.value())
        val_4 = int(self.w.val_4.value())
        val_5 = int(self.w.doubleSpinBox.value())
        print(val_0, val_1, val_2)
        print(val_5)
        #self.w.text.append("CLicked with values %d, %d , %d " % (val_0, val_1, val_2))
        if self.type == 0: #branch and bound
            pass
        elif self.type == 1:#NEH
          pass
        elif self.type == 2:#NEH Amelioree
            pass
        elif self.type == 3:#CDS
            pass
        elif self.type == 4: #Algorithme genetique
            sequence,makespan = solve_problem.solve_benchmark_problem(val_0, val_2, val_1, val_3, val_4, val_5)
        elif self.type == 5:#VNS
            pass
        elif self.type == 6: #Hyper Heuristqiue
            pass
        elif self.type == 7: #Palmer
            pass
        print(sequence, makespan)
        self.w.label_resultat.setText(str(sequence))
        self.w.timeField.display(makespan)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
    # sys.exit()
