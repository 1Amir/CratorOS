import os
import requests
import CratorOS
from scrapy import simple_get
from bs4 import BeautifulSoup
def Website():

	def check_content_div(html):

		if html.find(class_= "post_body"):
    			return html.find(class_= "post_body").text

		if html.find(class_= "section-content"):
    			return html.find(class_= "section-content").text

		if html.find(class_= "article-content clearfix"):
    			return html.find(class_= "article-content clearfix").text


	url = input("Hello user enter your BlogPost: ")
	raw_html = simple_get(url)
	html = BeautifulSoup(raw_html, 'html.parser')
	content = check_content_div(html)
	print("\n" + content + "\n")
def help():
		print "Comp.say(string)-put text on the screen"
		print "Comp.download(url)-download a file from a specifed url. eg. Comp.download('http://website.com/files/file.zip')"
		print "GoTo(path)-Go into specifed directory."
		CratorOS.CommandLine()
def download(url):
	os.system("wget " + url)
def say(y):
	print y
