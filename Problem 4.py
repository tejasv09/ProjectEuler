def check(number):
    number = str(number)
    start, end = 0, len(number) - 1
    while start < end:
        if number[start] != number[end]: return False
        start, end = start + 1, end - 1

    return True
        

def main():
    final = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if check(product):
                final.append(product)
                
    return max(final)

    

print(main())

    
        
        
