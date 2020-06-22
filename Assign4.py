#Farabi Hasan; UCID: 30110302

#This program contains code that displays certain features of a food web by
#creating and calling a set of functions.

import sys

##############################################################################
## Format a list of items so that they are comma separated and "and" appears
#  before the last item.
##############################################################################
#  Parameters:
#    data: the list of items to format
#  Returns: A string containing the items from data with nice formatting
def formatList(data):
  # Handle the case where the list is empty
  if len(data) == 0:
    return "(None)"

  # Start with an empty string that we will add items to
  retval = ""

  # Handle all of the items except for the last two
  for i in range(0, len(data) - 2):
    retval = retval + str(data[i]) + ", "

  # Handle the second last item
  if len(data) >= 2:
    retval += str(data[-2]) + " and "

  # Handle the last item
  retval += str(data[-1])

  # Return the result
  return retval


##########################################################################
### Part 1: What do the Predators Eat?
### This function first opens, then reads the file, and then creates the most
### important dictionary consisting of the different predators in the food web
### as its keys and the corresponding prey, either singular or in list form, as
### the key's (predator's) value
##########################################################################
# Parameters:
#   fileName: the file name entered in by the user
# Returns: the dictionary with the predators as keys and prey as values
def PredatorPrey(fileName):
    #Use a try and except block to check if file actually exists
    try:
        #Open file, and set to the read property
        fileText = open(fileName, "r")
    #Display error message and quit program for FileNotFoundErrors
    except FileNotFoundError:
        print("The file you have entered does not exist.")
        quit()

    foodWeb = {}

    for line in fileText.readlines():
        #Clear the whitespace and separate each line of text by commas
        new = line.strip().split(",")
        #Set the first word (index of zero) as the key (predator) and the
        #remaining word equal to the value in the form of a list
        foodWeb [new[0]] = new[1:]

    #Close the file
    fileText.close()

    return foodWeb

##########################################################################
### Part 2: Apex Predators
### This function creates a list of all the Apex Predators.
##########################################################################
# Parameters:
#   foodWeb: a dictionary with items (predator-prey dictionary)
# Returns: a list of the apex predators

def ApexPredators(foodWeb):

    ApexPred = []

    for pred in foodWeb.keys():
        #Initialize predApex to true
        predApex = True
        for key in foodWeb.keys():
            if pred in foodWeb[key]:
                #If the animal is in the list of prey, set predApex to false
                predApex = False
        if predApex:
            #If it is not present in any list of prey, add the animal to list
            #of apex predators
            ApexPred.append(pred)

    return ApexPred

##########################################################################
## Part 3: Producers
### This function creates a list of the producers in the food web (are only
### prey)
##########################################################################
# Parameters:
#   foodWeb: a dictionary with items (predator-prey dictionary)
# Returns: a list of all the producers

def Producers(foodWeb):
    allPrey = []
    allProducers = []
    #Place all the prey of the food web into a list
    for key in foodWeb.keys():
        for prey in foodWeb[key]:
            if prey not in allPrey:
                allPrey.append(prey)

    for producers in allPrey:
        #If the prey is not present in the list of keys (predators), it is a
        #producer, which is then added to the list of producers
        if producers not in foodWeb.keys():
            allProducers.append(producers)
    return allProducers

##########################################################################
## Part 4: Most Flexible Organism
### This function creates a list of the most flexible organism(s) in the food
### web (eat the most prey)
##########################################################################
# Parameters:
#   foodWeb: a dictionary with items (predator-prey dictionary)
# Returns: a list of the most flexible organism(s)

def Flex(foodWeb):
    MostFlex = []
    count = 0
    for key in foodWeb.keys():
        #For the very first predator, add it to the empty list because we cannot
        #compare it with any other values
        if count == 0:
            MostFlex.append(key)
            #Set the count to 1 so that we always compare from now on
            count = count + 1
            mostPrey = len(foodWeb[key])
        else:
            #If the list of prey is greater than the previous record, we must
            #clear the list and add the current predator to a lone list
            if len(foodWeb[key]) > mostPrey:
                MostFlex.clear()
                MostFlex.append(key)
                mostPrey = len(foodWeb[key])
            #If the list of prey is equal to the previous record, add the
            #current predator to the list
            elif len(foodWeb[key]) == mostPrey:
                MostFlex.append(key)
    return MostFlex

