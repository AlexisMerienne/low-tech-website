import markdown
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join



class HtmlParser:

    content_apropos = ""
    content_bc = ""
    content_enquete = ""

    def __init__(self,content_apropos,content_bc,content_enquete) :
        self.content_apropos = content_apropos
        self.content_bc = content_bc
        self.content_enquete = content_enquete

    
    def openmarkdown(self):
        with open(self.content_apropos, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
        f.close()
        return html

    


    def write_html_content_apropos(self):

        with open("apropos/template/home.html") as ap_f:
            ap_html = ap_f.read()

        ap_soup = BeautifulSoup(ap_html, 'html.parser')
        
        ap_wrapper = ap_soup.find("div",class_='entry-content')
        new_ap = self.openmarkdown()
        new_ap = BeautifulSoup(new_ap,'html.parser')
        ap_wrapper.insert(1,new_ap)
        
        
        return ap_soup.prettify()

        




