import random

secret_number= random.randint(1,100) # get a number randomly
#print(secret_number)
print("*** YOU HAVE 6 CHANCES TO GUESS THE NUMBER *** ")
print("(NUMBER RANGE 1 to 100)")
for count in range(6):
    try:
        user_number= float(input("Enter your number: "))
        if user_number!= secret_number:        # check that both numbers are not equals
            print('Your guessing is wrong.')
            if user_number> secret_number:     # check the gap between secret_number and user_number 
                print('It is too high.')
            else:
                print('It is too low.')
        else:
            print(f'Your guessing is correct.\nThe secret number is {secret_number}.\nYou got {count+1} chances to guess.')
            break
    except ValueError:
        print('Invalid Input.')
print()
if user_number!= secret_number and count== 5:
    print('You cannot guess')
print('End')
