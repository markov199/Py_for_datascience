import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def print_info(img_array:np.ndarray):
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)

def ft_zoom(array:np.ndarray, row_start: int, row_end: int, col_start: int, col_end: int)->np.ndarray:
    try:
        zoomed_array = array[row_start:row_end, col_start:col_end]
        grey = np.mean(zoomed_array, axis=2, dtype=np.uint)
        return (grey)
    except Exception as e:
        print(f"{type(e).__name__} : {e}")

def ft_display(array:np.ndarray, title:str):
    plt.imshow(array, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()


def main():
    try:
        array = ft_load("../animal.jpeg")
        print_info(array)
        zoomed_array = ft_zoom(array, 100, 500, 400, 800)
        print_info(zoomed_array)
        ft_display(zoomed_array, "greyscale")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")




if __name__ == "__main__":
    main()


"""ref
https://www.geeksforgeeks.org/working-images-python/

https://e2eml.school/convert_rgb_to_grayscale

"""