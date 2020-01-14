#! python3
import webbrowser,sys,pyperclip
#mapit launches browser and to google maps
#webbrowser.open('https://inventwithpython.com/')

if len(sys.argv) > 1:
    # get the address from the command line
    inputAddress = '+'.join(sys.argv[1:])

else:
    inputAddress = '+'.join(pyperclip.paste())


webbrowser.open('https://www.google.com/maps/place/' + inputAddress)


