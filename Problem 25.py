c, n = 1, 1
counter = 2
while True:
    c, n = n, c + n
    counter = counter + 1
    if len(str(n)) == 1000:
        print(counter)
        break
        
    
