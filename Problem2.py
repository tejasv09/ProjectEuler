


first, second = 1, 2
count = 0
while True:
    if second > 4000000: break
    if second % 2 == 0: count = count + second 
    first, second = second, first + second
    print(count)

print(count)

