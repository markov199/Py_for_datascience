import  numpy as np
from PIL import Image

def ft_load(path: str) : 
    im = Image.open(path)
    print(f"Format of image : {im.format}")
    img_array = np.array(im)
    print(f"The shape of image is: {img_array.shape}")
    return img_array

"""
ref
https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
"""






""" ref
https://www.tutorialspoint.com/downloading-files-from-web-using-python
https://www.geeksforgeeks.org/check-if-a-file-is-valid-image-with-python/
https://www.dash.app/blog/png-vs-jpg
https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
"""