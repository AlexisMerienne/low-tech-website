import numpy as np
import os
from PIL import Image

GREYSCALE = True
PATH = 'src/images/'

class Dithering:

    im_name = ''
    img = ''
    width = 0
    height = 0

    def __init__(self,im_name):
        # Read in the image, convert to greyscale.
        self.im_name = os.path.splitext(im_name)[0]
        img = Image.open(PATH+im_name)
        if GREYSCALE:
            img = img.convert('L')

        width, height = img.size
        self.width = 400
        self.height = int(height * self.width / width)
        self.img = img.resize((self.width, self.height), Image.ANTIALIAS)

        

  

    def get_new_val(self,old_val,nc):
        """
        Get the "closest" colour to old_val in the range [0,1] per channel divided
        into nc values.

        """

        return np.round(old_val * (nc - 1)) / (nc - 1)

    # For RGB images, the following might give better colour-matching.
    #p = np.linspace(0, 1, nc)
    #p = np.array(list(product(p,p,p)))
    #def get_new_val(old_val):
    #    idx = np.argmin(np.sum((old_val[None,:] - p)**2, axis=1))
    #    return p[idx]

    def fs_dither(self,img, nc):
        """
        Floyd-Steinberg dither the image img into a palette with nc colours per
        channel.

        """

        arr = np.array(img, dtype=float) / 255

        for ir in range(self.height):
            for ic in range(self.width):
                # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
                old_val = arr[ir, ic].copy()
                new_val = self.get_new_val(old_val,nc)
                arr[ir, ic] = new_val
                err = old_val - new_val
                # In this simple example, we will just ignore the border pixels.
                if ic < self.width - 1:
                    arr[ir, ic+1] += err * 7/16
                if ir < self.height - 1:
                    if ic > 0:
                        arr[ir+1, ic-1] += err * 3/16
                    arr[ir+1, ic] += err * 5/16
                    if ic < self.width - 1:
                        arr[ir+1, ic+1] += err / 16

        carr = np.array(arr/np.max(arr, axis=(0,1)) * 255, dtype=np.uint8)
        return Image.fromarray(carr)



    def dither(self):
        img = self.img
        dim = self.fs_dither(img, 4)
        path = 'src/build/assets/'
        dim.save(path+self.im_name+'.jpg'.format(3))
