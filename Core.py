import random
import os
import time

f = open('MaksSongs', 'r')
f = f.readlines()

i = 'More!'
while i != 'Stop':

    print(random.choice(f))
    time.sleep(3)
    i = input('if u wanna see more - input "More!" or smth else\n')
    time.sleep(3)
    #os.system('cls')