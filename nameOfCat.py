import random

def nameOfCat():
    # Open the first file in read mode
    with open("breedNames.txt", "r") as f1:
        # Read all the lines of the file into a list
        lines1 = f1.readlines()
        # Choose a random line from the list
        line1 = random.choice(lines1)
    
    # Open the second file in read mode
    with open("synonyms.txt", "r") as f2:
        # Read all the lines of the file into a list
        lines2 = f2.readlines()
        # Choose a random line from the list
        line2 = random.choice(lines2)
    
    # # Open the third file in read mode
    # with open("stateOfCat.txt", "r") as f3:
    #     # Read all the lines of the file into a list
    #     lines3 = f3.readlines()
    #     # Choose a random line from the list
    #     line3 = random.choice(lines3)
    
    line1 = line1.strip()
    line2 = line2.strip()
    # line3 = line3.strip()
    # Combine the lines into a single string with a space between them
    # result = " ".join([line1, line2, line3])
    result = " ".join([line1, line2])
    
    # Return the result
    return result
    