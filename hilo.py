low = 1
high = 1000
print("Please guess a number between {} and {}".format(low, high))
input("Please ENTER START")

guesses = 1
while low != high:
    #The loop terminates when it figures the low and high are the same
    #print("Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2 #Binary search formula
    high_low = input("My guess is {}. Should I guess higher or lower?\n"
                     "Enter h, or l, or c if my guess was correct ".format(guess)).casefold()

    if high_low == 'h':
        #Guess higher. The low end of the becomes 1 greater than he guess
        #pass helps to hold the compiler from excuting this untill you put in the real code
        low = guess +1

    elif high_low == 'l':
        high = guess -1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break #out of the loop

    else:
        print("Please enter h, l or c")
    #guesses = guesses + 1  ---Augmented Assignment---#
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))