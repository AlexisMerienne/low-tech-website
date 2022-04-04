import markdown
from engine.__actualite__ import Actualites
from engine.__htlmparser__ import HtmlParser



def writehtml(file,html):
    with open(file, 'w') as f:
        f.write(html)



if __name__ == '__main__':

    actualites = Actualites()
    actualites.read_file_actualites("actualites")
    output_ac = actualites.write_html_actualites()

    HtmlParser = HtmlParser("apropos/content.md","","")



    writehtml('build/actualites.html',output_ac)
    writehtml('build/home.html',HtmlParser.write_html_content_apropos())
