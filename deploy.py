import shutil
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    original_ac = r'src/build/actualites.html'
    target_ac = r'output/views/actualites.html'

    original_home = r'src/build/home.html'
    target_home = r'output/home.html'

    original_bc = r'src/build/bilancarbone.html'
    target_bc = r'output/views/bilancarbone.html'

    original_enq = r'src/build/enquete.html'
    target_enq = r'output/views/enquete.html'

    srcasset = 'src/build/assets'
    for f in listdir(srcasset):
             if isfile(join(srcasset, f)):
                original_assets = r''+srcasset+'/'+f
                target_assets = r'output/assets/'+f
                shutil.copyfile(original_assets, target_assets)
                

    shutil.copyfile(original_ac, target_ac)
    shutil.copyfile(original_home, target_home)
    shutil.copyfile(original_bc, target_bc)
    shutil.copyfile(original_enq, target_enq)


