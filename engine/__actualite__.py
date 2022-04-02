import markdown
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join



class Actualites:

    actualites_list = []

    def __init__(self) :
        pass

    def read_file_actualites(self,path):
        for f in listdir(path):
             if isfile(join(path, f)):
                 html_act = SingleActualite(path+"/"+f)
                 self.actualites_list.append(html_act.get_single_actualite())


    def write_html_actualites(self):

        with open("actualites/template/actualites.html") as actu_f:
            actu_html = actu_f.read()

        actu_soup = BeautifulSoup(actu_html, 'html.parser')
        actu_list = actu_soup.find("div", class_="actualite-list")
       

        #on inverse la liste, pour avoir les articles les plus récents en premiers
        self.actualites_list.reverse()
        
        pos=1
        for act in self.actualites_list:
            hr_tag = actu_soup.new_tag("hr",style="margin-top: 20px;margin-bottom: 20px;")
            actu_list.insert(pos,hr_tag)
            div_tag = actu_soup.new_tag("div", class_ ="actualite-wrapper")
            div_tag.append(act)
            actu_list.insert(pos+1,div_tag)
            pos+=2
        
        return actu_soup.prettify()

        

class SingleActualite:

    md_doc = ""

    def __init__(self,doc):
        self.md_doc = doc


    def openmarkdown(self):
        with open(self.md_doc, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
        f.close()
        return html

    def get_single_actualite(self):
        new_actu = self.openmarkdown()
        new_actu = BeautifulSoup(new_actu, 'html.parser')
        h4 = new_actu.find("h4")
        h4['class'] = h4.get('class',  []) + ['act-title']
        h4['id'] = h4.get('id',  []) + ['act-title']

        return new_actu



