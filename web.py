from scrapy import simple_get
from bs4 import BeautifulSoup

if __name__ == '__main__':

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

