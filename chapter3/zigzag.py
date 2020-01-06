import time,sys

# familiar with function definitions in python already but practice 
# zigzag 

#number of indents

indent = 0

indentIsIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 0.1 seconds between prints
        if indentIsIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIsIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIsIncreasing = True
except KeyboardInterrupt:
    sys.exit()
