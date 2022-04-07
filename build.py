import markdown
from os import listdir
from os.path import isfile, join


from engine.__actualite__ import Actualites
from engine.__dithering__ import Dithering
from engine.__htlmparser__ import HtmlParser



def writehtml(file,html):
    with open(file, 'w') as f:
        f.write(html)



if __name__ == '__main__':

    actualites = Actualites()
    actualites.read_file_actualites("actualites")
    output_ac = actualites.write_html_actualites()
    
    for pic in listdir('images'):
        if isfile(join('images', pic)):
            dithering = Dithering(pic)
            dithering.dither()

    HtmlParser = HtmlParser("apropos/content.md","bilancarbone/content.md","enquete/content.md")



    writehtml('build/actualites.html',output_ac)
    writehtml('build/home.html',HtmlParser.write_html_content_apropos())
    writehtml('build/bilancarbone.html',HtmlParser.write_html_content_bilancarbone())
    writehtml('build/enquete.html',HtmlParser.write_html_content_enquete())
