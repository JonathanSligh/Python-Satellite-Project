import math

# Sieve of Eratosthenes
# Parameters: int maxNumber
# Returns: List of all prime numbers up to the max number given as the parameter
def calc(maxNumber):
    try:
        testIfInt = int(maxNumber)
    except:
        raise ValueError("FA04.calc():  Parameter is not an integerS")
    if maxNumber < 2: 
        return []
    
    maxNumber = maxNumber + 1
    potentialPrimes = [True for numbs in range(0, maxNumber)]
    potentialPrimes[0] = False
    potentialPrimes[1] = False

    potentialPrimes = nonPrimeEliminator(potentialPrimes, maxNumber)
    
    primes = []
    for eachPrime in range(0, maxNumber):
        if potentialPrimes[eachPrime]:
            primes.append(eachPrime)
    return primes

#Function that goes through the list of all potentially prime numbers and eliminates all the multiples (all the non-prime numbers)
#Parameters: list potentialPrimes and int maxNumber
#Returns: a list of numbers where the prime indexes are true
def nonPrimeEliminator(potentialPrimes, maxNumber):
    for eachNumber in range(2, int(math.sqrt(maxNumber) + 1)):
        if potentialPrimes[eachNumber]:
            for multiples in range(2 * eachNumber, maxNumber, eachNumber):
                potentialPrimes[multiples] = False
    return numbers

                

