# coding: utf-8
import os
import requests
import colorama
import Comp
import urllib2
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
#Reads input and calls the right function for each input
def Compiler(InputGiven):
	 if "help Crater" in InputGiven:
	 		Comp.help()
	 if InputGiven == "help linux":
	 		os.system("help")
	 if "Comp.download(" in InputGiven:#proper!!
	 	print "Feature being added in the future."
	 if InputGiven == "Open Blog":
		Comp.Website()
	 if "Goto" in InputGiven:
	 	Command2 = InputGiven.strip("Goto")
	 	Command3 = Command2.strip("(")
	 	Command4 = Command3.strip(")")
	 	os.chdir(Command4)
	 if "lf" in InputGiven:
	 	os.system("ls")
	 else:
	 	os.system(InputGiven)
#Starter command line
def CommandLine(UsernameCheck):
 	running = True
  	os.system("reset")
  	print(Style.BRIGHT)
 	print Fore.RED + "			CratorOS"
 	print "------------------------------------------------------------------"
 	print(Style.RESET_ALL)
 	while(running):
	  	print(Style.BRIGHT)
 		UserInput = raw_input(Fore.BLUE + "home@" + UsernameCheck + ":")
 		print(Style.RESET_ALL)
 		if 'exit' in UserInput:
 			running = False
 		if UserInput == 'help':
 				print 'All linux commands can be found by typing "help linux"(Not all linux commands work:e.g. cd)'	
 				print 'To see Crater commands, type "help Crater".'	
 		else:
 			Compiler(UserInput)
#Login code
def loginUser():
	print Fore.RED + "		Welcome to CratorOS!"
	print "-----------------------------------------------"
	print(Style.RESET_ALL)
	print "	Developed by Team Night OWL Studios"
	print " 	|#|#|#|#|#||######| |#| |######|"
	print "	   |#|     |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#####| |######|"
	print ""
	print Fore.CYAN + "-----------------------------------------------"
	UsernameCheck = raw_input("Enter Username:")
	print "-------------------------------------------"
	PasswordCheck = raw_input("Enter Password:")
	print "-------------------------------------------"
	print(Style.RESET_ALL)
	if open("WFBFQXQGEDOUVTAXACIOEFVITUHVIS.txt", "r").read() == UsernameCheck+PasswordCheck:
		print Fore.GREEN + "Successful login"
		print(Style.RESET_ALL)
		CommandLine(UsernameCheck)
	else:
		print Fore.RED + "Password or Username was incorrect!"
		print(Style.RESET_ALL)
		loginUser()
