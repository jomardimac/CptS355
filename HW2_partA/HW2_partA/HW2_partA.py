#Name: Jomar Dimaculangan
#WSU ID: 11422439
#Homework 2: Postscript Interpreter Part A

#Operand Stack: extantiate an operand stack for operations:

opstack = []

#checkers:

#checks to see if a variable is a dict type.
#will be returning true if type is dict, and false if it isn't
def isDict(x):
    if type(x) is dict:
        return True
    else:
        return False

#checks to see if a variable is an int type.
#will be returning true if type is int, and false if it isn't

def isInt(x):
    if type(x) is int:
        return True
    else:
        return False

#checks to see if a variable is a string type.
#will be returning true if type is string, and false if it isn't
def isStr(x):
    if type(x) is str:
        return True
    else:
        return False

# now define functions to push and pop values on the opstack according to your decision about which
# end should be the hot end. Recall that `pass` in python is a no-op: replace it with your code.

#opPop() pops off the top of the the operand stack and returns the number it popped off
def opPop():
    if(opstack is []):
        print("operator stack is empty")
    else:
        return opstack.pop()

#opPush adds a value on the top of opstack
def opPush(value):
    opstack.append(value)
    

#Dictionary stack: Define dictionary stack and its operations:

dictstack = [{}]

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

#dictPop takes off the top dictionary of and returns the popped dictionary
def dictPop():
    if(dictstack is [{}]):
        print("dictionary stack is empty")
    else:
        return dictstack.pop()

#dictPush adds a value in a dictionary on top of the dictstack
def dictPush(val):
    dictstack.append({val})

#define defines a name and puts a value in top of the dictstack
def define(name, value):
    dictstack[-1][name] = value

#look up iterates through the whole dictionary stack and
#returns the value of the given key:
def lookup(name):
    for i in dictstack: #go through each dict in the stack
        for x in i.keys(): #go through the keys to see if it matches
            if(x == name): #if it does match, return name
                return i.get(name)

    print("can't find")

# Arithmetic operators: define all the arithmetic operators here -- add, sub, mul, div, mod

#opAdd pops off the top two integers and adds them together and puts the sum on top of stack
def opAdd():
    val1 = opPop()#pop the top two integers
    val2 = opPop()
    if(isInt(val1) and isInt(val2)): #check and make sure that they are integers. if they are, add them
        trueval = val1 + val2
        opPush(trueval) #put them on top of the stack
    else: #exception handler
        print("invalid inputs, not integer") 
        opPush(val2)#put everything back
        opPush(val1)

#opSub pops off the top two integers and subtracts the second popped to the first popped item
def opSub():
    int1 = opPop(); #pop the top two int
    int2 = opPop();
    if(isInt(int1) and isInt(int2)): #checker similar to add
        val = int2-int1
        opPush(val)
    else:
        print("invalid inputs, not integer") #put them back together otherwise
        opPush(int2)
        opPush(int1)
    
#opMult pops off the top two integers and multiplies them together
def opMul():
    int1 = opPop() #pop top two int
    int2 = opPop()
    if(isInt(int1) and isInt(int2)): #checker similar to add
        val = int1 * int2
        opPush(val)
    else:
        print("invalid inputs, not integer") #put them back together otherwise
        opPush(int2)
        opPush(int1)

#opDiv pops off the top two integers and divides the second popped to the first.
def opDiv():
    int1 = opPop();
    int2 = opPop();
    if(int1 == 0 ): #check to see if their integers and/or dividing by 0
        print("dividing by 0") #put everythign back
        opPush(int2)
        opPush(int1)
    elif(isInt(int1) and isInt(int2)): #Checks if inputs are valid
        val = int2 / int1
        opPush(val)
    else:
        print("invalid inputs, not integer") #put them back together otherwise
        opPush(int2)
        opPush(int1)

def opMod():
    int1 = opPop();
    int2 = opPop();
    if(int1 is 0):
        print("can't mod by 0, error") #checks if modding by 0, if not, throw an exception
        opPush(int2)
        opPush(int1)
    else: #modulus the first popped item to the latest popped item
        val = int2 % int1
        opPush(val)

