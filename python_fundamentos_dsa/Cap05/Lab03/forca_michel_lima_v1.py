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

    def show_display_list(x):
        for i in range(len(chosen_word)):
            x.append('_')

        print(' '.join(x))

    def update_display_list(cw, cl, dl):

        cw = dict(enumerate(cw))
        cl = dict(enumerate(cl))
        dl = dict(enumerate(dl))

        for i, j in zip(cw, cw.values()):
            for x, y in zip(cl, cl.values()):
                if j == y:
                    dl[i] = y
                else:
                    continue


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
             ''']

# list that displays wich word the user have been guessed
display_list = []

# importing txt file
with open('palavras.txt', 'r') as file:
    words = file.read()

# printing the content
#print('\n' + words)

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
    Hangman.show_display_list(display_list)
    Hangman.show_status()

    chosen_letter = input(str('\nEscolha uma letra: '))

    if chosen_letter in chosen_word:
        #print('\nTem a letra "{}" na palavra {}'.format(chosen_letter, chosen_word))
        success_list.append(chosen_letter)

        Hangman.update_display_list(chosen_word, chosen_letter, display_list)

        os.system('cls')
    else:
        #print('\nNão tem a letra "{}" na palavra "{}"'.format(chosen_letter, chosen_word))
        mistake_list.append(chosen_letter)
        os.system('cls')
        incr += 1

os.system('cls')
Hangman.show_head()
Hangman.show_chosen_word()
Hangman.show_board()
print('--------------- GAME OVER =(  ---------------- ')