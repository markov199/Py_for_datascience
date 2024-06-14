import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def print_info(img_array:np.ndarray):
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)

def ft_crop(array:np.ndarray, row_start: int, row_end: int, col_start: int, col_end: int)->np.ndarray:
    try:
        cropped_array = array[row_start:row_end, col_start:col_end]
        return (cropped_array)
    except Exception as e:
        print(f"{type(e).__name__} : {e}")

def ft_display(array:np.ndarray, title:str):
    plt.imshow(array, cmap='gray')
    plt.title(title)
    plt.axis('on')
    plt.show()

def ft_tranpose(array:np.ndarray):
    try:
        x,y,z = array.shape
        new_array = np.zeros((y,x,z), dtype=array.dtype)
        for i in range(y):
            for j in range(x):
                for k in range(z):
                    new_array[i][j][k] = array[j][i][k]
        return (new_array[:,:,0:1])

    except Exception as e:
        print(f"{type(e).__name__} : {e}")

def main():
    try:
        array = ft_load("../animal.jpeg")
        cropped_array = ft_crop(array,150, 550, 400, 800)
        transposed_array = ft_tranpose(cropped_array)
        ft_display(transposed_array, "transposed")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")



if __name__ == "__main__":
    main()