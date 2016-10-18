#Name: Jomar Dimaculangan
#WSU ID: 11422439
#Homework 2: Postscript Interpreter Part A

#Operand Stack: extantiate an operand stack for operations:
opstack = []

# now define functions to push and pop values on the opstack according to your decision about which
# end should be the hot end. Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    return opstack.pop()

def popPush(value):
    opstack.append(value)
    

#Dictionary stack: Define dictionary stack and its operations:

dictstack = [{}]

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    
    pass
def dictPush():
    
    pass
def define(name, value):
    
    pass
def lookup(name):
    pass
    # return the value associated with name
    # what is your design decision about what to do when there is no definition for name

# Arithmetic operators: define all the arithmetic operators here -- add, sub, mul, div, mod
def opAdd():
    return (opPop() + opPop())

def opSub():
    int1 = opPop();
    int2 = opPop();
    return (int2-int1)

def opMul():
    return (opPop() * opPop())

def opDiv():
    int1 = opPop();
    int2 = opPop();
    if(int2 == 0):
        print("dividing by 0, error")
    else:
        return (int2 // int1)

def opMod():
    int1 = opPop();
    int2 = opPop;
    if(int2 is 0):
        print("can't mod by 0, error")
    else:
        return (int2 % int1)