##########################################################################
## Part 5: The Tastiest Organism
### This function creates a list of the tastiest organism(s) in the food web
### (are eaten the most)
##########################################################################
# Parameters:
#   foodWeb: a dictionary with items (predator-prey dictionary)
# Returns: a list of the tastiest organism(s)

def Tasty(foodWeb):
    TastyOrg = []
    count = 0
    for allPrey in foodWeb.values():
        for prey in allPrey:
            #Set the predatorCount to zero for each prey in the web
            predatorCount = 0
            for pred in foodWeb.keys():
                for OnePredsPrey in foodWeb[pred]:
                    if prey in OnePredsPrey:
                        #Increase the count by one for every predator that the
                        #prey is listed in
                        predatorCount = predatorCount + 1
                        #For the very first prey, we add it to the list of
                        #tastiest organisms as we cannot compare it with
                        #previous values
                        if count == 0:
                            TastyOrg.append(prey)
                            mostPred = predatorCount
                            count = count + 1
                        else:
                            #If the number of predators for a specific prey
                            #exceeds the previous record, we clear the list
                            #of prey and add the current prey to an empty list
                            if predatorCount > mostPred:
                                TastyOrg.clear()
                                TastyOrg.append(prey)
                            #If the number of predators equals the previous
                            #record, we add the prey to the list
                            elif predatorCount == mostPred:
                                TastyOrg.append(prey)
    return TastyOrg

##########################################################################
## Part 6: Determining Height
### This function determines the height (longest possible path to a producer)
### of each organism in the food web and sorts it in a dictionary
##########################################################################
# Parameters:
#   foodWeb: a dictionary with items (predator-prey dictionary)
# Returns: a dictionary where the keys are all the organisms listed in
# alphabetical order, whereas the values are the heights of the organisms

def Height(foodWeb):
    height_dict = {}
    for pred in foodWeb.keys():
        height_dict[pred] = 0
    for MultiplePrey in foodWeb.values():
        for PreyList in MultiplePrey:
            if PreyList not in height_dict.keys():
                    height_dict[PreyList] = 0

    new_height_dict = sorted(height_dict)

    height_dict.clear()

    for key in new_height_dict:
        height_dict[key] = 0

    changed = True

    while changed:
        changed = False
        for predators in foodWeb.keys():
            allPrey = foodWeb[predators]
            for prey in allPrey:
                if height_dict[predators] <= height_dict[prey]:
                    height_dict[predators] = height_dict[prey] + 1
                    changed = True

    return height_dict

##########################################################################
## Main Function
### This function determines the file name and calls all the previously created
### functions and prints all the stats in a certain sequence
##########################################################################
# Parameters:
#   None
# Returns: None (only prints strings)

def main():

    #If a command line argument is provided, then it will be the file name
    #(second in the list)

    if len(sys.argv) == 2:
        fileName = sys.argv[1]

    #Ask the user to input a file name if no command line argument is
    #provided
    if len(sys.argv) < 2:
        fileName = input("Enter the name of a file: ")

    #Display an error message and quit if more than a single command
    #line argument is provided
    if len(sys.argv) > 2:
        print("This program must be started with one command line parameter.")
        print("Quitting...")
        quit()

    #Assign the dictionary to a variable for use
    foodWeb = PredatorPrey(fileName)

    #Series of print statements which print different stats (parts)on specific
    #line sequences, where most are formatted through the formatList function
    for pred in foodWeb.keys():
        print(pred,"eats",formatList(foodWeb[pred]))

    print("Apex Predators:", formatList(ApexPredators(foodWeb)))

    print("Producers:", formatList(Producers(foodWeb)))

    print("Most Flexible Eaters:", formatList(Flex(foodWeb)))

    print("Tastiest:", formatList(Tasty(foodWeb)))

    print("Heights: ")

    #Assign the dictionary of the heights created in the "Heights" function to
    #a variable
    heights = Height(foodWeb)

    #Create a for loop so that heights are displayed on separate lines
    for animal in heights.keys():
        print("", animal + ":", heights[animal])

#Call the main function to display and run everything
main()
