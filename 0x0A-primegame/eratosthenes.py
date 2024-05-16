#!/usr/bin/python3

# N is the given number, to find all prime number smaller or equal to n.
# create an array of True of the len of N + 1
# starting from the first p(prime) = 2
# we find multiples of p starting from the square of p and above to N
# we update the multiple(s) index(es) in the array of True to be False


def eratosthenes(n):
    """
    Prints all prime numbers smaller or equal to n
    """
    if n % 2 == 0:
        inc = 1
    else:
        inc = 2
    prime = [True for i in range(n + 1)]
    print(prime)
    
    p = 2
    
    while (p * p <= n + 1):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    print(prime)
    
    for i in range(2, n + 1):
        if prime[i] == True:
            print(i)
eratosthenes(45)