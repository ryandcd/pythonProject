# Ryan Croos
# 2/15/2021
# Lets mess around
# TO DO
# implement win counter
# fix function return if user puts in an invalid input to user
# make this more robust

# import xlrd
# import xlwt
import random # for random number generator
import time # for implementing time delays for printing in terminal

def bby_function(name, bgo, bleh):
    print(f'Hello, {name}\n')
    time.sleep(1) # create computer thinking effect
    print(f'It seems that I am talking to {bgo}!!!!!!\n')
    time.sleep(1) # create computer thinking effect
    if len(bleh) == 3:
        print(f'Why are you {bleh}!!!\n')
    elif bleh == 'not bleh': # make ROBUST
        print(f'I am happy that you are not bleh, {bgo}')



if __name__ == '__main__':
    x = input('What is your real name? ')
    y = input('Are you bingo or bungo? ')
    z = input('Bleh or not bleh? ')
    bby_function(x, y, z)



