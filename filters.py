""" SYSC 1005 A Fall 2015 Lab 4 - Part 3.
"""

from Cimpl import *

#--------------------------------------

def grayscale(img):
    """ (Cimpl.Image) -> None
    
    Convert the specified picture into a grayscale image.
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)
        
def negative(img):
    for pixel in img:
        
        x, y, col = pixel
        
        r, g, b = col
        
        #The opposite of each color becomes the difference between the color and the maximum. To remove the negative off the value found, the absoulute function is needed#
        r = abs(r - 255)
        g = abs(g - 255)
        b = abs(b - 255)
        
        neg = create_color(r, g, b)
        
        set_color(img, x, y, neg)

def weighted_grayscale(img):
    """ (Cimpl.Image) -> None
              
    for pixel in img:
            x, y, col = pixel
            r, g, b = col    
            
            #percentage of each color needed for the grayscale: #
            
            r = r * 0.299
            g = g * 0.587
            b = b * 0.114
            
            #for grayscale, each color has the same brightness, which is a combination of all three colors#
            #Hence, sum of colors for brightness#
            
            brightness = r + g + b
            gray = create_color(brightness,brightness,brightness)
                    
            set_color(img, x, y, gray)   
            
            #---------------------------------------------------------------
            # A filter that checks every pixel's
            # red, green and blue components, individually.
            
def solarize(img, threshold):
                """ (Cimpl.Image) -> None
                
                Solarize the specified image.
                
                >>> image = load_image(choose_file()) 
                >>> solarize(image)
                >>> show(image)     
                """
            
                for x, y, col in img:
                    red, green, blue = col
            
                    # Invert the values of all RGB components that are less than threshold,
                    # leaving components with higher values unchanged.
            
                    if red < threshold:
                        red = 255 - red
            
                    if green < threshold:
                        green = 255 - green
            
                    if blue < threshold:
                        blue = 255 - blue
            
                    col = create_color(red, green, blue)
                    set_color(img, x, y, col)
            
            
def black_and_white(img):
                """ (Cimpl.Image) -> None
                
                Convert the specified image to a black-and-white (two-tone) image.
                
                >>> image = load_image(choose_file()) 
                >>> black_and_white(image)
                >>> show(image)     
                """
            
                black = create_color(0, 0, 0)
                white = create_color(255, 255, 255)
            
                for x, y, col in img:
                    red, green, blue = col
            
                    brightness = (red + green + blue) // 3
                    
                    if brightness < 128:
                        set_color(img, x, y, black)
                    else:     # brightness is between 128 and 255, inclusive
                        set_color(img, x, y, white)
            
            
            #--------------------------------------
            
def black_and_white_and_gray(img):
                """ (Cimpl.Image) -> None
                
                Convert the specified image to a black-and-white-and-gray
                (three-shade) image.
            
                >>> image = load_image(choose_file()) 
                >>> black_and_white_and_gray(image)
                >>> show(image)     
                """
            
                black = create_color(0, 0, 0)
                gray = create_color(128, 128, 128)
                white = create_color(255, 255, 255)
            
                for x, y, col in img:
                    red, green, blue = col
                    
                    brightness = (red + green + blue) // 3
            
                    if brightness < 85:
                        set_color(img, x, y, black)
                    elif brightness < 171: # brightness is between 85 and 170, inclusive
                        set_color(img, x, y, gray)
                    else:                  # brightness is between 171 and 255, inclusive
                        set_color(img, x, y, white)
            
            
            #-----------------------------------------------------------------
            
def extreme_contrast(img):
    """(Cimpl.Image)->None
    Modify img, maximizing the contrast between the light and dark
    pixels"""
    
    for x, y, col in img:
        red, green, blue = col
        
        if red < 128:
            red = 0
        else:
            red = 255
        
        if blue < 128:
            blue = 0
        else:
            blue = 255
            
        if green < 128:
            green = 0
        else:
            green = 255
            
        col = create_color(red, green, blue)
        set_color(img, x, y, col)            
            
def sepia_tint(img):
    
    grayscale(img)
    
    for x, y, col in img:
        red, green, blue = col    
            
        if red < 63:
            blue = blue * 0.9
            red = red * 1.1
            
        elif red < 192:
            blue = blue * 0.85
            red = red * 1.15
            
        else:
            blue = blue * 0.93
            red = red * 1.08
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
       