#String Operators: define all the string operators -- length, get, put, getinerval

#length : gets a string (from the stack) and pushes the length of the string on the stack
def length():
    strin = len(opPop()) #get the length of the string and push it
    opPush(strin)

#get : gets a string and an index (integer) value (from the stack) and pushes the ASCII value of the character at position index onto the stack
def get():
    strin = opPop() #takes out the string 
    index = opPop() #takes out  the index
    opPush(ord(strin[index])) #push the asciivalue of the char

#put : gets a string, an index (integer) value, and an ASCII(integer) value (from the stack), replaces the character at position index in the string 
#with the given ASCII character. The resulting string, however,is not stored in the operand stack. Hence, for explicit use of put operator,
# we can define a string variable and apply the put operation on the value of this variable.

def put():
    strin = opPop() #grab the string from the stack
    index = opPop() #grab the index from the stack afterwards
    asc = opPop() #this will be the ascii value that will replace the char
    newstring = strin[:index] + chr(asc) + strin[index+1:] #replace the string
    opPush(newstring) #push on top of stack

#getinterval : gets a string, an index (integer) value, and a count (integer) value (from the stack), and 
#returns the substring of string starting at index for count. Pushes the substring on the stack.
#example: (CptS355) 0 3 getinterval output: Cpt

def getinterval():
    strin = opPop() #gets the string on top of the stack
    count = opPop() #get an starting index
    val = opPop() #get how many char you want in
    newstr = strin[count:val] #grab the new interval
    opPush(newstr) #push the substring on stack

# Define the stack manipulation  and print operators: dup, exch, pop, roll, copy, clear, stack

# dup: adds a duplicate copy of the top object of the stack to the stack.
def dup():
    val = opPop() #pop the value 
    opPush(val) #push the value twice so there will be a duplicate
    opPush(val)

#exch: exchanges the position of the top two elements on the stack.
def exch():
    val1 = opPop() #grabe the top two stacks
    val2 = opPop()
    opPush(val1) #switch them and will be the exchange
    opPush(val2)

#pop: pop the top value from the stack
def pop():
    opPop() #pops the value

#roll: 
def roll():
    shift = opPop() #get how many times the num in operand stack will shift
    indexes = opPop() #get which numbers wil lbe shifted
    newstack = opstack[-indexes:] #create a new stack with just how many indexes there are
    fillin = [0]*indexes #create a new stack to fill in the rolled values
    for i in range(0,indexes):
        fillin[i] = newstack[(i-shift) % indexes] #THIS WILL ROLL THE VALUES 

    opstack[-indexes:] = fillin
#copy:adds a copy of the top n objects on the stack.

def copy():
    count = opPop() #will be the 'n' in how many copies n objects on the stack
    index = -count #will be used as an index in the stack
    i = 0
    while i < count: #go through the stack based on the 'n' in copy
        opstack.append(opstack[index]) #add on to the top of the stack 
        i = i + 1

#clear: empties the operator stack
def clear():
    opstack.clear() #built in clear function

#stack: prints out the things in stack 
def stack():
    for i in opstack:
        print(i)

# Define the dictionary manipulation operators: dict, begin, end, def
# name the function for the def operator psDef because def is reserved in Python

def Dict():
    opPush({}) #pushes a new dict


def begin():
    first = opPop() #pops off the top of operand
    if (isDict (first)): #checks if it is a dict
        dictstack.append(first) #adds the popped off operand to the dictionary stack
    else:
        print("can't add, not a dict")

def end():
    return dictPop() #ends the dict by popping off 

#psDef: creates a dictionary when popping off the top two values in operand stack
def psDef():
    val1 = opPop()
    val2 = opPop()
    define(val2,val1)


#test cases:

#always going to clear the stack for these tests to avoid lingering values:

def testOpPop():
    global opstack
    opstack.clear() 
    opstack = [1,2] #gonna test to pop 2
    test1 = opPop()
    if(test1 == 2):
        return True
    else:
        return False

def testOpPush():
    global opstack
    opstack.clear()
    opPush(1) #push 1 in the stack 
    if(opstack == [1]): #check to see if the pushed val is there
        return True
    else:
        return False

