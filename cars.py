# Importing needed things
import xml.etree.ElementTree as ET
from enum import Enum
import os

# Adding Enum Actions
class Actions(Enum):
    PRINT = 1
    ADD = 2
    DELETE = 3
    UPDATE = 4
    EXIT = 5
    CHANGE_COLOR = 6

# Create the root element
root = ET.Element("animals")

# Create animal elements with attributes and text
animal1 = ET.SubElement(root, "animal")
animal1.set("animal", "Monkey")
animal1.set("gender", "male")
animal1.set("age", "12")

# Animal 2
animal2 = ET.SubElement(root, "animal")
animal2.set("animal", "Lion")
animal2.set("gender", "male")
animal2.set("age", "5")

# Animal 3
animal3 = ET.SubElement(root, "animal")
animal3.set("animal", "Zebra")
animal3.set("gender", "female")
animal3.set("age", "9")

# Convert the XML structure to a string
xml_str = ET.tostring(root, encoding="utf-8")

# Write the XML string to a file
with open("animal_list.xml", "wb") as f:
    f.write(xml_str)

# Def cleanScreen- cleans all screen inside terminal
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Def displayMenu- Displays the start up menu 
def displayMenu():
    for x in Actions: print(f'{x.value} - {x.name}')
    return Actions(int(input("your selection: ")))

# Def menu- The main menu of the program
def menu():
    while (True):
        userSelection = displayMenu()
        if userSelection == Actions.PRINT : printAnimals()
        if userSelection == Actions.ADD : pass
        if userSelection == Actions.DELETE: deleteAnimal()
        if userSelection == Actions.UPDATE : pass
        if userSelection == Actions.EXIT: return
        if userSelection == Actions.CHANGE_COLOR : changeColor()


# Def printAnimals- prints all animals inside XML file
def printAnimals():
    # Parse the XML file
    tree = ET.parse("animal_list.xml")
    root = tree.getroot()
    # Iterate through the animal elements and print their text content
    for animal_element in root.findall("animal"):
        print("Animal:", animal_element.text)

# Def addAnimal- add new animal to the list
def addAnimal():
    pass

# Def deleteAnimal- deletes an animal in the list
def deleteAnimal():
    userDelete = input("enter animal to delete")
    import xml.etree.ElementTree as ET
    tree = ET.parse('animal_list.xml')  # Replace with your XML file name
    root = tree.getroot()               # Get the root element
    item_to_delete = root.find(userDelete)  # Replace 'item' with the tag of the item you want to delete
    tree.write('animal_list.xml')  # Replace with the desired output file name


# Def updateAnimal- search for element in the list then change its value
def updateAnimal():
    pass

# Def changeColor- changes the color inside terminal
def changeColor():
    print(RED + "This text is red.")

# Def findAnimal- finds an animal inside of the list
def findAnimal():
    found = False
    foundAnimal = ""
    search =input("give me name to search")
    if foundAnimal["name"]==search:
            found =True
            found_contact =contact
    if found :
        print(foundAnimal)
        return foundAnimal
    return None


if __name__ == '__main__':
    clearScreen()
    menu()