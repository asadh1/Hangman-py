# -*- coding: utf-8 -*-

import os
import pwd
import random
import re
import sys

# Functions
def clear():
  '''Clears the shell.'''
  os.system('cls' if os.name == 'nt' else 'clear')

def get_word(file_path):
  '''Gets words from the file path that was passed in.'''
  if file_path != None:
    file = open(file_path)
    data = file.readlines()
    file.close()
    words = re.split(r', ', data[0])
  else:
    words = ["placeholder", "placeholder", "placeholder"]
  return random.choice(words)

def start_hangman(file_path = None):
  '''Receives a letter or action from user.'''
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  word = get_word(file_path)
  word_progress = '_' * len(word)
  used_letters = []
  tries = 5
  game_over = False
  
  while True:
    print("Type a letter for your guess or type 'quit' to quit.")
    print("Guess the word: {}".format(word_progress))

    # Take the right input
    if sys.version_info.major == 3:
      latest_input = input(">>> ")
    elif sys.version_info.major == 2:
      latest_input = raw_input(">>> ")

    # Check input
    if len(latest_input) != 1 and latest_input.lower() != 'quit':
      clear()
      print("Sorry, that’s not a valid answer. Answer must be only one letter.\nPlease try again or type 'quit’ to quit.\n")
      continue
    elif latest_input not in alphabet and latest_input != 'quit':
      clear()
      print("Sorry, that’s not a valid answer.Make sure your answer is a letter.\n")
      continue
    elif latest_input in used_letters:
      clear()
      print("You’ve used that letter already!\n")
      continue
    elif latest_input == 'quit':
      print("[Game Ended]")
      break
    else:
      used_letters.append(latest_input)
      if latest_input in word:
        clear()
        print("You guessed right!\n")
        word_progress_list = list(word_progress)
        for index in [count.start() for count in re.finditer(latest_input, word)]:
          word_progress_list[index] = latest_input
        word_progress = ''.join(word_progress_list)

        # Check if the player won.
        if word == word_progress:
          print("You’ve won! The word was {}.\n[Game Ended]".format(word))
          break
        else:
          continue

      else:
        clear()
        tries -= 1
        print("Nice guess, but {} is not in the word.\n".format(latest_input))

        # Check if the player lost.
        if tries == 0:
          print("Sorry, you’ve run out of turns.The word was: {}.\n[Game Ended]".format(word))
          break
        continue
start_hangman("/Users/{}/Downloads/Hangman-py-master/hangman_words.txt".format(pwd.getpwuid(os.getuid())[0]))
