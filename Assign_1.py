#Farabi Hasan ; UCID: 30110302

#This program codes for a clown face that is positioned in the window in response to user input.

#Import code from SimpleGraphics.py file

from SimpleGraphics import *

x_offset = int(input("Enter a number here: ")) - 150

y_offset = int(input("Enter a number here: ")) - 150

#Change the background colour to black

background("black")

#Code for the white body of the clown emoji

setColor("white")
ellipse (x_offset, y_offset, 300, 300)

#Code for the eyes consisting of three separate ellipses for each eye

setColor ("steel blue")
ellipse (x_offset + 70, y_offset + 59, 60, 100)

setColor ("steel blue")
ellipse (x_offset + 160, y_offset + 59, 60, 100)

setColor("white")
ellipse (x_offset + 80, y_offset + 70, 40, 80)

setColor ("white")
ellipse (x_offset + 170, y_offset + 70, 40, 80)

setColor("black")
ellipse (x_offset + 90, y_offset + 82.5, 20, 50)

setColor("black")
ellipse (x_offset + 180, y_offset + 82.5, 20, 50)

#Code for left (from perspective of user) eyelashes

setColor ("black")
line (x_offset + 100, y_offset + 59, x_offset + 100, y_offset + 44)
line (x_offset + 114, y_offset + 64, x_offset + 124, y_offset + 49)
line (x_offset + 86, y_offset + 64, x_offset + 76, y_offset + 49)

#Code for right (from perspective of user) eyelashes

setColor ("black")
line (x_offset + 190, y_offset + 59, x_offset + 190, y_offset + 44)
line (x_offset + 204, y_offset + 64, x_offset + 214, y_offset + 49)
line (x_offset + 176, y_offset + 64, x_offset + 166, y_offset + 49)

#Code for the nose

setColor("red")
ellipse (x_offset + 127.5, y_offset + 135, 35, 35)


#Code for the mouth

setColor ("firebrick4")
blob (x_offset + 40, y_offset + 180, x_offset + 145, y_offset + 230, x_offset + 250, y_offset + 180, x_offset + 145, y_offset + 260)

#Code for blush

setColor ("pink")
ellipse (x_offset + 20, y_offset + 152, 40, 40)
ellipse (x_offset + 230, y_offset + 152, 40, 40)

setColor ("pink2")
ellipse (x_offset + 25, y_offset + 157, 30, 30)
ellipse (x_offset + 235, y_offset + 157, 30, 30)

#Code for red hair

setColor ("red2")
ellipse (x_offset + 250, y_offset + 35, 50, 50)
ellipse (x_offset + 235, y_offset + 20, 50, 50)
ellipse (x_offset + 215, y_offset + 5, 50, 50)
ellipse (x_offset, y_offset + 35, 50, 50)
ellipse (x_offset + 15, y_offset + 20, 50, 50)
ellipse (x_offset + 30, y_offset + 5, 50, 50)

#Code for the crown

#Crown frame

setColor ("gold1")
polygon (x_offset + 90, y_offset + 25, x_offset + 205, y_offset + 25, x_offset + 225, y_offset - 65, x_offset + 185, y_offset - 10, x_offset + 145, y_offset - 65, x_offset + 105, y_offset - 10, x_offset + 65, y_offset - 65)

#Balls on top of crown

setColor ("gold")
ellipse (x_offset + 212.5, y_offset - 90, 25, 25)
ellipse (x_offset + 132.5, y_offset - 90, 25, 25)
ellipse (x_offset + 52.5, y_offset - 90, 25, 25)

#Gems on the crown

#Code for left-most red gem

setOutline ("black")
setFill ("red")
ellipse (x_offset + 95, y_offset - 5, 25, 25)

#Code for large central red gem

setOutline ("black")
setFill ("red")
ellipse (x_offset + 125, y_offset - 5, 45, 25)

#Code for right-most red gem

setOutline ("black")
setFill ("red")
ellipse (x_offset + 175, y_offset - 5, 25, 25)

#Code for the text, which is centered just below the clown face

setColor ("firebrick2")
setFont ("Arial", "48", "bold")
text (400, 500, "Shaun the Clown")
