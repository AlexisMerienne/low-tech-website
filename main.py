from click import style
import markdown
from bs4 import BeautifulSoup

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

    with open("output/views/actualites.html") as actu_f:
        actu_html = actu_f.read()

    actu_soup = BeautifulSoup(actu_html, 'html.parser')

    actu_list = actu_soup.find("div", class_="actualite-list")
    hr_tag = actu_soup.new_tag("hr",style="margin-top: 20px;margin-bottom: 20px;")
    actu_list.append(hr_tag)
    div_tag = actu_soup.new_tag("div", class_ ="actualite-wrapper")
   

    html = openmarkdown('actualite/impactometre_numerique.md')
    new_actu = BeautifulSoup(html, 'html.parser')
    h4 = new_actu.find("h4")
    h4['class'] = h4.get('class',  []) + ['act-title']
    h4['id'] = h4.get('id',  []) + ['act-title']

    div_tag.append(new_actu)

    actu_list.insert(1,div_tag)
    
   
    output = actu_soup.prettify()

    writehtml('output/views/actualites.html',output)

