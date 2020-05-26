def largest(number):
    main = []
    for i in range(2, number):
        if prime(number):
            print('a')
            if number == 1: return max(main)
            while number % i == 0:
                number /= i
            main.append(i)
        else:
            continue

    
    


def prime(number):
    for i in range(2, number): 
        if number % i == 0: 
            return False
    return True


print(largest(13195))

    

    


    
        
            

    
