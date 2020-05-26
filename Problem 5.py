

def check(number):
    for i in range(11, 21):
        if number % i != 0: return False

    return True

def main():
    i = 2520
    while True:
        if check(i): return i
        i = i + 2520
    return i



print(main())
            

    
        

    
