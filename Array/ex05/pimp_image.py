from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def ft_display(array, titles):
    fig, axs = plt.subplots(3, 2)
    for ax, img, title in zip(axs.flat, array, titles):
        ax.imshow(img)
        ax.set_title(title)


    # axs[0, 0].imshow(array)
    # axs[0, 0].set_title("Original")

    # axs[0, 1].imshow(invert)
    # axs[0, 1].set_title("Inverted")

    # axs[1, 0].imshow(red)
    # axs[1, 0].set_title("Red")

    # axs[1, 1].imshow(green)
    # axs[1, 1].set_title("Green")

    # axs[2, 0].imshow(blue)
    # axs[2, 0].set_title("Blue")

    # axs[2, 1].imshow(grey)
    # axs[2, 1].set_title("Grey")
    
    # Hide any unused subplots (if there are any)
    for ax in axs.flat:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()


def ft_invert(array:np.ndarray):
    inverted_array = np.zeros_like(array, dtype=array.dtype)
    inverted_array = 255 - array[:,:,:3]
    return inverted_array
    

def ft_red(array:np.ndarray):
    red_array = np.zeros_like(array, dtype=array.dtype)
    red_array[:,:,0] = array[:,:,0]
    return red_array

def ft_blue(array:np.ndarray):
    blue_array = np.zeros_like(array)
    blue_array[:,:,2] = array[:,:,2]
    return blue_array
    
def ft_green(array:np.ndarray):
    green_array = np.zeros_like(array)
    green_array[:,:,1] = array[:,:,1]
    return green_array

def ft_grey(array:np.ndarray):
    sum_array = array.sum(axis=2)
    grey_image = (sum_array /3).astype(np.uint8)
    grey_array = np.stack([grey_image, grey_image, grey_image], axis=2)
    return grey_array

    # astype(np.uint8) ensures that numbers range from 0 to 255
    # np.stack is used to convert into 3d

def main():
    array = ft_load("../landscape.jpg")
    array = array.astype(np.uint8)
    invert = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)

    titles = ["Original", "Inverted", "Red", "Green", "Blue", "Grey"]

    ft_display([array, invert, red, green, blue, grey], titles)

    
if __name__ == "__main__":
    main()