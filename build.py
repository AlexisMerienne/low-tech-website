from click import style
import markdown
from bs4 import BeautifulSoup
from engine.__actualite__ import Actualites

def openmarkdown(file):
    
    with open(file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    f.close()
    return html

def writehtml(file,html):
    with open(file, 'w') as f:
        f.write(html)



if __name__ == '__main__':

    actualites = Actualites()
    actualites.read_file_actualites("actualites")
    output = actualites.write_html_actualites()

    print(output)


    writehtml('build/actualites.html',output)

