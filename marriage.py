# John Sullivan & Shane Wallerick
# marriage.py
# CSC440
# 1/30/2020

import sys

def tests():
    args = sys.argv
    dataFile = open(args[1], "r")
    prefs = []
    knights = []
    ladies = []
    line = dataFile.readline()
    n = int(line)
    totalPeople = n * 2
    line = dataFile.readline()
    while line:
        prefs.append(line.split())
        line = dataFile.readline()
    i = 0
    while i < totalPeople/2:
        knights.append(prefs[i])
        knights[i].append(0)
        i+=1

    j = 0
    i = int(totalPeople/2)
    while i < totalPeople:
        ladies.append(prefs[i])
        ladies[j].append(0)
        i+=1
        j+=1
    
    print("knights")
    print(knights)
    print("ladies")
    print(ladies)



def Marriage():
    args = sys.argv
    dataFile = open(args[1], "r")
    prefs = []
    knights = []
    ladies = []
    line = dataFile.readline()
    n = int(line)
    totalPeople = n * 2
    line = dataFile.readline()
    while line:
        prefs.append(line.split())
        line = dataFile.readline()
    i = 0
    while i < totalPeople/2:
        knights.append(prefs[i])
        knights[i].append(0)
        i+=1

    j = 0
    i = int(totalPeople/2)
    while i < totalPeople:
        ladies.append(prefs[i])
        ladies[j].append(0)
        i+=1
        j+=1
    
    print("knights")
    print(knights)
    print("ladies")
    print(ladies)

#IMPORTANT
#index n+1 will be the flag

def main():
    Marriage()

main()


#hey whazsxdcfgtyhujiokplkjhgfvcxcfvghjikolpl,m sawesrt6y78u90-=]\[p0o98]