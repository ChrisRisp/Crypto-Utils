from random import randint


# Fermat's Little Theorem
def isPrime(n):
    return pow(2, n-1, n) == 1


if __name__=='__main__':
   
    prime1, prime2  = False, False
    
    while not prime2:    
        select = randint(10000000,20000000)
        prime1 = isPrime(select)

        if prime1:
            p = (2*select + 1)
            prime2 = isPrime(p)
            if prime2:
                print select
                break
        else:
            print 'No Prime:' + str(select)

