# coding: utf-8
import os
import CratorOS
def CreateUser():
	print "		Welcome to CratorOS!"
	print "-----------------------------------------------"
	print ""
	print "	Developed by Team Night OWL Studios"
	print " 	|#|#|#|#|#||######| |#| |######|"
	print "	   |#|     |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#| |#| |#|  |#|"
	print "	   |#|	   |#|  |#####| |######|"
	print ""
	print "The OS needs to install several peices of software to being."
	enter = raw_input("Press any key to Continue...")
	print "Installing all neccessary software..."
	os.system("sudo apt-get install python-pip")
	os.system("sudo pip install pygame")
	os.system("sudo pip install turtle")
	os.system("sudo pip install colorama==0.3.3")

	Username = raw_input("What will be your Username?:")
	password = raw_input("What will be your password?:")
	confpassword = raw_input("Confirm your password:")
	if password == confpassword:
		UserInfoLogin = open('WFBFQXQGEDOUVTAXACIOEFVITUHVIS.txt','w')#open text file with permissions to only write
		UserInfoLogin.write(Username)
		UserInfoLogin.write(password)
		os.system('reset')
		print "The linux command 'cd' does not work, please use 'Goto' instead."
		enter = raw_input("press enter to continue")
		CratorOS.CommandLine(Username)
def checkuser():
		os.system("reset")
		os.chdir("User")
		if open("WFBFQXQGEDOUVTAXACIOEFVITUHVIS.txt", "r").read() == "":	
			CreateUser()
		else:
			CratorOS.loginUser()
checkuser()