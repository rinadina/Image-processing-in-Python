# SYSC 1005 Fall 2015
# Implementing Lookup Tables Using Lists

from Cimpl import *

def build_solarize_lookup_table(threshold):
    """ Return a lookup table for a solarizing filter.
    The table is initialized so that only those RGB components with intensities
    less than the specified threshold will be modified:
       For a component c, c < threshold, the new component value is 255 - c.
       For a component c, c >= threshold, the new component value is c; i.e,
       the component is unchanged.
    """
    lookup = []

    # Initialize the table so that, for component c, lookup[c] contains the
    # new value for that component.
    
    for c in range(256):
        if c < threshold:
            lookup.append(255 - c)
        else:
            lookup.append(c)

    return lookup

# Create three lookup tables for the solarizing function, every time this 
# module is loaded into the Python interpreter; e.g., by clicking Run.

solarize_64_table = build_solarize_lookup_table(64)
solarize_128_table = build_solarize_lookup_table(128)
solarize_196_table = build_solarize_lookup_table(196)

def solarize(img, solarize_table):
    """
    Solarize the specified image, using lookup table solarize_table to 
    obtain the RGB components for the solarized image.
    """
    for x, y, col in img:
        red, green, blue = col
        
        # Use the lookup table to find the solarized values of the
        # red, green and blue components.
        red = solarize_table[red] 
        green = solarize_table[green]
        blue = solarize_table[blue]
        
        col = create_color(red, green, blue)
        set_color(img, x, y, col)
    
def test_solarize_lookup():  
    original = load_image(choose_file())  
    
    img = copy(original)    
    solarize(img, solarize_64_table)
    show(img)
    
    img = copy(original)          
    solarize(img, solarize_128_table)
    show(img) 
    
    img = copy(original)  
    solarize(img, solarize_196_table)
    show(img)    
