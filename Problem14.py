def recurse(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0: return 1 + recurse(n/2)
        else: return 1 + recurse(3*n + 1)
    

final = {i: recurse(i) for i in range(1, 1000000)}
m = max(final.values())
for key, value in final.items():
    if value == m:
        print(key)
        break


    
