Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open("C:\Users\user\Downloads\dataSample\0A32eTdBKayjCWhZqDOQ.bytes","r")

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open("C:\Users\user\Downloads\dataSample\0A32eTdBKayjCWhZqDOQ.bytes","r")
TypeError: file() argument 1 must be encoded string without NULL bytes, not str
>>> f = open("C:\\Users\\user\\Downloads\\dataSample\\0A32eTdBKayjCWhZqDOQ.bytes","r")
>>> lines = f.readlines()
>>> len(lines)
75105
>>> line10=lines[:10]
>>> len(line10)
10
>>> print line10[0]
00401000 56 8D 44 24 08 50 8B F1 E8 1C 1B 00 00 C7 06 08

>>> line10[0].split(" ")
['00401000', '56', '8D', '44', '24', '08', '50', '8B', 'F1', 'E8', '1C', '1B', '00', '00', 'C7', '06', '08\n']
>>> line10[0].replace("\n","").split(" ")
['00401000', '56', '8D', '44', '24', '08', '50', '8B', 'F1', 'E8', '1C', '1B', '00', '00', 'C7', '06', '08']
>>> line10[0].replace("\n","").split(" ")[1:]
['56', '8D', '44', '24', '08', '50', '8B', 'F1', 'E8', '1C', '1B', '00', '00', 'C7', '06', '08']
>>> r1 = line10[0].replace("\n","").split(" ")[1:]
>>> len(r1)
16
>>> for x in r1:
	print int(x)

	
56

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print int(x)
ValueError: invalid literal for int() with base 10: '8D'
>>> for x in r1:
	print int(x,16)

	
86
141
68
36
8
80
139
241
232
28
27
0
0
199
6
8
>>> 
