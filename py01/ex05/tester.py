
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey, ft_display
import numpy as np

array = ft_load("../landscape.jpg")
array = array.astype(np.uint8)
invert = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)

titles = ["Original", "Inverted", "Red", "Green", "Blue", "Grey"]

ft_display([array, invert, red, green, blue, grey], titles)
print(ft_invert.__doc__)