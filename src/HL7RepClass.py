#!/usr/bin/env python

## This python class will parse HL7 ORU messages as input (first argument) and will produce a
## tab-delimited flat file as output (2nd argument) consisting of the following HL7 v 2.3.x fields.
## MSH-3, MSH-5, PV1-2, PID-3, PID-5, ORC-1, ORC-2, ORC-3
## To-do:  I'll continue to add HL7 fields and will also convert this


__author__="ruben robles"
__date__ ="$Dec 4, 2011 12:29:38 AM$"

""" Sample Usage:
using python interpreter

>>> import HL7RepClass
>>> p1 = HL7RepClass.ParseORUClass('hl7results.inputfile.txt', 'hl7results.outputfile.txt')
>>> p1.parseORU()

"""

import re
import sys

global header
global fileHandle
class ParseORUClass:
    def __init__(self, inFile, outFile):
         self.inFile = inFile
         self.outFile = outFile

    def parseORU(self):
        f = file(self.inFile, 'r')
        fileHandle = open (self.outFile, 'w')
        header = "MSH-3\tMSH-5\tPV1-2\tPID-3\tPID-5\tORC-1\tORC-2\tORC-3\n"
        fileHandle.write(header)
        msgRow = [[],[],[],[],[], [], [],[]]
        for splitSeg in f.readlines():

            splitSeg  = splitSeg.split("|")
            if re.search("MSH", splitSeg[0]):
                msgRow[0] = splitSeg[2]
                msgRow[1] = splitSeg[4]
                
                
                
                ##print segRow
                ##fileHandle.write(segRow)
            if re.search("PID", splitSeg[0]):
            ##pidThree = splitSeg [3]
                pidThree = splitSeg [3].split("^")
                msgRow[3] = pidThree[0]
                msgRow[4] = splitSeg[5]
                msgRow[4] = splitSeg[5]
            if re.search("PV1", splitSeg[0]):
                msgRow[2] = splitSeg[2]
            if re.search("ORC", splitSeg[0]):
            ##orcTwo = splitSeg[2]
                orcOne = splitSeg[1]
                orcTwo = splitSeg[2].split("^")
                msgRow[5] = orcOne
                msgRow[6] = orcTwo[0]
                ## ORC-3
                orcThree = splitSeg[3].split("^")
                msgRow[7] = orcThree[0]
                segRow = (msgRow[0],"\t",msgRow[1],"\t", msgRow[2], "\t", msgRow[3],"\t",msgRow[4],"\t"+ msgRow[5],"\t",
                  msgRow[6], "\t", msgRow[7],"\n")
                ##function below displays object type (ie. tuple)
                print segRow.__class__
                print segRow
                segRow = ''.join(segRow)

                
                
                fileHandle.write(segRow)
         fileHandle.close()         
         
    def printStuff(self):
         print "inFle = ", self.inFile
         print "outFile = ", self.outFile



        



