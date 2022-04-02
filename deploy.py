import shutil


if __name__ == '__main__':
    original = r'build/actualites.html'
    target = r'output/views/actualites.html'

    shutil.copyfile(original, target)


