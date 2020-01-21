from random import randint
import sys
# generate a number 1 - 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user?

# check that input is a number 1 - 10
while True:
    try:
        guess = int(input("Please guess a number 1 - 10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("You're a genius!!")
                break
        else:
            print("Hey, I said between 1 and 10")
    except ValueError:
        print('Please enter a number')
        continue

# check if number is the right guess. Otherwise
# ask again.
