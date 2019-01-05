# coding: utf-8
import os
import requests
import colorama
import urllib2
import gi
import sys
from bs4 import BeautifulSoup
from CratorLibrary import Comp
from colorama import Fore, Back, Style
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
			InputGiven = raw_input(Fore.BLUE + "home@" + UsernameCheck + ":")
			print(Style.RESET_ALL)
			if "Goto" in InputGiven:#Takes only the Directory Name of the Input and goes to that Directory if available
		    		Command2 = InputGiven.strip("Goto")
		    		Command3 = Command2.strip("(")
		    		Command4 = Command3.strip(")")
		    		Command5 = Command4.strip(" ")
		    		try:
		    			os.chdir(Command5)
		    		except OSError:
		    			print "[Errno 2] No such file or directory"
		    	elif InputGiven == "GoOut":
		    		os.chdir('..')
			elif 'exit' in InputGiven:
				running = False
			elif "help Crater" in InputGiven:
		 		print "Comp.say(string)-put text on the screen"
				print "GoTo(path)-Go into specifed directory."
				print "GoOut-Goes a directory back from the old directory"
		 	elif InputGiven == "help":
		 		print """These shell commands are defined internally.  Type `help' to see this list.
						Type `help name' to find out more about the function `name'.
						Use `info bash' to find out more about the shell in general.
						Use `man -k' or `info' to find out more about commands not in this list.

						A star (*) next to a name means that the command is disabled.

						 job_spec [&]                                                                            history [-c] [-d offset] [n] or history -anrw [filename] or history -ps arg [arg...]>
						 (( expression ))                                                                        if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMANDS; ]... [ else COMMANDS; ] >
						 . filename [arguments]                                                                  jobs [-lnprs] [jobspec ...] or jobs -x command [args]
						 :                                                                                       kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
						 [ arg... ]                                                                              let arg [arg ...]
						 [[ expression ]]                                                                        local [option] name[=value] ...
						 alias [-p] [name[=value] ... ]                                                          logout [n]
						 bg [job_spec ...]                                                                       mapfile [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [a>
						 bind [-lpsvPSVX] [-m keymap] [-f filename] [-q name] [-u name] [-r keyseq] [-x keyseq>  popd [-n] [+N | -N]
						 break [n]                                                                               printf [-v var] format [arguments]
						 builtin [shell-builtin [arg ...]]                                                       pushd [-n] [+N | -N | dir]
						 caller [expr]                                                                           pwd [-LP]
						 case WORD in [PATTERN [| PATTERN]...) COMMANDS ;;]... esac                              read [-ers] [-a array] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t >
						 cd [-L|[-P [-e]] [-@]] [dir]                                                            readarray [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] >
						 command [-pVv] command [arg ...]                                                        readonly [-aAf] [name[=value] ...] or readonly -p
						 compgen [-abcdefgjksuv] [-o option]  [-A action] [-G globpat] [-W wordlist]  [-F func>  return [n]
						 complete [-abcdefgjksuv] [-pr] [-DE] [-o option] [-A action] [-G globpat] [-W wordlis>  select NAME [in WORDS ... ;] do COMMANDS; done
						 compopt [-o|+o option] [-DE] [name ...]                                                 set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]
						 continue [n]                                                                            shift [n]
						 coproc [NAME] command [redirections]                                                    shopt [-pqsu] [-o] [optname ...]
						 declare [-aAfFgilnrtux] [-p] [name[=value] ...]                                         source filename [arguments]
						 dirs [-clpv] [+N] [-N]                                                                  suspend [-f]
						 disown [-h] [-ar] [jobspec ...]                                                         test [expr]
						 echo [-neE] [arg ...]                                                                   time [-p] pipeline
						 enable [-a] [-dnps] [-f filename] [name ...]                                            times
						 eval [arg ...]                                                                          trap [-lp] [[arg] signal_spec ...]
						 exec [-cl] [-a name] [command [arguments ...]] [redirection ...]                        true
						 exit [n]                                                                                type [-afptP] name [name ...]
						 export [-fn] [name[=value] ...] or export -p                                            typeset [-aAfFgilrtux] [-p] name[=value] ...
						 false                                                                                   ulimit [-SHabcdefilmnpqrstuvxT] [limit]
						 fc [-e ename] [-lnr] [first] [last] or fc -s [pat=rep] [command]                        umask [-p] [-S] [mode]
						 fg [job_spec]                                                                           unalias [-a] name [name ...]
						 for NAME [in WORDS ... ] ; do COMMANDS; done                                            unset [-f] [-v] [-n] [name ...]
						 for (( exp1; exp2; exp3 )); do COMMANDS; done                                           until COMMANDS; do COMMANDS; done
						 function name { COMMANDS ; } or name () { COMMANDS ; }                                  variables - Names and meanings of some shell variables
						 getopts optstring name [arg]                                                            wait [-n] [id ...]
						 hash [-lr] [-p pathname] [-dt] [name ...]                                               while COMMANDS; do COMMANDS; done
						 help [-dms] [pattern ...]                                                               { COMMANDS ; }"""
		    	else:
		 			os.system(InputGiven)
		    		
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
