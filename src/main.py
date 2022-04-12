
from os import listdir
from os.path import isfile, join


from src.engine.__actualite__ import Actualites
from src.engine.__dithering__ import Dithering
from src.engine.__htlmparser__ import HtmlParser



def writehtml(file,html):
    with open(file, 'w') as f:
        f.write(html)



if __name__ == '__main__':

    actualites = Actualites()
    actualites.read_file_actualites("src/content/actualites")
    output_ac = actualites.write_html_actualites()
    
    for pic in listdir('src/images'):
        if isfile(join('src/images', pic)):
            dithering = Dithering(pic)
            dithering.dither()

    HtmlParser = HtmlParser("src/content/apropos/content.md","src/content/bilancarbone/content.md","src/content/enquete/content.md")



    writehtml('src/build/actualites.html',output_ac)
    writehtml('src/build/home.html',HtmlParser.write_html_content_apropos())
    writehtml('src/build/bilancarbone.html',HtmlParser.write_html_content_bilancarbone())
    writehtml('src/build/enquete.html',HtmlParser.write_html_content_enquete())
