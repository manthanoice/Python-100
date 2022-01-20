# format a output using string() method
cstr = 'eh idk man'
# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '$'))
# Printing the left aligned string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
# Printing the right aligned string with "-" padding
print ("The right aligned string is : ")
print (cstr.rjust(40, ' '))