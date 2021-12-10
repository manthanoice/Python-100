from PIL.Image import new
import colorgram

colors = colorgram.extract('E:\Python 100\Day-18\hirst.jpg', 40)

the_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    the_list.append(new_color)

print(the_list)