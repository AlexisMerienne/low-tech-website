import markdown
from engine.__actualite__ import Actualites



def writehtml(file,html):
    with open(file, 'w') as f:
        f.write(html)



if __name__ == '__main__':

    actualites = Actualites()
    actualites.read_file_actualites("actualites")
    output = actualites.write_html_actualites()


    writehtml('build/actualites.html',output)

