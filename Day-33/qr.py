from pyqrcode import *
import png

s = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

url = pyqrcode.create(s)

url.png('rick-roll.png', scale=9)