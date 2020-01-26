Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tupla=("tiago", "python", "udemy")
>>> tuplas
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tuplas
NameError: name 'tuplas' is not defined
>>> tupla
('tiago', 'python', 'udemy')
>>> tupla(0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tupla(0)
TypeError: 'tuple' object is not callable
>>> tupla(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tupla(1)
TypeError: 'tuple' object is not callable
>>> tupla(0:2)
SyntaxError: invalid syntax
>>> tupla[0]
'tiago'
>>> tupla[0:2]
('tiago', 'python')
>>> len(tupla)
3
>>> tupla+tupla
('tiago', 'python', 'udemy', 'tiago', 'python', 'udemy')
>>> tupla*5
('tiago', 'python', 'udemy', 'tiago', 'python', 'udemy', 'tiago', 'python', 'udemy', 'tiago', 'python', 'udemy', 'tiago', 'python', 'udemy')
>>> 4 in tupla
False
>>> tiago in tupla
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tiago in tupla
NameError: name 'tiago' is not defined
>>> "udemy" in tupla
True
>>> lista=[1,4, "tiago"]
>>> lista
[1, 4, 'tiago']
>>> tupla2=tuple(lista)
>>> tupla2
(1, 4, 'tiago')
>>> 
