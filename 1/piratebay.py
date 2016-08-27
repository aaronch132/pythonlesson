import random
secret=random.randint(1,99)
guess = 0
tries = 0
print "AHOY!!!! I,m the Dread Pirate Roberts, and i have a secret!"
print "it is a number from 1 to 99.    I'll give  you 6 tries. "
while guess != secret and tries <6:
    guess=input("what's ya guess? ")
    if guess <secret:
        print "too low, ye unblessed-human !"
    elif guess > secret:
        print "too high, whatever ur name is!"
    tries= tries + 1
if guess ==secret:
    print "there ya go! found mah secret in",tries,",ye did!"
else:
    print "no more gueses! better luck next time,m8!"
    print "the secret number was",secret
