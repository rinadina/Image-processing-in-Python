
from Cimpl import*

def build_hot_metal_lookup_table(): 

    lookup_table = []
    
    for brightness in range(256):
        if 0 <= brightness < 170:
            r = 1.5 * brightness
            new_red = r
            new_green = 0
            new_blue = 0
            col = create_color(new_red, new_green, new_blue)
            lookup_table.append(col)
        else:
            g = (3 * brightness) - 510
            new_green = g
            new_red = 255
            new_blue = 0
            col = create_color(new_red, new_green, new_blue)
            lookup_table.append(col)
            
    return lookup_table 

hot_metal_table=build_hot_metal_lookup_table()

def hot_metal(img, table):
    for x, y, col in img:
        red, green, blue = col
        brightness = int(0.3 * red + 0.59 * green + 0.11 * blue)
        
        new_color = table[brightness]
        
        set_color(img, x, y, new_color)    