def _adjust_component(amount):
    """(int) -> int
    Divides the rage 0 to 255 into 4 equal parts. Then, returns midpoint
    of the quandrant in which amount lies """
    
    if amount < 64:
        return 31
    elif 63 < amount < 128:
        return 95
    elif 127 < amount < 192:
        return 159
    else:
        return 223
    
def posterize(img):
    for x, y, col in img:
        red, green, blue = col 
        
        red =  _adjust_component(red)
        blue =  _adjust_component(blue)
        green =  _adjust_component(green)
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)    
        
def simplify(img):
    """(Cimpl.Image)->None
    Modifies img so that each pixel is white, black, red, green or blue. Very bright pixels become white
    Very dark pixels become black
    The rest become red, green or blue based on which component is the largest"""
    
    for x, y, col in img:
        red, green, blue = col   
        
        if red > 200 and blue > 200 and green > 200:
            col = create_color(255, 255, 255)
            
        elif red < 50 and blue < 50 and green < 50:
            col = create_color(0, 0, 0)
            
        elif red > green and red > blue:
            col = create_color(255, 0, 0)
        
        elif green > red and green > blue:
            col = create_color(0, 255, 0)
        else:
            col = create_color(0, 0, 255)
        set_color(img, x, y, col)
    

def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of the image bound to source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @(x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def detect_edges(img, threshold):
    target = copy(img)
    for y in range(0, get_height(img) - 1):
            for x in range(0, get_width(img)): 
                
                top_red, top_green, top_blue = get_color(img, x, y)
                bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
                
                # Average the top components of the pixels
                top = (top_red + top_green + top_blue) // 3 
                
                #Average the bottom components of the pixels
                bottom = (bottom_red + bottom_green + bottom_blue) // 3
                
                contrast = abs(top - bottom)
                
                if contrast > threshold:
                    black = create_color(0, 0, 0)
                    set_color(target, x, y, black)
                    
                else:
                    white = create_color(255,255,255)
                    set_color(target, x, y, white)                    
    
    return target          
                
def detect_edges__better(img, threshold):
    target = copy(img)
    for y in range(0, get_height(img) - 1):
            for x in range(0, get_width(img) - 1): 
                
                top_red, top_green, top_blue = get_color(img, x, y)
                
                bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
                
                right_red, right_green, right_blue = get_color(img, x + 1, y)
                
                # Average the top components of the pixels
                top = (top_red + top_green + top_blue) // 3 
                
                #Average the bottom components of the pixels
                bottom = (bottom_red + bottom_green + bottom_blue) // 3
                
                #Average the right components of the pixels
                right = (right_red + right_green + right_blue) // 3
                
                contrast1 = abs(top - bottom)
                contrast2 = abs(top - right)
                
                if contrast1 > threshold or contrast2 > threshold:
                    black = create_color(0, 0, 0)
                    set_color(target, x, y, black)
                    
                else:
                    white = create_color(255,255,255)
                    set_color(target, x, y, white)                    
    
    return target                          

def blur_better(source):
    target = copy(source)
    for y in range(1, get_height(source) - 1):
            for x in range(1, get_width(source) - 1):
                sum_red = 0
                sum_green= 0
                sum_blue = 0
                for x1 in range(x-1, x+2):
                    for y1 in range(y-1, y+2):
                        r, g, b = get_color(source, x1, y1)
                        
                        sum_red = sum_red + r
                        sum_green = sum_green + g
                        sum_blue = sum_blue + b
                        
                        # Average the components of the 9 pixels
                        new_red = sum_red // 9
                        new_green = sum_green // 9
                        new_blue = sum_blue // 9
                        
                        # Blur the pixel @(x, y) in the copy of the image
                        new_color = create_color(new_red, new_green, new_blue)
                        set_color(target, x, y, new_color)
                        
    return target                        
                        
                    
def flip(img):
    target = copy(img)
    for y in range(0, get_height(img) - 1):
        for x in range(0, get_width(img) - 1):
            midpoint_row = get_width(img) // 2
            midpoint_column = get_height // 2
            
        
             
                    
