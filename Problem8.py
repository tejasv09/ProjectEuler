with open("Problem7.txt", 'r') as myfile: data = myfile.read().replace('\n', '')
main = list(map(int, list(''.join(str(line) for line in data))))
main = ''.join(str(i) for i in main)


largestProduct = 0
for i in range(0, len(main) - 13 + 1):
    product = 1
    for j in range(i, i + 13):
        product *= int(main[j: j + 1])

    if product > largestProduct:
        largestProduct = product

print(largestProduct)
    
    


