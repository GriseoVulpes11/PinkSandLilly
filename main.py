import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QDialog, \
    QAction

import DataStorage as DS

# Receiving data from PSL.p
data = DS.Retrieve_from_file()


# Creates color class for the GUI
class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


# Creates main Window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setStyleSheet("""
        QPushButton[Work_Button=true] {
                border: 0px solid #8f8f91;
                border-radius: 6px;
                background-color: #DDE1E4;
                min-width: 40px;
                max-width:40px;
            }
        QPushButton[Change_Name=true]{
            border: 0px solid #8f8f91;
            border-radius: 6px;
            background-color: #DDE1E4;
            color: black;
            min-width: 180px;
            max-width:180px;
        }
        QLabel {
        color: #F2F5EA;
        font-weight: bold;
        }
        QLabel[Title=true] {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 30px;
            color: #F2F5EA;
        }
            QMainWindow { background-color: #424651 } 
        """)

        self.setWindowTitle("PinkSandLilly")
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        # The main Layout ||

        main_layout = QVBoxLayout()
        Title = QLabel("PinkSandLilly")
        Title.setProperty("Title",True)
        Title.setAlignment(QtCore.Qt.AlignCenter)
        Title.setFont(QFont("Helvetica", 20))
        main_layout.addWidget(Title)
        # First Layer --

        data_class_1 = data[1]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 1
            layoutNested.addWidget(QLabel(data_class_1["Name"]))
            work = len(data_class_1["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton1 = QPushButton()
            WorkButton1.setIcon(QIcon('plac.png'))
            WorkButton1.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button1():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_1["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_1["Work"]
                add_work_button1 = QPushButton("Add Work")

                def add_work1():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[1]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[1] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_1 = QPushButton()

                    # displays the description and due date
                    def work_description1():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button1 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked1():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[1]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button1.clicked.connect:
                            delete_work_button_clicked1()

                        description_layout.addWidget(delete_work_button1)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_1.clicked.connect(work_description1)
                    # sets work button image
                    work_discription_button_1.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_1)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button1.clicked.connect(add_work1)
                Work_Layout.addWidget(add_work_button1)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton1.clicked.connect(work_button1)
            layoutNested.addWidget(WorkButton1)

        # Second Layer --
        data_class_2 = data[2]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 2
            layoutNested.addWidget(QLabel(data_class_2["Name"]))
            work = len(data_class_2["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton2 = QPushButton()
            WorkButton2.setIcon(QIcon('plac.png'))
            WorkButton2.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button2():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_2["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_2["Work"]
                add_work_button2 = QPushButton("Add Work")

                def add_work2():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[2]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[2] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_2 = QPushButton()

                    # displays the description and due date
                    def work_description2():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button2 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked2():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[2]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button2.clicked.connect:
                            delete_work_button_clicked2()

                        description_layout.addWidget(delete_work_button2)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_2.clicked.connect(work_description2)
                    # sets work button image
                    work_discription_button_2.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_2)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button2.clicked.connect(add_work2)
                Work_Layout.addWidget(add_work_button2)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton2.clicked.connect(work_button2)
            layoutNested.addWidget(WorkButton2)
        # Third Layer --

        data_class_3 = data[3]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 3
            layoutNested.addWidget(QLabel(data_class_3["Name"]))
            work = len(data_class_3["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton3 = QPushButton()
            WorkButton3.setIcon(QIcon('plac.png'))
            WorkButton3.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button3():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_3["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_3["Work"]
                add_work_button3 = QPushButton("Add Work")

                def add_work3():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[3]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[3] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_3 = QPushButton()

                    # displays the description and due date
                    def work_description3():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button3 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked3():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[3]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button3.clicked.connect:
                            delete_work_button_clicked3()

                        description_layout.addWidget(delete_work_button3)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_3.clicked.connect(work_description3)
                    # sets work button image
                    work_discription_button_3.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_3)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button3.clicked.connect(add_work3)
                Work_Layout.addWidget(add_work_button3)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton3.clicked.connect(work_button3)
            layoutNested.addWidget(WorkButton3)

        # Fourth Layer --
        data_class_4 = data[4]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 4
            layoutNested.addWidget(QLabel(data_class_4["Name"]))
            work = len(data_class_4["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton4 = QPushButton()
            WorkButton4.setIcon(QIcon('plac.png'))
            WorkButton4.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button4():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_4["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_4["Work"]
                add_work_button4 = QPushButton("Add Work")

                def add_work4():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[4]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[4] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_4 = QPushButton()

                    # displays the description and due date
                    def work_description4():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button4 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked4():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[4]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button4.clicked.connect:
                            delete_work_button_clicked4()

                        description_layout.addWidget(delete_work_button4)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_4.clicked.connect(work_description4)
                    # sets work button image
                    work_discription_button_4.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_4)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button4.clicked.connect(add_work4)
                Work_Layout.addWidget(add_work_button4)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton4.clicked.connect(work_button4)
            layoutNested.addWidget(WorkButton4)

        # Fifth Layer --
        data_class_5 = data[5]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 5
            layoutNested.addWidget(QLabel(data_class_5["Name"]))
            work = len(data_class_5["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton5 = QPushButton()
            WorkButton5.setIcon(QIcon('plac.png'))
            WorkButton5.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button5():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_5["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_5["Work"]
                add_work_button5 = QPushButton("Add Work")

                def add_work5():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[5]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[5] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_5 = QPushButton()

                    # displays the description and due date
                    def work_description5():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button5 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked5():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[5]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button5.clicked.connect:
                            delete_work_button_clicked5()

                        description_layout.addWidget(delete_work_button5)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_5.clicked.connect(work_description5)
                    # sets work button image
                    work_discription_button_5.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_5)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button5.clicked.connect(add_work5)
                Work_Layout.addWidget(add_work_button5)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton5.clicked.connect(work_button5)
            layoutNested.addWidget(WorkButton5)

        # sixth Layer --
        data_class_6 = data[6]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 6
            layoutNested.addWidget(QLabel(data_class_6["Name"]))
            work = len(data_class_6["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton6 = QPushButton()
            WorkButton6.setIcon(QIcon('plac.png'))
            WorkButton6.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button6():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_6["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_6["Work"]
                add_work_button6 = QPushButton("Add Work")

                def add_work6():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[6]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[6] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_6 = QPushButton()

                    # displays the description and due date
                    def work_description6():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button6 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked6():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[6]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button6.clicked.connect:
                            delete_work_button_clicked6()

                        description_layout.addWidget(delete_work_button6)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_6.clicked.connect(work_description6)
                    # sets work button image
                    work_discription_button_6.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_6)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button6.clicked.connect(add_work6)
                Work_Layout.addWidget(add_work_button6)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton6.clicked.connect(work_button6)
            layoutNested.addWidget(WorkButton6)

        # seventh Layer --
        data_class_7 = data[7]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 7
            layoutNested.addWidget(QLabel(data_class_7["Name"]))
            work = len(data_class_7["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton7 = QPushButton()
            WorkButton7.setIcon(QIcon('plac.png'))
            WorkButton7.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button7():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_2["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_7["Work"]
                add_work_button7 = QPushButton("Add Work")

                def add_work7():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[7]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[7] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_7 = QPushButton()

                    # displays the description and due date
                    def work_description7():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button7 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked7():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[7]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button7.clicked.connect:
                            delete_work_button_clicked7()

                        description_layout.addWidget(delete_work_button7)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_7.clicked.connect(work_description7)
                    # sets work button image
                    work_discription_button_7.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_7)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button7.clicked.connect(add_work7)
                Work_Layout.addWidget(add_work_button7)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton7.clicked.connect(work_button7)
            layoutNested.addWidget(WorkButton7)

        # Eigth Layer --
        data_class_8 = data[8]
        layoutNested = QHBoxLayout()
        main_layout.addLayout(layoutNested)

        if data != 1:
            # places name of class 8
            layoutNested.addWidget(QLabel(data_class_8["Name"]))
            work = len(data_class_8["Work"])
            # places the amount of assignments
            if work == 1:
                number_of_assignments_title = " Assignment"
            else:
                number_of_assignments_title = " Assignments"

            layoutNested.addWidget(QLabel(str(work) + number_of_assignments_title))
            # places button for opening work tab
            WorkButton8 = QPushButton()
            WorkButton8.setIcon(QIcon('plac.png'))
            WorkButton8.setProperty('Work_Button', True)

            # the work tab dialogue
            def work_button8():
                work_dialogue = QDialog()
                Work_Layout = QVBoxLayout()
                if work != 0:
                    Work_Layout.addWidget(QLabel("Your work for " + data_class_8["Name"]))
                else:
                    Work_Layout.addWidget(QLabel("You don't seem to have any work for this class"))
                work_dic = data_class_8["Work"]
                add_work_button8 = QPushButton("Add Work")

                def add_work8():
                    m = QDialog()
                    add_work_layout = QVBoxLayout()
                    work_name = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'What Do you want this work to be called?:')
                    work_name_real = work_name[0]
                    description = QtWidgets.QInputDialog.getText(
                        self, 'Input Dialog', 'Enter any Discription you want to have for this assignment:')
                    description_real = description[0]
                    items = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                             "October", "November", "December")
                    month_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                                " ", items, 0, False)
                    # sets the days to match months
                    month_date_real = month_date[0]
                    if month_date_real == 'January':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'February':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28')
                    elif month_date_real == 'March':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'April':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'May':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'June':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'July':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'August':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'September':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'October':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')
                    elif month_date_real == 'November':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30')
                    elif month_date_real == 'December':
                        days = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", '18', '19', '20', '21', '22',
                                '23', '24', '25', '26', '27', '28', '29', '30', '31')

                    day_date = QtWidgets.QInputDialog.getItem(self, "Enter the due date",
                                                              "What day of " + str(
                                                                  month_date_real) + " is this due", days, 0,
                                                              False)
                    day_date_real = day_date[0]
                    # puts the data collected for the new assignment in hard storage
                    complete_data = DS.Retrieve_from_file()
                    section_data = complete_data[8]
                    work_data = section_data["Work"]
                    section_data_length = len(work_data)
                    if len(work_data) != 0:
                        final_data_number = max(section_data["Work"])
                        work_data[int(final_data_number) + 1] = {"Work": str(work_name_real),
                                                                 "Imp": str(description_real),
                                                                 "timeneeded": str(month_date_real) + "/" + str(
                                                                     day_date_real)}
                    else:
                        work_data[8] = {"Work": str(work_name_real), "Imp": str(description_real),
                                        "timeneeded": str(month_date_real) + "/" + str(
                                            day_date_real)}
                    DS.add_to_file(complete_data)

                # displays the work names
                for x in work_dic:
                    assignment = work_dic[x]
                    work_nested_layout = QHBoxLayout()
                    work_nested_layout.addWidget(QLabel(str(assignment['Work'])))
                    work_discription_button_8 = QPushButton()

                    # displays the description and due date
                    def work_description8():
                        work_description_dialog = QDialog()
                        description_layout = QVBoxLayout()
                        description_layout.addWidget(QLabel("Description:"))
                        description_layout.addWidget(QLabel(str(assignment["Imp"])))
                        description_layout.addWidget(QLabel(" "))
                        description_layout.addWidget((QLabel("This assignment is Due:")))
                        description_layout.addWidget(QLabel(str(assignment["timeneeded"])))

                        # deletes the work

                        delete_work_button8 = QPushButton("Delete this assignment")

                        def delete_work_button_clicked8():
                            complete_data = DS.Retrieve_from_file()
                            section_data = complete_data[8]
                            work_dictonary = section_data["Work"]

                            try:
                                del work_dictonary[x]
                                DS.add_to_file(complete_data)
                            except:
                                DS.add_to_file(complete_data)

                        if delete_work_button8.clicked.connect:
                            delete_work_button_clicked8()

                        description_layout.addWidget(delete_work_button8)

                        work_description_dialog.setLayout(description_layout)
                        work_description_dialog.setWindowModality(Qt.ApplicationModal)
                        work_description_dialog.exec_()

                    work_discription_button_8.clicked.connect(work_description8)
                    # sets work button image
                    work_discription_button_8.setIcon(QIcon('plac.png'))
                    work_nested_layout.addWidget(work_discription_button_8)
                    Work_Layout.addLayout(work_nested_layout)

                add_work_button8.clicked.connect(add_work8)
                Work_Layout.addWidget(add_work_button8)
                work_dialogue.setLayout(Work_Layout)
                work_dialogue.setWindowModality(Qt.ApplicationModal)
                work_dialogue.exec_()

            WorkButton8.clicked.connect(work_button8)
            layoutNested.addWidget(WorkButton8)

        # Bottom layer buttons
        # Creates the dialogue for EditClassButton

        def EditClassNameButton():
            # Dialoge Boxes for input text
            # Number 1
            def EditName1():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the first class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[1]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 2
            def EditName2():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the second class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[2]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 3
            def EditName3():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the third class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[3]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 4
            def EditName4():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the forth class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[4]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 5
            def EditName5():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the fifth class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[5]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 6
            def EditName6():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the sixth class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[6]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 7
            def EditName7():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the seventh class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[7]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            # Number 8
            def EditName8():
                c = QDialog()
                edit = QtWidgets.QInputDialog.getText(
                    self, 'Input Dialog', 'Enter the new name for the eighth class :')
                change = edit[0]
                fulldata = DS.Retrieve_from_file()
                secdata = fulldata[8]
                secdata["Name"] = change
                DS.add_to_file(fulldata)

            Name = 0

            d = QDialog()
            ECBLayout = QVBoxLayout()
            ECBLayout.addWidget(QLabel("Choose Witch class name you want to change"))
            # Choosing  to change the name
            # The first Class
            clss = data[1]
            NameButton1 = QPushButton(clss["Name"])
            NameButton1.clicked.connect(EditName1)
            ECBLayout.addWidget(NameButton1)

            # The Second class
            clss = data[2]
            NameButton2 = QPushButton(clss["Name"])
            NameButton2.clicked.connect(EditName2)
            ECBLayout.addWidget(NameButton2)

            # The Third class
            clss = data[3]
            NameButton3 = QPushButton(clss["Name"])
            NameButton3.clicked.connect(EditName3)
            ECBLayout.addWidget(NameButton3)

            # The forth class
            clss = data[4]
            NameButton4 = QPushButton(clss["Name"])
            NameButton4.clicked.connect(EditName4)
            ECBLayout.addWidget(NameButton4)

            # The fifth  class
            clss = data[5]
            NameButton5 = QPushButton(clss["Name"])
            NameButton5.clicked.connect(EditName5)
            ECBLayout.addWidget(NameButton5)

            # The Sixth class
            clss = data[6]
            NameButton6 = QPushButton(clss["Name"])
            NameButton6.clicked.connect(EditName6)
            ECBLayout.addWidget(NameButton6)

            # The Second class
            clss = data[7]
            NameButton7 = QPushButton(clss["Name"])
            NameButton7.clicked.connect(EditName7)
            ECBLayout.addWidget(NameButton7)

            # The Eighth class
            clss = data[8]
            NameButton8 = QPushButton(clss["Name"])
            NameButton8.clicked.connect(EditName8)
            ECBLayout.addWidget(NameButton8)

            # Intialization
            d.setLayout(ECBLayout)
            d.setWindowTitle("Edit Class")
            d.setWindowModality(Qt.ApplicationModal)
            d.exec_()



        layoutNestedBT = QHBoxLayout()
        EditButton = QPushButton("Change Class Name")
        EditButton.setProperty("Change_Name",True)
        EditButton.clicked.connect(EditClassNameButton)
        layoutNestedBT.addWidget(EditButton)
        main_layout.addLayout(layoutNestedBT)
        main_layout.addLayout(layoutNestedBT)

        # Initializes

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
