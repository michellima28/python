Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numero=20
>>> numero
20
>>> while True:
	numero=numero-1
	print(nuemro)
	if (numero==2):
		break

	
Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    print(nuemro)
NameError: name 'nuemro' is not defined
>>> while True:
	numero=numero-1
	print(numero)
	if (numero==2):
		break

18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
>>> numero=10
>>> numero
10
>>> while True:
	numero=numero-1
	if(numero==4):
		continue
	print(numero)
	if(numero==2):
		break

	
9
8
7
6
5
3
2
>>>  for x in range(0,5) :
	 
SyntaxError: unexpected indent
>>> for x in range(0,5):
	pass

>>> 
