import shutil


if __name__ == '__main__':
    original_ac = r'build/actualites.html'
    target_ac = r'output/views/actualites.html'

    original_home = r'build/home.html'
    target_home = r'output/home.html'

    shutil.copyfile(original_ac, target_ac)
    shutil.copyfile(original_home, target_home)


