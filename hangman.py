import random

def get_guess():
    while True:
        guess = raw_input("Guess: ")
        if len(guess)>1:
            print "Your guess must have exactly one character!"
            continue
        if not guess.islower():
            print "Your guess must be a lowercase letter!"
            continue
        if guess.islower() and len(guess) == 1:
            break
        
    return guess

def update_dashes(secret_word,dashes,guess):
    l = list(secret_word)
    d = list(dashes)
    new = ""
    if guess in secret_word:
        for i in range(len(l)):
            if l[i] == guess:
                new += guess
            else:
                new += d[i]
    return new


words = ["eggplant","eda","dark","hello","sprite"]

secret_word = random.choice(words)
dashes = "-"*len(secret_word)
con = True
guesses_left = 10
while con:
    print(dashes)
    print str(guesses_left)+" incorrect guesses left."
    letter = get_guess()
    if letter in secret_word:
        dashes = update_dashes(secret_word,dashes,letter)
    if dashes == secret_word:
        print "Congrats! You win. The word was: "+secret_word
        con = False
    else:
        print "That letter is not in the secret word!"
        guesses_left -= 1
        if guesses_left == 0:
            print "You lose. The word was: "+secret_word
            con = False


