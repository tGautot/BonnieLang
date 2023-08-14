#!/usr/bin/python3

UP = "w"
DOWN = "s"
LEFT = "a"
RIGHT = "d"
ACTIVATE = "#"

grid = []
pos = [0,0]
stack = []
hand = 0
pc = 0 # Program Counter (points to the char)


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

def jumpTo():
    global pc
    pc = hand

def jumpFrw():
    global pc
    pc += hand


def ifZeroJumpTo():
    if len(stack) == 0:
        raise("Cannot use If when stack is empty")
    if stack[-1] == 0:
        global pc
        pc = hand

def ifZeroJumpFrw():
    if len(stack) == 0:
        raise("Cannot use If when stack is empty")
    if stack[-1] == 0:
        global pc
        pc += hand

def ifZogJumpTo():
    if len(stack) == 0:
        raise("Cannot use If when stack is empty")
    if stack[-1] >= 0:
        global pc
        pc = hand

def ifZogJumpFrw():
    if len(stack) == 0:
        raise("Cannot use If when stack is empty")
    if stack[-1] >= 0:
        global pc
        pc += hand


tileToAction = {
    # Deprecated;"GenNumber": lambda : setInHand(parameter),
    "AddToStack": lambda : stack.append(hand),
    "PopStack": lambda : setInHand(stack.pop()), # TODO put in own function to check stack size b4 pop
    "PrintStr": lambda : print(strFromStack()),
    "PrintInt": lambda : print(stack.pop()), # TODO put in own function to check stack size b4 pop
    "Add": doAdd,
    "Sub": doSub,
    "Mul": doMult,
    "Div": doDiv,
    "Mod": doMod,
    "JumpTo":jumpTo,
    "JumpFrw":jumpFrw,
    "IfZeroJumpTo": ifZeroJumpTo,
    "IfZeroJumpFrw": ifZeroJumpFrw,
    "IfZogJumpTo": ifZogJumpTo,
    "IfZogJumpFrw": ifZogJumpFrw,
    
}



def executeTile():
    tile = grid[pos[0]][pos[1]]
    tileToAction[tile]()

def doScript(script):
    global pos, pc
    pc = 0
    while pc < len(script):
        if script[pc] == UP:
            pos[0]-=1
        elif script[pc] == LEFT:
            pos[1]-=1
        elif script[pc] == DOWN:
            pos[0]+=1
        elif script[pc] == RIGHT:
            pos[1]+=1
        # TODO check if pos is still valid

        elif script[pc] == ACTIVATE:
            executeTile()

        elif script[pc].isdigit() or script[pc] == "-":
            numStr = ""
            if script[pc] == "-":
                numStr = "-"
                pc+=1 
            while script[pc].isdigit():
                numStr += script[pc]
                pc+=1
            numVal = 0
            try:
                numVal = int(numStr)
            except:
                raise("Trying to create value but id invalid: " + numStr)
            setInHand(numVal)
            pc-=1
        pc+=1



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




