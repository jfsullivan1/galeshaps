# John Sullivan & Shane Wallerick
# marriage.py
# CSC440
# 1/30/2020

import sys
import time

stopwatch = time.time()

# =================================================================================
# INVARIANTS: 
# - Any person will always have n preferences for marriage partners. (The given n)
# - There will always be n * 2 total people. 
# - If a lady is removed from one of the knights preferences list, it means she preferred someone else over him. 
# - Any engaged lady finds her current partner more desirable than any previous partners. 
# =================================================================================

def ReadFile():

    # Setup
    args = sys.argv

    # Try to open file 
    try:
        dataFile = open(args[1], "r")
    except(IndexError):
        exit(1)

    marriedCouples = {}
    singleKnights = []
    knights = {}
    ladies = {}
    line = dataFile.readline()

    # Get the 'n' amount of people from the first line in the file 
    try:
        n = int(line)
    except(ValueError):
        exit(1)

    # Fill up the knights and ladies dictionaries. 
    # Dictionary will contain a name as the key followed by their preferences as the value.
    # Example,    Henry : [Mary, Cindy, Barbara]
    for index, line in enumerate(dataFile):

        # First, we are going to make sure the file is formatted correctly. 
        # This simply checks the length of the preferences to see if it's correct length.  
        if len(line.split()[1:]) > n or len(line.split()[1:]) < n:
            exit(1)

        # Here, everything is sorted into dictionaries. 
        if(index < n):
            knights [line.split()[0]] = line.split()[1:]
            singleKnights.append(line.split()[0])
        else:
            ladies [line.split()[0]] = line.split()[1:]

    marriedCouples = Matchmaking(knights, ladies, singleKnights, marriedCouples)
    
    return marriedCouples

def Matchmaking(knights, ladies, singleKnights, marriedCouples):
    # =======================================================================
    # Invariants: 
    # - At the end of every loop, each lady is either married or has not been proposed to by a knight. 
    # - At the end of every loop, our set of married couples is a matching. 
    # =======================================================================
    while singleKnights:
        knight = singleKnights.pop(0)
        lady = knights[knight].pop(0)

        if(marriedCouples.get(lady)):
            
            # Checks if the position of current husband based on preference is less than proposee position 
            #   if it is, marry him instead and make current husband single, 
            #   else, she says no to the knight. 
            if(ladies[lady].index(knight) < ladies[lady].index(marriedCouples.get(lady))):
                newlySingleKnight = marriedCouples.get(lady)
                marriedCouples[lady] = knight
                singleKnights.append(newlySingleKnight)
            
            else:
                singleKnights.append(knight)

        # If both were unmarried, marry them. 
        else:
            marriedCouples[lady] = knight

    return marriedCouples

# Driver code
def main():
    
    marriedList = ReadFile()
    for couple in marriedList:
        print(marriedList[couple], couple)
    sys.stderr.write(" ========== Benchmark Time: %s sec. ==========" %(time.time() - stopwatch))

if __name__ == "__main__":
    main()



