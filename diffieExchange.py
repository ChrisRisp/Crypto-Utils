
#Group Modulus
p = input('Enter Modulus: ')

#Generator
g = input('Enter Generator: ')

#Secret Alex
seca = input('Enter Alex Secret: ')

#Secret Blake
secb = input('Enter Blake Secret: ')


def exchange():
    # Exchanging Secrets
    B = pow(g,secb,p)
    print 'Blake sends ..', B
    A = pow(g,seca,p)
    print 'Alice sends ..', A

    # Shared Key
    K1 = pow(B,seca,p)
    K2 = pow(A,secb,p)

    print 'Our keys ...', K1, K2
  


if __name__ == "__main__": 
    exchange()
