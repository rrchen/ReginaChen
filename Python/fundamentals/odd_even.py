def counter():
    for num in range (1, 2001):
        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number."
        else:
            print "Numer is " + str(num) + ". This is an odd number."

counter()
