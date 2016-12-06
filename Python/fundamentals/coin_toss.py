import random

def coinToss(num_tosses):
    print "Starting the program..."
    heads = 0
    tails = 0
    for num in range(num_tosses):
        result = int(round(random.random()))
        print result
        if (result is 1):
            coin = "head!"
            heads += 1
        else:
            coin = "tail!"
            tails += 1
        print "Attempt #" + str(num + 1) + ": Throwing a coin... It's a " + str(coin) + " ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "Ending the program, thank you!"

coinToss(5000)
