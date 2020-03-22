from PySide2 import QtCore, QtGui, QtWidgets

def getHoudiniWindow():
    win = hou.ui.mainQtWindow()
    return win

class OutputNulls(QtWidgets.QMainWindow):
        
    def __init__(self, parent=None):
        super(OutputNulls, self).__init__(parent)
        
        widget = QtWidgets.QWidget()
        """
        Resize widget window
        """
        self.resize(500, 50)
        self.setWindowTitle("Output Null")
        
        hbox = QtWidgets.QGridLayout()
        """
        Output node name - input
        """
        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.setObjectName("nameInput")

        hbox.addWidget(self.nameInput, 0, 0, 1, 6)
        """
        Buttons, can be edited, depends requirements
        """
        out_button = QtWidgets.QPushButton("OUT")
        out_render = QtWidgets.QPushButton("OUT_RENDER")
        out_geo = QtWidgets.QPushButton("OUT_GEO")
        out_pts = QtWidgets.QPushButton("OUT_PTS")
        out_volume = QtWidgets.QPushButton("OUT_VOLUME")
        out_qc = QtWidgets.QPushButton("QUIT")
        
        hbox.addWidget(out_button, 1, 0)
        hbox.addWidget(out_render, 1, 1)
        hbox.addWidget(out_geo, 1, 2)
        hbox.addWidget(out_pts, 1, 3)
        hbox.addWidget(out_volume, 1, 4)
        hbox.addWidget(out_qc, 1, 5)
        """
        Stylesheet and color set in RGB values 
        """
        out_button.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(211, 47, 47) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )
                      
        out_render.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(230, 81, 0) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )  
                      
        out_geo.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(123, 31, 162) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )                        
        
        out_pts.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(0, 151, 167) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )

        out_volume.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(46, 125, 50) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )

        out_qc.setStyleSheet("QPushButton { color: rgb(200,200,200); border: 0px; background-color: rgb(97, 97, 97) }"
                      "QPushButton:pressed { color: white; border: 0px; background-color: rgb(80,80,80) }" )                      
                      
        out_button.clicked.connect(self.setNull)
        out_render.clicked.connect(self.setNull)
        out_geo.clicked.connect(self.setNull)
        out_pts.clicked.connect(self.setNull)
        out_volume.clicked.connect(self.setNull)
        out_qc.clicked.connect(self.quit)

        widget.setLayout(hbox)      
        self.setCentralWidget(widget)    
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
    """
    Creating Null objects based on selected button
    """        
    def setNull(self):
        if not hou.selectedNodes():
            print "Select Node to setup output!"
        else:
    
            for node in hou.selectedNodes():
                path = node.parent().path()
                
            outputnull = hou.node(path).createNode("null")
            outputnull.setInput(0, node, 0)
            outputnull.move(node.position())
            outputnull.move((0, -2))
            
            if not self.nameInput.text():
                outputname = node.parent().name()
            else:
                outputname = self.nameInput.text()
                   
            sending_button = self.sender()
            outputnull.setName(sending_button.text() + "_" + outputname, 1)
            """
            Node colors in RGB % values
            """
            if sending_button.text()=="OUT": color_render = hou.Color((0.83, 0.18, 0.18))
            if sending_button.text()=="OUT_RENDER": color_render = hou.Color((0.90, 0.32, 0))
            if sending_button.text()=="OUT_GEO": color_render = hou.Color((0.48, 0.12, 0.64))
            if sending_button.text()=="OUT_PTS": color_render = hou.Color((0, 0.59, 0.65))
            if sending_button.text()=="OUT_VOLUME": color_render = hou.Color((0.18, 0.49, 0.20))
            if sending_button.text()=="QC_OUT": color_render = hou.Color((0.38, 0.38, 0.38))
            
            outputnull.setColor(color_render)
    
            outputWidget.close()

    def quit(self):
        outputWidget.close()
        
outputWidget = OutputNulls()
outputWidget.setWindowFlags(outputWidget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
outputWidget.setStyleSheet("QMainWindow {background: rgb(80, 80, 80);}");
outputWidget.show()