def testDictPop():
    global opstack
    global dictstack
    dictstack = [{'a',2},{'b',3}] #set a stack to pop
    test1 = dictPop() #pops the last one
    if(test1 == {'b',3}):
        return True
    else:
        return False

def testDictPush():
    global opstack
    global dictstack
    dictstack.clear()
    dictPush('a') #pushes the letter 'a'
    if(dictstack == [{'a'}]): #dictstack should contain the char pushed
        return True
    else:
        return False

def testDefine():
    global opstack
    global dictstack
    dictstack = [{'a':1}] #going to put a premade stack
    define('b',4) #define the letter b in the dict stack
    if(dictstack == [{'a': 1, 'b': 4}]):
        return True
    else:
        return False

def testLookup():
    global opstack
    global dictstack
    dictstack = [{'a':1},{'b':2},{'c':3,'d':4}] #a preset list to find the name
    test1 = lookup('d') #clal the function and try to find a name
    if(test1 == 4):
        return True
    else:
        return False

def testOpAdd():
    global opstack

    opstack.clear()
    opPush(1) #push 1
    opPush(2) #push 2
    opAdd() #should add up to 3
    if(opPop() != 3): return False
    return True

def testOpSub():
    global opstack
    opstack.clear()
    opPush(2) #push 2
    opPush(1) #push 1
    if(opPop() != 1): return False #should add up to 1
    return True

def testOpMult():
    global opstack
    opstack.clear()
    opPush(3) #push 3 twice and see if it adds up to 9
    opPush(3)
    opMul()
    if(opPop() != 9): return False
    return True

def testOpDiv():
    global opstack
    opstack.clear()
    opPush(8) #push 8 and divide by 4
    opPush(4)
    opDiv()
    if(opPop() != 2.0): return False
    return True

def testOpMod():
    global opstack
    opstack.clear()
    opPush(3) #going to be used as an even number. if even, return popped wil lbe 0, 1 otherwise
    opPush(2)
    opMod()
    if(opPop() != 1): return False
    return True

def testLen():
    global opstack
    opstack.clear()
    opPush('aaa') #should have 3 as length
    length()
    if(opPop() != 3): return False
    return True

def testGet():
    global opstack
    opstack.clear()
    opPush(0) #push which index it should be on
    opPush('CptS355') #push the string you want to see the ascii val
    get() #call the get function to pop off the last item
    if(opPop() != 67): return False #ascii val of C is 67
    return True

def testPut():
    global opstack
    opstack.clear()
    opPush(99) #push the ascii value of wanted char
    opPush(0) #push the index of the string
    opPush('CptS355') #push the string
    put() #call function, it should change 'C' to 'c'
    if(opPop() != 'cptS355'): return False
    return True

def testInterval():
    global opstack
    opstack.clear()
    opPush(3) #push how many char from the index you wnat
    opPush(0) #push the index you want
    opPush('CptS355') #push the string you want
    getinterval()
    if(opPop() != 'Cpt'): return False
    return True

def testDup():
    global opstack
    opstack = [3,2,1] #set a preset stack
    dup() #should have the top stack twice.
    if(opstack != [3, 2, 1, 1]): return False
    return True

def testExch():
    global opstack
    opstack = [3,2,1] #set a preset stack 
    exch() #should swap the most top two items
    if(opstack != [3, 1, 2]): return False
    return True

def testPop():
    global opstack
    opstack = [4,3] #set a preset stack
    pop()
    if(opstack != [4]): return False
    return True

def testRoll():
    global opstack
    opstack.clear()
    opPush(4) #set up the stack as [4,3,2,1]
    opPush(3)
    opPush(2)
    opPush(1)
    opPush(3) #this will be the index, how many items will switch
    opPush(1) #this will be the shift, how many times the itmes will shift
    roll() #call roll function
    if(opstack != [4, 1, 3, 2]): return False #opstack should roll correctly
    return True

