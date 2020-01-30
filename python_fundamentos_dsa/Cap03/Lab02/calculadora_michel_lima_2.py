# mensagem inicial
print('\n ------------- Calculadora Python -------------\n')

# funcoes aritmericas
def soma(x, y):
    return x + y 
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    return x / y

# variaveis de input
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão\n')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
operacao = int(input('\nEscolha uma das operações (1 a 4): '))

# realizando as operacoes
if operacao == 1:
    print('\n{} + {} = ' .format(num1, num2), soma(num1,num2), '\n')
elif operacao == 2:
    print('\n{} - {} = ' .format(num1, num2), subtracao(num1,num2), '\n')
elif operacao == 3:
    print('\n{} * {} = ' .format(num1, num2), multiplicacao(num1,num2), '\n')
elif operacao == 4:
    print('\n{} / {} = ' .format(num1, num2), divisao(num1,num2),  '\n')    
else:
    print('\nDados inválidos! Por favor, digite um número de 1 a 4.\n')

