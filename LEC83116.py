Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L = [('e',1),('d',3),('f',2),('a',2)]
>>> sorted(L,key = lambda item : item[1])
[('e', 1), ('f', 2), ('a', 2), ('d', 3)]
>>> sorted(L,key = lambda item : item[2])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sorted(L,key = lambda item : item[2])
  File "<pyshell#2>", line 1, in <lambda>
    sorted(L,key = lambda item : item[2])
IndexError: tuple index out of range
>>> L1= sorted(L, key = lambda item : item[0])
>>> L1
[('a', 2), ('d', 3), ('e', 1), ('f', 2)]
>>> L1 = sorted(L1, key = lambda item : item[0])
>>> L1 = sorted(L1, key = lambda item : item[1])
>>> L1
[('e', 1), ('a', 2), ('f', 2), ('d', 3)]
>>> #this is how you sort from the second
>>> L
[('e', 1), ('d', 3), ('f', 2), ('a', 2)]
>>> L.sort(key = lambda item : item[0], reverse = True)
>>> L
[('f', 2), ('e', 1), ('d', 3), ('a', 2)]
>>> L.sort(key = lambda item : item[0], reverse = False)
>>> L
[('a', 2), ('d', 3), ('e', 1), ('f', 2)]
>>> 

>>> L.sort(key = lambda item : item[0], reverse = True)
>>> for x in L:
	print(L[0], " ", L[1], end = ',')

	
('f', 2)   ('e', 1),('f', 2)   ('e', 1),('f', 2)   ('e', 1),('f', 2)   ('e', 1),
>>> for x in L:
	print(x[0], end = ',')
	print(x[1], end = ';')

	
f,2;e,1;d,3;a,2;
>>> c = "355"
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	print("n/a")

	
CptS  355
>>> c = 354
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	print("n/a")

	
n/a
>>> c = "354"
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	print("n/a")

	
EE  354
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	print("n/a")
	pass

EE  354
>>> if c=="33":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	pass

EE  354
>>> c = "33"
>>> if c=="33":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	pass

CptS  33
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	pass

>>> c = "421"
>>> if c=="355":
	print("CptS ",c)
elif c == "354":
	print("EE ",c)
else:
	pass

>>> d = {'a':1,2: 'x','b':3}
>>> d
{2: 'x', 'b': 3, 'a': 1}
>>> d['a']
1
>>> d[2]
'x'
>>> print('\n')


>>> d
{2: 'x', 'b': 3, 'a': 1}
>>> list(d)
[2, 'b', 'a']
>>> d.items()
dict_items([(2, 'x'), ('b', 3), ('a', 1)])
>>> d.keys()
dict_keys([2, 'b', 'a'])
>>> d = {'a':1,2:'x','b':3}
>>> d
{2: 'x', 'b': 3, 'a': 1}
>>> list(d.keys())
[2, 'b', 'a']
>>> list(d.values())
['x', 3, 1]
>>> v = 5
>>> if v in d.keys():
	print(d[v])

	
>>> v = 'a'
>>> if v in d.keys():
	print(d[v])

	
1
>>> d.get(5,-1)
-1
>>> d.get('a',-1)
1
>>> #returns the value of the key
>>> sort(d)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    sort(d)
NameError: name 'sort' is not defined
>>> sorted(d)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    sorted(d)
TypeError: unorderable types: str() < int()
>>> #since its nota list , it won't run
>>> sorted(list(d.items()))
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    sorted(list(d.items()))
TypeError: unorderable types: str() < int()
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> d
{2: 'x', 'b': 3, 'a': 1}
>>> d1 = {'a':1, 'b':3, 'c' : 5}
>>> d1
{'c': 5, 'b': 3, 'a': 1}
>>> sorted(list(d1.items()))
[('a', 1), ('b', 3), ('c', 5)]
>>> sorted(d1)
['a', 'b', 'c']
>>> d
{2: 'x', 'b': 3, 'a': 1}
>>> d1 = {'a':1, 'b':3, 'c': 3}
>>> d1 = {'a':1 , 'b':3, 'b': 4}
>>> d1
{'b': 4, 'a': 1}
>>> 
>>> 
>>> S = {'a','b','c'}
>>> S
{'a', 'b', 'c'}
>>> 
