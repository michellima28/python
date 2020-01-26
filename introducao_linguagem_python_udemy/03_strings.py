Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome='Michel Lima'
>>> print(nome)
Michel Lima
>>> nome[0:5]
'Miche'
>>> nome[1:5]
'iche'
>>> nome[0:6]
'Michel'
>>> nome+nome
'Michel LimaMichel Lima'
>>> nome*3
'Michel LimaMichel LimaMichel Lima'
>>> 'i' in nome
True
>>> 'a' in nome
True
>>> 'z' in nmome
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'z' in nmome
NameError: name 'nmome' is not defined
>>> 'z' in nome
False
>>> 
