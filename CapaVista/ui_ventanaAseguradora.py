# Form implementation generated from reading ui file 'c:\Users\Zangara\Documents\1-CURSO AX\8460 - TÉCNICAS AVANZADAS DE PROGRAMACIÓN\BBDD\.vscode\LaSegura\SegurosLaGallega\CapaVista\ventanaAseguradora.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventanaAseguradora(object):
    def setupUi(self, ventanaAseguradora):
        ventanaAseguradora.setObjectName("ventanaAseguradora")
        ventanaAseguradora.resize(1032, 838)
        self.centralwidget = QtWidgets.QWidget(ventanaAseguradora)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 10, 701, 128))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtCarnetPersona = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCarnetPersona.setMaximumSize(QtCore.QSize(167, 16777215))
        self.txtCarnetPersona.setObjectName("txtCarnetPersona")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCarnetPersona)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.txtNombreyApellidoPersona = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombreyApellidoPersona.setObjectName("txtNombreyApellidoPersona")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNombreyApellidoPersona)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.txtDireccionpersona = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtDireccionpersona.setObjectName("txtDireccionpersona")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtDireccionpersona)
        self.lblIDPERSONA = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblIDPERSONA.setEnabled(False)
        self.lblIDPERSONA.setText("")
        self.lblIDPERSONA.setObjectName("lblIDPERSONA")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lblIDPERSONA)
        self.lblautosdepersona = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblautosdepersona.setObjectName("lblautosdepersona")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lblautosdepersona)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 300, 701, 131))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtnroInforme = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtnroInforme.setEnabled(False)
        self.txtnroInforme.setObjectName("txtnroInforme")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtnroInforme)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtFechaInforme = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtFechaInforme.setObjectName("txtFechaInforme")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtFechaInforme)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txtLugarInforme = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtLugarInforme.setObjectName("txtLugarInforme")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLugarInforme)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.txtImporteDanios = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtImporteDanios.setObjectName("txtImporteDanios")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtImporteDanios)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(70, 150, 701, 142))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtModelo = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtModelo.sizePolicy().hasHeightForWidth())
        self.txtModelo.setSizePolicy(sizePolicy)
        self.txtModelo.setMaximumSize(QtCore.QSize(400, 16777215))
        self.txtModelo.setObjectName("txtModelo")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModelo)
        self.txtAnio = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txtAnio.setMaximumSize(QtCore.QSize(70, 16777215))
        self.txtAnio.setText("")
        self.txtAnio.setObjectName("txtAnio")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAnio)
        self.lblDisplay = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lblDisplay.setText("")
        self.lblDisplay.setObjectName("lblDisplay")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lblDisplay)
        self.txtMatricula = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMatricula.sizePolicy().hasHeightForWidth())
        self.txtMatricula.setSizePolicy(sizePolicy)
        self.txtMatricula.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txtMatricula.setText("")
        self.txtMatricula.setObjectName("txtMatricula")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtMatricula)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 20, 188, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnExcel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExcel.setObjectName("btnExcel")
        self.verticalLayout.addWidget(self.btnExcel)
        self.btnBuscarPersona = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBuscarPersona.setObjectName("btnBuscarPersona")
        self.verticalLayout.addWidget(self.btnBuscarPersona)
        self.btnBuscarVehiculo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBuscarVehiculo.setObjectName("btnBuscarVehiculo")
        self.verticalLayout.addWidget(self.btnBuscarVehiculo)
        self.btnAgregarInforme = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAgregarInforme.setObjectName("btnAgregarInforme")
        self.verticalLayout.addWidget(self.btnAgregarInforme)
        self.btnPersonasaWord = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPersonasaWord.setObjectName("btnPersonasaWord")
        self.verticalLayout.addWidget(self.btnPersonasaWord)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 450, 411, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBoxVehiculo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBoxVehiculo.setObjectName("comboBoxVehiculo")
        self.gridLayout_2.addWidget(self.comboBoxVehiculo, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.comboBoxCarnet = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBoxCarnet.setObjectName("comboBoxCarnet")
        self.gridLayout_2.addWidget(self.comboBoxCarnet, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(70, 550, 256, 192))
        self.listView.setObjectName("listView")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(420, 550, 256, 192))
        self.tableView.setObjectName("tableView")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(730, 560, 256, 192))
        self.columnView.setObjectName("columnView")
        ventanaAseguradora.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventanaAseguradora)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        ventanaAseguradora.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventanaAseguradora)
        self.statusbar.setObjectName("statusbar")
        ventanaAseguradora.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaAseguradora)
        QtCore.QMetaObject.connectSlotsByName(ventanaAseguradora)

    def retranslateUi(self, ventanaAseguradora):
        _translate = QtCore.QCoreApplication.translate
        ventanaAseguradora.setWindowTitle(_translate("ventanaAseguradora", "Ventana Aseguradora"))
        self.label_4.setText(_translate("ventanaAseguradora", "Carnet Conductor"))
        self.label_11.setText(_translate("ventanaAseguradora", "Nombre "))
        self.label_12.setText(_translate("ventanaAseguradora", "Direccion"))
        self.lblautosdepersona.setText(_translate("ventanaAseguradora", "TextLabel"))
        self.label_5.setText(_translate("ventanaAseguradora", "numero de Informe"))
        self.label_6.setText(_translate("ventanaAseguradora", "fecha de Informe"))
        self.label_7.setText(_translate("ventanaAseguradora", "Lugar"))
        self.label_8.setText(_translate("ventanaAseguradora", "Importe Daños"))
        self.label.setText(_translate("ventanaAseguradora", "Matricula"))
        self.label_2.setText(_translate("ventanaAseguradora", "Modelo"))
        self.label_3.setText(_translate("ventanaAseguradora", "Año"))
        self.btnExcel.setText(_translate("ventanaAseguradora", "Autos a Excel"))
        self.btnBuscarPersona.setText(_translate("ventanaAseguradora", "Buscar Carnet"))
        self.btnBuscarVehiculo.setText(_translate("ventanaAseguradora", "Buscar Vehiculo"))
        self.btnAgregarInforme.setText(_translate("ventanaAseguradora", "Agregar Informe"))
        self.btnPersonasaWord.setText(_translate("ventanaAseguradora", "Personas a Word"))
        self.label_10.setText(_translate("ventanaAseguradora", "Carnet Conductor"))
        self.label_9.setText(_translate("ventanaAseguradora", "matricula vehiculo"))
