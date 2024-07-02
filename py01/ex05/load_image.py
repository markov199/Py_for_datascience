import  numpy as np
from PIL import Image

def ft_load(path: str)->np.ndarray:
    try:

        im = Image.open(path)
        img_array = np.array(im)
        return img_array
    except Exception as e:
        print(f"{type(e).__name__} : {e}")