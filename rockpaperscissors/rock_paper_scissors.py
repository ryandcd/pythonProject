# Ryan Croos
# 11/24/2021
# Lets mess around
# TO DO
# implement win counter
# fix function return if user puts in an invalid input to user
# make this more robust

# import xlrd
# import xlwt
import random # for random number generator
import time # for implementing time delays for printing in terminal



# rock paper scissors function
def rps(): # user inputs either 'rock' 'paper' or 'scissors'
    user = input("Let's play rock paper scissors. What is your hand? ")
    while True: # check for valid user input
        if user in ('rock', 'paper', 'scissors', 'scissor', 'Rock', 'Paper', 'Scissors', 'Scissor'):
            break
        else:
            print('Invalid Input')
            return

    # assigning variables for hands to be added to array 'rock' 'paper' 'scissor'
    r = 'rock'
    p = 'paper'
    s = 'scissors'

    # create array for the potential hands
    rps = [r, p, s]

    # use the "random" module to pick out strong from rps array
    comp = rps[random.randint(0,2)]
    print('The computer has chosen...')
    time.sleep(1)  # 1 second delay in terminal for a "thinking" effect
    print(comp.capitalize() + '!')
    time.sleep(1)  # 1 second delay in terminal for a "thinking" effect

    # rules for determining winner
    # rock conditions
    if user == 'rock' and comp == s:
        print("Calculating....")
        time.sleep(1)
        print('Rock beats Scissors! You win!')
            # add play again option later
    elif user == 'rock' and user == comp:
        print("Calculating....")
        time.sleep(1)
        print('Tie! Draw again')
    elif user == 'rock' and comp == p:
        print("Calculating....")
        time.sleep(1)
        print('Paper beats rock! You lost :(')

    if user == 'paper' and comp == r:
        print("Calculating....")
        time.sleep(1)
        print('Paper beats rock! You won!')
    elif user == 'paper' and user == comp:
        print("Calculating....")
        time.sleep(1)
        print('You both chose paper, draw again')
    elif user == 'paper' and comp == s:
        print("Calculating....")
        time.sleep(1)
        print('Scissors beats paper! You lost...')

    if user == 'scissors' or user =='scissor' and comp == p:
        print("Calculating....")
        time.sleep(1)
        print('Scissors beats paper. You won!')
    elif user == 'scissors' or user == 'scissor' and comp == s:
        print("Calculating....")
        time.sleep(1)
        print('You have both drawn..... scissors, draw again')
    elif user == 'scissors' or user == 'scissor' and comp == r:
        print("Calculating....")
        time.sleep(1)
        print('You lost!')

# restart the function based on user input 'y' or 'n'
while True:
    rps()
    while True:
        ans = input('Play again? (y/n): ')
        if ans in ('y', 'n'):
            break
        print('Invalid Input\n')
    if ans == 'y':
        continue
    else:
        print('Thanks for playing!')
        break