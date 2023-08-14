#!/usr/bin/python3

grid = []
pos = [0,0]
stack = []
hand = 0
parameter = 0


def executeTile():
    tile = grid[pos[0]][pos[1]]
    if tile == "GenNumber":
        setInHand(parameter)
    elif tile == "AddToStack":
        global stack
        stack.append(hand)
    elif tile == "PrintStr":
        print(strFromStack())

def strFromStack():
    out = ""
    while len(stack) > 0 and stack[-1] != 0:
        out += chr(stack.pop()) 
    if len(stack) > 0:
        stack.pop()
    return out

def setInHand(val):
    global hand
    hand = val

def setParameter(val):
    global parameter
    parameter = val
    
def doScript(script):
    global pos, parameter
    c = 0
    while c < len(script):
        if script[c] == "w":
            parameter = 0
            pos[0]-=1
        if script[c] == "a":
            parameter = 0
            pos[1]-=1
        if script[c] == "s":
            parameter = 0
            pos[0]+=1
        if script[c] == "d":
            parameter = 0
            pos[1]+=1
        # TODO check if pos is still valid

        if script[c] == "#":
            executeTile()
        
        if script[c].isdigit():
            numStr = ""
            while script[c].isdigit():
                numStr += script[c]
                c+=1
            setParameter(int(numStr))
            c-=1
        c+=1



print("READING GRID -------------------------------------")

gridFile = open("grid.txt", "r")
while True:
    l = gridFile.readline()
    if l == "\n":
        break
    grid.append(l.split(","))

l = gridFile.readline()
startPosStr = l.split(",")
pos = [int(startPosStr[0]), int(startPosStr[1])]


print("INTERPRETING SCRIPT ------------------------------")

import sys
scriptFile = open(sys.argv[1], "r")
script = ''.join(scriptFile.readlines())
doScript(script)




