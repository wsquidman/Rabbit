# Copyright (c) 2022, w_squidman. All rights reserved.

import random
import hashlib
import time

class bcolors: # text print colors
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

print(bcolors.OKGREEN + """ 
       ()_
       ( _)
       / \__
     O/ _/`"`
      \  )_
       `""`"
""")

print(bcolors.WARNING + "WARNING: Warren is not responsible for malicious use of this program. With great power comes great responsibilty. (as an old man in a spiderman movie once said)")

# actual program LMAO
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+=/?\;:'|`~}{][_><"
characterList = list(characters)
guess = ""

hash = input(bcolors.HEADER + "hash: ")

charLimitInput = input(bcolors.HEADER + "character limit: ")
charLimit = int(charLimitInput)

while True: # skiddy me timbers this is gonna take a while
    guess = random.choices(characterList, k = charLimit)
  
    print(guess)
    guess = "".join(guess)
    print(bcolors.UNDERLINE + guess)
    encodedGuess = guess.encode("utf-8")
    digest = hashlib.md5(encodedGuess.strip()).hexdigest() # set "md5" in "hashlib.md5" to the encoder type.
  
    if digest == hash:
      print(bcolors.OKGREEN + "hash decoded, showing password...")
      time.sleep(2)
      print("password: " + guess)
      break
