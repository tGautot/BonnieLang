#!/usr/bin/python3

grid = []
pos = [0,0]
stack = []
hand = 0
parameter = 0



def doAdd():
    global stack
    if len(stack) < 2:
        raise("Even though bonnie is really cute, she still needs at least 2 numbers to do an addition")
    a,b  = stack.pop(), stack.pop()
    stack.append(a+b)

def doSub():
    global stack
    if len(stack) < 2:
        raise("Even though bonnie is really cute, she still needs at least 2 numbers to do a substraction")
    a,b  = stack.pop(), stack.pop()
    stack.append(a-b)

def doMult():
    global stack
    if len(stack) < 2:
        raise("Even though bonnie is really cute, she still needs at least 2 numbers to do a multiplication")
    a,b  = stack.pop(), stack.pop()
    stack.append(a*b)

def doDiv():
    global stack
    if len(stack) < 2:
        raise("Even though bonnie is really cute, she still needs at least 2 numbers to do a division")
    a,b  = stack.pop(), stack.pop()
    stack.append(a//b)

def doMod():
    global stack
    if len(stack) < 2:
        raise("Even though bonnie is really cute, she still needs at least 2 numbers to do a modulus")
    a,b  = stack.pop(), stack.pop()
    stack.append(a%b)

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


tileToAction = {
    # Deprecated;"GenNumber": lambda : setInHand(parameter),
    "AddToStack": lambda : stack.append(hand),
    "PopFromStack": lambda : setInHand(stack.pop()), # TODO put in own function to check stack size b4 pop
    "PrintStr": lambda : print(strFromStack()),
    "PrintInt": lambda : print(stack.pop()), # TODO put in own function to check stack size b4 pop
    "Add": doAdd,
    "Sub": doSub,
    "Mul": doMult,
    "Div": doDiv,
    "Mod": doMod

}


def executeTile():
    tile = grid[pos[0]][pos[1]]
    tileToAction[tile]()


    
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
            setInHand(int(numStr))
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




