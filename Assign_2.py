#Farabi Hasan;

#This program displays a map of various hurricanes with lines of longitude and
#latitude, hurricane positions, paths, and strengths (via colour indicators).

#Import code from SimpleGraphics.py

from SimpleGraphics import *

#Set the number of times the program is run as count

count = 0

#Allow user to input values for latitude and longitude

#This if statement ensures that when a value of zero is entered, the following
#body statements won't run.
if count == 0:
    latitude = float(input("Enter a value for latitude (0 to stop): "))
    if latitude > 0:
        longitude = float(input("Enter a value for longitude: "))
        wind_speed = float(input("Enter wind speed here: "))

#Add one to count so that once these statements are run once, the condition for
#the previous if statement won't be true
count = count + 1

#Store the dimensions of the image in variables to avoid usage of magic numbers.

map_width = 1022
map_height = 620

#Resizing the window to the image dimensions

resize(map_width, map_height)

#Use loadImage to store the map in a variable

map = loadImage ("map.gif")

#Display the image using drawImage

#Variable assigned for any coordinate of the origin (0, 0)
origin = 0

drawImage (map, origin, origin)

#Draw lines of longitude and latitude

#Store the value for the gap between the latitude and longitude lines
#in a variable.

#Proportion of the latitude to the number of pixels in the height
#Use getWidth() and getHeight() functions to avoid using magic numbers
y_to_lat_proportion = 25 / getHeight()

#Proportion of the longitude to the number of pixels in the width
x_to_long_proportion = 45 / getWidth()

#Difference between latitude origin (Equator) and window origin
lat_difference = 10

#Difference between longitude origin (Prime Meridian) and window origin
long_difference = 95

#Pixel value of spaces between lines of latitude
lat_space = getHeight() / 5

#Pixel value of spaces between lines of longitude
long_space = getWidth() / 9

#Lines of latitude and values displayed through a while loop

#Code for the lines itself
while map_height >= 0:
    setColor ("light gray")
    line (origin, map_height, getWidth(), map_height)

#Code for the text displaying values of latitude
    #Set restrictions on map_height so that 10N and 35N aren't displayed.
    if map_height < getHeight() and map_height > 0:
        #lat_text stores the latitude value converted from the y-value
        lat_text = (getHeight() - map_height) * y_to_lat_proportion + 10
        setFont ("Arial", "12")
        #Move text 3 pixels to the right of the origin for better visibility and
        #make the anchor at the southwest corner of the text box
        text (origin + 3, map_height, "%.iN" % lat_text, "sw")
    #Reassign value of map_height by continously subtracting lat_space to
    #determine the y-coordinae of the next line of latitude.
    map_height = map_height - lat_space

#While loop for creating the lines of longitude and values in text form.
while map_width >= 0:
    setColor ("light gray")
    line (map_width, origin, map_width, getHeight())

#Conversion from x to longitude
    #0.1 added to origin due to approximation of floating point numbers.
    if map_width > origin + .1 and map_width < getWidth():
        long_text = -((map_width) * x_to_long_proportion - 95)
        setFont ("Arial", "12")
        #Move text 3 pixels to the right of the origin for better visibility
        text (map_width + 3, origin, "%.iW" % long_text, "nw")
    map_width = map_width - long_space

#Plotting points on the map

#Store value for number of dots so that lines are only drawn once there are at
#at least two dots on the map.
dot = 0
#Assign a variable for the maximum hurricane category which later helps
#determine which one is the maximum
max_category = 0
#Store wind speed in a variable to help determine max wind speed
stored_wind_speed = 0

