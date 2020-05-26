with open('Problem11.txt', 'r') as myfile:
    main = myfile.read().rstrip().split()




temp = [[list(map(int, main))[i] for i in range(0 + k*20, 20 + k*20)] for k in range(0, 20)]
maxProducth = 0
for i in range(len(temp)):
    for j in range(len(temp[i]) - 4 + 1):
        product = 1
        for k in range(j, j + 4):
            product *= temp[i][k]

        
        if product > maxProducth:
            maxProducth = product
        

ttemp = list(zip(*temp))
maxProductv = 0
for i in range(len(ttemp)):
    for j in range(len(ttemp[i]) - 4 + 1):
        product = 1
        for k in range(j, j + 4):
            product *= ttemp[i][k]
       
        if product > maxProductv:
            maxProductv = product


maxProductD = 0
for i in range(len(temp) - 4 + 1):
    for j in range(len(temp[i]) - 4 + 1):
        product = 1
        for f in range(0, 4):
            product *= temp[i + f][j + f]
        if product > maxProductD:
            maxProductD = product

    
maxProductDT = 0
ttemp = ttemp[::-1]
for i in range(len(ttemp) - 4 + 1):
    for j in range(len(ttemp[i]) - 4 + 1):
        product = 1
        for f in range(0, 4):
            product *= ttemp[i + f][j + f]
        if product > maxProductDT:
            maxProductDT = product
print(maxProductDT)






