from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
 #initialize the fonts list
fonts = []
fonts = figlet.getFonts()
#get text from the user

if len(sys.argv) == 1:
    isRandomFont = True

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
    isRandomFont = False

else:
    sys.exit(1)



if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print ("Invalid usage")
        sys.exit(1)
else:
    f = random.choice(fonts)# get a random font from the fonts list
    figlet.setFont(font=random.choice(fonts))


s = input("Input: ")
print("Output: ")
print(figlet.renderText(s))

