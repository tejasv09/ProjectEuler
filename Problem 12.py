i = 1
while True:
    t = i * (i + 1) / (2)
    count = 0
    for k in range(1, int(t) + 1):
        if t % k == 0:
            count = count + 1
    if count > 500:
        print(t)
        break
    count = 0
    i = i + 1


    

