import os
import requests
from scrapy import simple_get
from bs4 import BeautifulSoup
def help():
		print "Comp.say(string)-put text on the screen"
		print "Comp.download(url)-download a file from a specifed url. eg. Comp.download('http://website.com/files/file.zip')"
		print "GoTo(path)-Go into specifed directory."
		CratorOS.CommandLine()
def say(y):
	print y
