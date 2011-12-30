## by Ruben Robles
##
## These Python classes provide a simple example of how Python classes can be implemented as 
## standalone Jython scripts.  I've even taken it a step further and have used knowledge gathered from
## zetcode.com in order to build a Jython class (HL7ORUGui.py) which uses the Java Swing GUI library to implement the HL7RepClass.py script.
## This Python script will parse a HL7 ORU messages as input (first argument) and will produce a
## tab-delimited flat file as output (2nd argument) consisting of the following HL7 v 2.3.x fields.
## MSH-3, MSH-5, PV1-2, PID-3, PID-5, ORC-1, ORC-2, ORC-3
## This current version includes an the OO Python class (HL7RepClass.py) which includes the methods necessary to:
## Open the input file with the HL7 ORU messages as the first argument.
## Parse the input file for selected singleton HL7 fields.
## Output these parsed fields in a tab-delimited format to the text file specified in the 2nd parameter.
## Finally, I've also included a modified version of the standalone Jython.jar named "jython_standalone.jar".
## I've added some necessary Python modules (re.py, etc.) in order to allow the HL7RepClass.py script to run in 
## standalone mode.  More info on how to do this can be found here:
## More info on packaging Jython standalone programs can be found here:
## http://goo.gl/idNmY
## Another more advanced option is the One-Jar method http://goo.gl/lQMre .  However, this solution requires Java 1.6 and higher.
## This may be an issue in some enterprise environments where legacy Java apps may require workstations to use 
## an older version of the JRE such as Java 1.5.x.
