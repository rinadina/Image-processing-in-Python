 Matrix convolution and image processing.

A convolution kernel is a square matrix; for example:

    |c00  c01  c02|
C = |c10  c11  c12|
    |c20  c21  c22|

from Cimpl import *

def convolution_filter(img, kernels, name):
    """ Return a new image created from the picture bound to img,
    using the specified 3-by-3 convolution kernel.
    """

    # Create a blank image that's the same size as the original image.
    # The filter modifies this image, so that the convolution always uses
    # pixels from the original image, instead of pixels that have been
    # been modified.

    dest = create_image(get_width(img), get_height(img))
    
    kernel = kernels[name]

    for y in range(1, get_height(img)-1):
        for x in range(1, get_width(img)-1):
            
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            divisor = 0

            # NW (north west corner)
            r, g, b = get_color(img, x-1, y-1)
            sum_red = sum_red + r * kernel[0][0]
            sum_green = sum_green + g * kernel[0][0]
            sum_blue = sum_blue + b * kernel[0][0]
            divisor = divisor + kernel[0][0]

            # N
            r, g, b = get_color(img, x, y-1)
            sum_red = sum_red + r * kernel[0][1]
            sum_green = sum_green + g * kernel[0][1]
            sum_blue = sum_blue + b * kernel[0][1]
            divisor = divisor + kernel[0][1]

            # NE
            r, g, b = get_color(img, x+1, y-1)
            sum_red = sum_red + r * kernel[0][2]
            sum_green = sum_green + g * kernel[0][2]
            sum_blue = sum_blue + b * kernel[0][2]
            divisor = divisor + kernel[0][2]

            # W
            r, g, b = get_color(img, x-1, y)
            sum_red = sum_red + r * kernel[1][0]
            sum_green = sum_green + g * kernel[1][0]
            sum_blue = sum_blue + b * kernel[1][0]
            divisor = divisor + kernel[1][0]

            # center
            r, g, b = get_color(img, x, y)
            sum_red = sum_red + r * kernel[1][1]
            sum_green = sum_green + g * kernel[1][1]
            sum_blue = sum_blue + b * kernel[1][1]
            divisor = divisor + kernel[1][1]

            # E
            r, g, b = get_color(img, x+1, y)
            sum_red = sum_red + r * kernel[1][2]
            sum_green = sum_green + g * kernel[1][2]
            sum_blue = sum_blue + b * kernel[1][2]
            divisor = divisor + kernel[1][2]

            # SW
            r, g, b = get_color(img, x-1, y+1)
            sum_red = sum_red + r * kernel[2][0]
            sum_green = sum_green + g * kernel[2][0]
            sum_blue = sum_blue + b * kernel[2][0]
            divisor = divisor + kernel[2][0]

            # S
            r, g, b = get_color(img, x, y+1)
            sum_red = sum_red + r * kernel[2][1]
            sum_green = sum_green + g * kernel[2][1]
            sum_blue = sum_blue + b * kernel[2][1]
            divisor = divisor + kernel[2][1]

            # SE
            r, g, b = get_color(img, x+1, y+1)
            sum_red = sum_red + r * kernel[2][2]
            sum_green = sum_green + g * kernel[2][2]
            sum_blue = sum_blue + b * kernel[2][2]
            divisor = divisor + kernel[2][2]

            # To normalize the new component values, divide them by the sum
            # of the values in the kernel. If the divisor is 0, divide by 1.
            if divisor == 0:
                divisor = 1

            new_red = sum_red // divisor

            new_red = min(max(new_red, 0), 255)

            new_green = sum_green // divisor
            new_green = min(max(new_green, 0), 255)

            new_blue = sum_blue // divisor
            new_blue = min(max(new_blue, 0), 255)

            col = create_color(new_red, new_green, new_blue)
            set_color(dest, x, y, col)

    # all the pixels except those on the edges
    # are made to black.

    black = create_color(0, 0, 0)

    bottom_row = get_height(img) - 1
    for x in range(get_width(img)):
        set_color(dest, x, 0, black)
        set_color(dest, x, bottom_row, black)

    right_column = get_width(img) - 1
    for y in range(get_height(img)):
        set_color(dest, 0, y, black)
        set_color(dest, right_column, y, black)

    return dest

blur_kernel = (
    (1, 1, 1),  # top row
    (1, 1, 1),  # middle row
    (1, 1, 1)   # bottom row
)

def test_convolution_filter():
    original = load_image(choose_file())
    show(original)
    
    new_image = convolution_filter(original, blur_kernel)
    show(new_image)
    # save_as(new_image, "convolution_blur.jpg")

def build_kernel_table():
    dict = {}
    dict["blur"] = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    dict["sharpen"] = ((0, -3, 0), (-3, 21, -3), (0, -3, 0))
    dict["emboss"] = ((-18, -9, 0), (-9, 9, 9), (0, 9, 18))
    dict["edge detect 1"] = ((0, 9, 0), (9, -36, 9), (0, 9, 0))
    dict["edge detect 2"] = ((-9, -9, -9), (-9, 72, -9), (-9, -9, -9))
    
    return dict
    
