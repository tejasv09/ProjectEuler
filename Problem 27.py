def prime(number):
    for i in range(2, number):
        if number % i == 0: return False
    return True
        



def product():
    final = {}
    for a in range(-999, 1000):
        for b in range(-999, 1000, 2):
            n = 0
            while prime(n**2 + a*n + b):
                n = n + 1
            final[(a,b)] = n
            print((a,b))

print(product())
    