#Create a while loop for the points, the repetition of input statements, and
#the lines connecting the points.
while latitude > 0:
    #Series of if-elif-else statements that postition and colour-code each point
    #based on the input wind speed. Conversion from longitude/latitude to x/y
    #values is performed.
    if wind_speed >= 157:
        setColor("purple")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 15, 15)
    elif wind_speed >= 130:
        setColor("red")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 13, 13)
    elif wind_speed >= 111:
        setColor("orange")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 11, 11)
    elif wind_speed >= 96:
        setColor("yellow")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 9, 9)
    elif wind_speed >= 74:
        setColor("green")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 7, 7)
    elif wind_speed < 74:
        setColor("gray")
        ellipse((longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion, 5, 5)
    #Add one to dot variable so that we only draw lines once we have more than
    #one dot (plotted point)
    dot = dot + 1

    if dot > 1:
        #Series of if-elif-else statements that help determine line colours,
        #maximum categories, and maximum wind speeds.
        if wind_speed >= 157:
            setColor ("purple")
            #Add the radius of the plotted points to the x and y coordinates of
            #the ellipses to make the lines travel through the centres of the
            #points instead of their top left corners.
            line(stored_x + 7.5, stored_y + 7.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 7.5)
            #Maximum category stored if category 5 is reached at any point.
            max_category = 5
            #stored_wind speed is only altered if a new wind speed is greater
            #than any of the others through the use of an if statement.
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed
        elif wind_speed >= 130:
            #Using prev_wind_speed (defined at the bottom of the loop; line 242)
            #we can compare the wind speeds of subsequent points and assign
            #colors.
            if prev_wind_speed >= 157:
                setColor("purple")
            else:
                setColor("red")
            line(stored_x + 6.5, stored_y + 6.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 6.5)
            if max_category < 4:
                max_category = 4
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed
        elif wind_speed >= 111:
            if prev_wind_speed >= 157:
                setColor("purple")
            elif prev_wind_speed >= 130:
                setColor("red")
            else:
                setColor("orange")
            line(stored_x + 5.5, stored_y + 5.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 5.5)
            if max_category < 3:
                max_category = 3
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed
        elif wind_speed >= 96:
            if prev_wind_speed >= 157:
                setColor("purple")
            elif prev_wind_speed >= 130:
                setColor("red")
            elif prev_wind_speed >= 111:
                setColor("orange")
            else:
                setColor("yellow")
            line(stored_x + 4.5, stored_y + 4.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 4.5)
            if max_category < 2:
                max_category = 2
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed
        elif wind_speed >= 74:
            if prev_wind_speed >= 157:
                setColor("purple")
            elif prev_wind_speed >= 130:
                setColor("red")
            elif prev_wind_speed >= 111:
                setColor("orange")
            elif prev_wind_speed >= 96:
                setColor("yellow")
            else:
                setColor("green")
            line(stored_x + 3.5, stored_y + 3.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 3.5)
            if max_category < 1:
                max_category = 1
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed
        else:
            if prev_wind_speed >= 157:
                setColor("purple")
            elif prev_wind_speed >= 130:
                setColor("red")
            elif prev_wind_speed >= 111:
                setColor("orange")
            elif prev_wind_speed >= 96:
                setColor("yellow")
            elif prev_wind_speed >= 74:
                setColor("green")
            else:
                setColor("gray")
            line(stored_x + 2.5, stored_y + 2.5, (longitude + long_difference) * 1 / x_to_long_proportion, getHeight() - (latitude - 10) * 1 / y_to_lat_proportion + 2.5)
            if max_category < 1:
                max_category = 0
            if stored_wind_speed < wind_speed:
                stored_wind_speed = wind_speed

    #Stored x and y coordinates from previous dot for the coordinates of the
    #lines connecting each of the dots.
    stored_x = (longitude + long_difference) * 1 / x_to_long_proportion

    stored_y = getHeight() - (latitude - 10) * 1 / y_to_lat_proportion

    #Store previous wind speed in a variable to help determine the colours of
    #connecting lines.
    prev_wind_speed = wind_speed

    #Repeat input statement until a value of zero is entered for latitude.
    latitude = float(input("Enter a value for latitude (0 to stop): "))
    #If a zero is entered for latitude, we will want the program to stop
    #requesting values and display a message (line 259)
    if latitude != 0:
        longitude = float(input("Enter a value for longitude: "))
        wind_speed = float(input("Enter wind speed here: "))

#Code for displaying the Maximum Category in the top right corner of the map,
#where the coordinates of the text box are given for the northeast corner. 5 is
#subtracted from the total width and 20 added to the origin for better
#visibility.
setColor("light gray")
setFont ("Arial", "13.5")
text(getWidth() - 5, origin + 20, "Max. Category: %.i" % max_category, "ne")

#Code for displaying the Max Wind Speed in mph which is 20 pixels below the text
#for the maximum category.
setColor("light gray")
setFont ("Arial", "13.5")
text(getWidth() - 5, origin + 40, "Max. Wind Speed (mph): %.1f" % stored_wind_speed, "ne")

#Message displayed once a 0 is entered in latitude
print("You cannot enter any more values.")
