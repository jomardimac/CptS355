#Name: Jomar Dimaculangan
#WSU ID: 11422439
#Date: August 28, 2016
#Ran on Windows 10

#creates a dictionary for each character in s1 that is mapped in s2
#Used the documentation in python for help: https://docs.python.org/3.3/library/functions.html#zip
def makettable(s1,s2):
    #dict() is used as a constructor to build key value pairs.
    #zip is the iterator for tuples
    return dict(zip(s1,s2))

#translates the dictionary used in makettable and changes each character in s to its old character
def trans(ttable,s):
    #iterate each letters in s
    for i in s:
        #get the keys of the ttable made by makettable
        j = ttable.keys()
        #use the get function to replace all of the 
        get = ttable.get(i)
        #go through the keys to see if the character matches one of the charcter in the keys
        for x in j:
            if x == i:
                #replace all of the ones in there
                s = s.replace(i,get)
        
        
    return s

#test1 made by sakire 
def testtrans():
    ttable = makettable('abc','xyz')
    revttable = makettable('xyz','abc')
    tests = "Now I know my abc's"
    answers = "Now I know my xyz's"
    test1 = tests
    print(test1)
    test1 = trans(ttable, tests)
    print(test1)
    test2 = "Lets change 'abdf'"
    ttable2 = makettable('abdf','yuzx')
    print(test2)
    test2 = trans(ttable2,test2)
    print(test2)
  
    if trans(ttable,tests) != answers:
        print("False")
        return False
    if trans(ttable,"Now I know my abc's") == answers:
        print("True")
        return True
    if trans(revttable, trans(ttable,tests)) != "Now I know mb abc's":
        print("False") 
        return False
    if trans(ttable,'') != '':
        print("False")
        return False;
    if trans(makettable('',''), "abc") != 'abc':
        print("False")
        return False

    return


#use a helper function to find a key:
def myKeyHisto(thelist):
    x,y = thelist
    return -y,x

#hist() returns a list of characters in the input s string while paired with frequency. will be sorted from most frequent to least.
#if the same frequency, it will be sorted in alphabetical order.
#histo(test) = [('t',2),('e',1),('s',1)]
def histo(s):
    alphabet = list()
    #create a dictionary
    freqChar = dict()
    #go through the string and see if a character is in the dictionary, if it is, update it and add the frequency.
    for i in s:
        if i in freqChar:
            freqChar[i] = freqChar.get(i)+1
            
        #if not, add it in as a tuple:
        else:
            freqChar[i] = 1
   
    #now time to sort by using the sort function built in the python:
    #grab the items from the dictionary:
    items = freqChar.items()
    #according to the documentation: sorted(iterable, key = none, reverse = False)
    #sorted(list of tuples, key = sort by frequency, reverse = True)

    alphabet = sorted(items,key = myKeyHisto) #alphabetalize
    
    return alphabet

def test2():
    test = "implemented"
    b = histo(test)
    print(b)

    return

def myKeyGraph(thekey):
    x,y = thekey
    return x,y

def digraphs(ss):
    #create two iterators for indexing the string:
    i = 0
    j = 1
    #create a string:
    string = str()
    #define a list to put in the digraphs:
    striing = list()
    #define a dictionary to put the list and frequency in:
    di = dict()
    #go through the string:
    for x in ss[:-1] :
        #put the string inside the dictionary:
        string = '/' + ss[i] + ss[j] + '/'
        #if the string is in the dictionary, update it by adding 1, this will be the frequency
        if string in di:
            di[string] = di.get(string) + 1
        #if the string is not in the dictionary, add it in.
        else:
            di[string] = 1

        i = i + 1
        j = j + 1

    sorting = sorted(di.items(),key = myKeyGraph)

    return sorting

def test3():
    test = 'This is a test for the digraphs function. This should sort them alphabetical. One Question Mark ?'
    print(test)
    print(digraphs(test))
    test2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    print(test2)
    print(digraphs(test2))

    return


if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if testtrans():
        print(passedMsg % 'testtrans')
    else:
        print(failedMsg % 'testtrans')
