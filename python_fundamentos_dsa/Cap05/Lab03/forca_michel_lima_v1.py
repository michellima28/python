# -*- coding:utf-8 -*-
# import libraries
import random
import os

# classes and sub-classes
class Hangman():

    def show_header():
        print('\n ---------------- JOGO DA FORCA ---------------- ')

    def import_file():
        with open('palavras.txt', 'r') as file:
            w = file.read()
            return w

    def words_list():
        wl = words.split('\n')
        wl.remove('')
        return wl

    def chosen_word():
        cw = random.choice(words_list)
        return cw

    def show_chosen_word():
        print('\n  A palavra era: {}' .format(chosen_word))


    def ask_a_letter():
        cl = input(str('\n  Escolha uma letra: '))
        return cl

    def show_board(i):
        print(board[i])

    def display_list(cw):
        ds = []
        for i in range(len(cw)):
            ds.append('_')
        return ds

    def show_display_list():
        print('  {}' .format(display_list))

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

        return list(dl.values())

    def show_status(sl, ml):
        #print('\n  Acertos: {}'.format(sl))
        print('\n  Erros: {}'.format(ml))

    def show_game_over():
        print('  --------------- GAME OVER =(  ---------------- ')

# list that shows the hangman
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

# creating objects
words = Hangman.import_file()
words_list = Hangman.words_list()
chosen_word = Hangman.chosen_word()
display_list = Hangman.display_list(chosen_word)
success_list = []
mistake_list = []
incr = 0

# guess if there is a letter in a word
while len(mistake_list) < len(board)-1:

    Hangman.show_header()
    Hangman.show_board(incr)
    Hangman.show_display_list()
    Hangman.show_status(success_list, mistake_list)
    chosen_letter = Hangman.ask_a_letter()

    if chosen_letter in chosen_word:
        success_list.append(chosen_letter)
        display_list = Hangman.update_display_list(chosen_word, chosen_letter, display_list)
        os.system('cls')
    else:
        mistake_list.append(chosen_letter)
        os.system('cls')
        incr += 1

os.system('cls')
Hangman.show_header()
Hangman.show_board(incr)
Hangman.show_game_over()
Hangman.show_chosen_word()