def testCopy():
    global opstack
    opstack = [4,3,2,1] #set a preset stack to copy
    opPush(3) #this will be the count on which object will be copied
    copy() #call copy function ,should equal [4, 3, 2, 1, 3, 2, 1]
    if(opstack != [4, 3, 2, 1, 3, 2, 1]): return False
    return True

def testClear():
    global opstack
    opstack = [1] #set a preset stack
    clear() #clear the whole opstack
    if(opstack != []): return False #should be cleared
    return True

def testDict():
    global opstack
    global dictstack
    clear() 
    Dict() #calling dict should create a dictionary
    if(opstack != [{}]) : return False
    return True

def testBegin():
    global opstack
    global dictstack
    clear()
    dictstack.clear()
    opPush({'a':3})
    begin()
    if(dictstack != [{'a':3}]): return False
    return True

def testEnd():
    global opstack
    global dictstack
    dictstack = [{}, {3}] #preset stack
    if (dictPop() != {3}): return False
    return True

def testpsDef():
    global opstack
    global dictstack
    clear()
    opPush(1)
    opPush(2)
    psDef()
    if(dictstack !=[{1:2}]): return False
    return True


if __name__ == '__main__':

    opstack = []
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    print("Name: Jomar Dimaculangan. \nHomework 2 Part A\n")
    
    if testOpPop():
        print(passedMsg % 'testOpPop')
    else:
        print(failedMsg % 'testOpPop')

    if testOpPush():
        print(passedMsg % 'testOpPush')
    else:
        print(failedMsg % 'testOpPush')

    if testDictPop():
        print(passedMsg % 'testDictPop')
    else:
        print(failedMsg % 'testDictPop')

    if testDictPush():
        print(passedMsg % 'testDictPush')
    else:
        print(failedMsg % 'testDictPush')
    
    if testDefine():
        print(passedMsg % 'testDefine')
    else:
        print(failedMsg % 'testDefine')

    if testLookup():
        print(passedMsg % 'testLookup')
    else:
        print(failedMsg % 'testLookup')

    if testOpAdd():
        print(passedMsg % 'testOpAdd')
    else:
        print(failedMsg % 'testOpAdd')

    if testOpSub():
        print(passedMsg % 'testOpSub')
    else:
        print(failedMsg % 'testOpSub')

    if testOpMult():
        print(passedMsg % 'testOpMult')
    else:
        print(failedMsg % 'testOpMult')

    if testOpDiv():
        print(passedMsg % 'testOpDiv')
    else:
        print(failedMsg % 'testOpDiv')
    if testOpMod():
        print(passedMsg % 'testOpMod')
    else:
        print(failedMsg % 'testOpMod')

    if testLen():
        print(passedMsg % 'testLen')
    else:
        print(failedMsg % 'testLen')
    if testGet():
        print(passedMsg % 'testGet')
    else:
        print(failedMsg % 'testGet')
    if testPut():
        print(passedMsg % 'testPut')
    else:
        print(failedMsg % 'testPut')
    if testInterval():
        print(passedMsg % 'testInterval')
    else:
        print(failedMsg % 'testInterval')
    if testDup():
        print(passedMsg % 'testDup')
    else:
        print(failedMsg % 'testDup')
    if testExch():
        print(passedMsg % 'testExch')
    else:
        print(failedMsg % 'testExch')
    if testPop():
        print(passedMsg % 'testPop')
    else:
        print(failedMsg % 'testPop')
    if testRoll():
        print(passedMsg % 'testRoll')
    else:
        print(failedMsg % 'testRoll')
    if testCopy():
        print(passedMsg % 'testCopy')
    else:
        print(failedMsg % 'testCopy')
    if testClear():
        print(passedMsg % 'testClear')
    else:
        print(failedMsg % 'testClear')
    if testDict():
        print(passedMsg % 'testDict')
    else:
        print(failedMsg % 'testDict')
    if testBegin():
        print(passedMsg % 'testBegin')
    else:
        print(failedMsg % 'testBegin')

    if testEnd():
        print(passedMsg % 'testEnd')
    else:
        print(failedMsg % 'testEnd')
    if testpsDef():
        print(passedMsg % 'testpsDef')
    else:
        print(failedMsg % 'testpsDef')
