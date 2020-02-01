# -*- coding:utf-8 -*-
# import libraries
import random
import os

# Classes and sub-classes
class Hangman():

    def show_head():
        print('\n ---------------- JOGO DA FORCA ---------------- ')

    def show_chosen_word():
        # print the chosen one
        print('\nA palavra sorteada foi: {}'.format(chosen_word))

    def show_board():
        print(board[incr])

    def show_status():
        # print errors list
        #print('\nTamanho da lista de erros: ' + str(len(mistake_list)))
        # print chosen word
        #print('\nTaamanho da lista da ´palavra sorteada: ' + str(len(chosen_word)))
        # print hints
        print('\nAcertos: {}'.format(success_list))
        # print mistakes
        print('\nErros: {}'.format(mistake_list))

# list that displays the hangman
board = ['''
  +-------------+
  |             |
  |
  |
  |
  |
  |
  |
  |
             ''',
             '''
  +-------------+
  |             |
  |             O
  |
  |
  |
  |
  |
  |             
             ''',
             '''
  +-------------+
  |             |
  |             O
  |             |
  |             |
  |
  |
  |
  |           
             ''',
             '''
  +-------------+
  |             |
  |             O
  |            /|
  |             |
  |            
  |
  |
  |           
             ''',
             '''
  +-------------+
  |             |
  |             O
  |            /|\ 
  |             |
  |            
  |
  |
  |           
             ''',
             '''
  +-------------+
  |             |
  |             O
  |            /|\ 
  |             |
  |            /
  |
  |
  |                
             ''',
             '''
  +-------------+
  |             |
  |             O
  |            /|\ 
  |             |
  |            / \ 
  |
  |
  |             
             ''']

# importing txt file
with open('C:\github\python\python_fundamentos_dsa\Cap05\Lab03\palavras.txt', 'r') as file:
    words = file.read()

# printing the content
print('\n' + words)

# transform content in list
words_list = words.split('\n')
words_list.remove('')

# choose a randomic word in a list
chosen_word = random.choice(words_list)

# success and mistake lists
success_list = []
mistake_list = []

# incremental variable
incr = 0

# guess if there is a letter in a word
while len(mistake_list) < len(board)-1:
    Hangman.show_head()
    Hangman.show_chosen_word()
    Hangman.show_board()
    Hangman.show_status()
    chosen_letter = input(str('\nEscolha uma letra: '))
    if chosen_letter in chosen_word:
        print('\nTem a letra "{}" na palavra {}'.format(chosen_letter, chosen_word))
        success_list.append(chosen_letter)
        os.system('cls')
    else:
        print('\nNão tem a letra "{}" na palavra "{}"'.format(chosen_letter, chosen_word))
        mistake_list.append(chosen_letter)
        os.system('cls')
        incr += 1


