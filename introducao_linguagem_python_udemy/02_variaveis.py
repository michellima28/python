Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> valorhora=4
>>> diastrabalho=30
>>> horasdetrabalho=8
>>> vencimentomensal=valorhora*horastrabalho*diastrabalho
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    vencimentomensal=valorhora*horastrabalho*diastrabalho
NameError: name 'horastrabalho' is not defined
>>> vencimentomensal=valorhora*horasdetrabalho*diastrabalho
>>> nome=michel
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nome=michel
NameError: name 'michel' is not defined
>>> nome='Michel'
>>> print(valorhora)
4
>>> print(diastrabalho)
30
>>> print(horasdetrabalho)
8
>>> print(vencimentomensal)
960
>>> print(nome)
Michel
>>> nomero1=11
>>> numero2=10
>>> resultado=nomero1+numero2
>>> print(resultado)
21
>>> 
