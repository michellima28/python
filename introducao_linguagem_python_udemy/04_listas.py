Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista=[1,4,7,'Michel',23,14]
>>> print(lista)
[1, 4, 7, 'Michel', 23, 14]
>>> lista.append('python')
>>> print(lista)
[1, 4, 7, 'Michel', 23, 14, 'python']
>>> lista.append[20]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lista.append[20]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> lista.append(20)
>>> print(lista)
[1, 4, 7, 'Michel', 23, 14, 'python', 20]
>>> lista.index('Michel')
3
>>> lista.index('python')
6
>>> lista.count(4)
1
>>> lista.append(4)
>>> print(lista)
[1, 4, 7, 'Michel', 23, 14, 'python', 20, 4]
>>> lista.count(4)
2
>>> lista.remove('python')
>>> print(lista)
[1, 4, 7, 'Michel', 23, 14, 20, 4]
>>> lista.remove(4)
>>> print(lista)
[1, 7, 'Michel', 23, 14, 20, 4]
>>> lista.reverse()
>>> print(lista)
[4, 20, 14, 23, 'Michel', 7, 1]
>>> lista2=(1,9,4,2,7,6)
>>> print(lista2)
(1, 9, 4, 2, 7, 6)
>>> lista2.sort()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista.sort()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lista.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> listanumerica=[1,7,4,1,15,75,34,100,45,36]
>>> print(listanumerica)
[1, 7, 4, 1, 15, 75, 34, 100, 45, 36]
>>> listanumerica.sort()
>>> print(listanumerica)
[1, 1, 4, 7, 15, 34, 36, 45, 75, 100]
>>> 
