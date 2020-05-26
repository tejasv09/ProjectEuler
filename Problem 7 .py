

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def main():
    number = 2
    index = 1
    while True:
        number = number + 1
        if prime(number):
            index = index + 1
        
        if index == 10001: return number

print(main())
    
    
