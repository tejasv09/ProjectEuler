with open('Problem13.txt', 'r') as myfile:
    s = sum(int(line) for line in myfile)
    print(s)
