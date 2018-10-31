
import random
random_number = random.randint (1,2)
guess = ""
print ("I'm thinking of a number between 1 and 10. \nPLease guess what it is: ")
while guess != random_number:

    guess = input("")
    try:
        if random_number < int(guess):
            print ("That's too high!")
            continue
        elif random_number > int(guess):
            print ("That's too low!")
            continue
        elif random_number == int(guess):
            print ("That's it! You got it!")
            break
        else:
            print ("That's not an option. Please try again.")
            continue
    except ValueError:
        print ("D'oh! That is NOT a number, Bart!")
        continue
