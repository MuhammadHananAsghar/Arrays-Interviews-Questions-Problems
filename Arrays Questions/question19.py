# Two Stacks in One Array
import random

stackList = [None for _ in range(6)]
StackOnetop = 0
StackTwotop = len(stackList)//2

def push1(value: int):
    global StackOnetop
    if StackOnetop >= len(stackList)//2:
        print("Stack One Overflow.")
    elif StackOnetop < 0:
        print("Stack One Underflow")
    else:
        stackList[StackOnetop] = value
        StackOnetop = StackOnetop + 1

def push2(value: int):
    global StackTwotop
    if StackTwotop >= len(stackList):
        print("Stack Two Overflow.")
    elif StackTwotop < len(stackList)//2:
        print("Stack Two Underflow")
    else:
        stackList[StackTwotop] = value
        StackTwotop = StackTwotop + 1

def pop1():
    global StackOnetop
    if StackOnetop < 0:
        print("Stack One Underflow")
    else:
        StackOnetop = StackOnetop - 1

def pop2():
    global StackTwotop
    if StackTwotop < len(stackList)//2:
        print("Stack Two Underflow")
    else:
        StackTwotop = StackTwotop - 1

def printStacks():
    global StackTwotop, StackOnetop
    print("StackOne: ", end="")
    for i in reversed(range(StackOnetop)):
        print(stackList[i], end=" ")
    print()

    print("StackTwo: ", end="")
    for i in reversed(range(len(stackList)//2, StackTwotop)):   
        print(stackList[i], end=" ")
    print()

for _ in range(3):
    push1(random.randint(10, 50))
    push2(random.randint(50, 100))

printStacks()
pop1()
pop2()
printStacks()