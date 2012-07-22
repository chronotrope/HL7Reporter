#!/usr/local/bin/jython
# -*- coding: utf-8 -*-
## HL7ORUGUI.py
## Ruben Robles
## This is a Jython class which uses the Java Swing libraries to implement a simple
## GUI wrapper around the HL7RepClass.py and implements the parsing method found in that Python class.
"""
Modified ZetCode Jython Swing tutorial
For the full Jython Swing tutorial, see:
http://zetcode.com/tutorials/jythonswingtutorial/introduction/


"""
import sys
import os
currPath = os.getcwd()
## this way i can distribute the ExampleFileFilter java class in the /lib folder of the current working directory
sys.path.append(currPath+'/lib')
from java.awt import BorderLayout
import ExampleFileFilter
from javax.swing import BorderFactory
from javax.swing import JFileChooser
from javax.swing import JTextArea
from javax.swing import JScrollPane
from javax.swing import JButton
from javax.swing import JToolBar
from javax.swing import JPanel
from javax.swing import JFrame
from javax.swing import JTextField
from javax.swing import JLabel
import HL7RepClass
import os
##from javax.swing.filechooser import FileNameExtensionFilter


class HL7GUIFrame(JFrame):
   outputTextField = None


   def __init__(self):
       super(HL7GUIFrame, self).__init__()

       self.initUI()

   def initUI(self):

       global outputTextField
       self.panel = JPanel()
       self.panel.setLayout(BorderLayout())

       toolbar = JToolBar()
       openb = JButton("Choose input file", actionPerformed=self.onClick)
       outputLabel = JLabel("   Enter output file name:  ")
       outputTextField = JTextField("hl7OutputReport.txt", 5)
       print outputTextField.getText()


     


       toolbar.add(openb)
       toolbar.add(outputLabel)
       toolbar.add(outputTextField)
      

       self.area = JTextArea()
       self.area.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10))
       self.area.setText("Select your HL7 ORU messages text file to be converted to tab-delimited flat \nfile with select HL7 fields.\n")
       self.area.append("You can enter the path + file name for your output file or it will default to the current \nfile name in the text field above in your current working directory.")

       pane = JScrollPane()
       pane.getViewport().add(self.area)

       self.panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10))
       self.panel.add(pane)
       self.add(self.panel)

       self.add(toolbar, BorderLayout.NORTH)


       self.setTitle("HL7 ORU Results Reporter")
       self.setSize(600, 300)
       self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
       self.setLocationRelativeTo(None)
       self.setVisible(True)
       return outputTextField.getText()


   def onClick(self, e):

       print outputTextField.getText()
       chooseFile = JFileChooser()
       filter = ExampleFileFilter()
       filter.addExtension("txt")
       filter.setDescription("txt HL7 input files")
       chooseFile.setFileFilter(filter)
       

       ##ret = chooseFile.showDialog(self.panel, "Choose file")
       ret = chooseFile.showOpenDialog(self.panel)

       if ret == JFileChooser.APPROVE_OPTION:
           file = chooseFile.getSelectedFile()
           text = self.readFile(file)
           self.area.append(text)
           outputFile = outputTextField.getText()
           p1 = HL7RepClass.ParseORUClass(file.getCanonicalPath(), outputFile)
           p1.parseORU()
           print "\noutfile = ", outputFile

   def readFile(self, file):
       filename = file.getCanonicalPath()
       print "filename is now ", filename
       f = open(filename, "r")
       
       text = f.read()
     
       return text



if __name__ == '__main__':
   HL7GUIFrame()