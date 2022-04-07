import shutil
from distutils.dir_util import copy_tree

if __name__ == '__main__':
    original_ac = r'build/actualites.html'
    target_ac = r'output/views/actualites.html'

    original_home = r'build/home.html'
    target_home = r'output/home.html'

    original_bc = r'build/bilancarbone.html'
    target_bc = r'output/views/bilancarbone.html'

    original_enq = r'build/enquete.html'
    target_enq = r'output/views/enquete.html'

    original_assets = 'build/assets'
    target_assets = 'output/assets'

    shutil.copyfile(original_ac, target_ac)
    shutil.copyfile(original_home, target_home)
    shutil.copyfile(original_bc, target_bc)
    shutil.copyfile(original_enq, target_enq)
    copy_tree(original_assets, target_assets)


