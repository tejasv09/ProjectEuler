
def change(amount, coins):`
    w
    ays = {}
    ways[0] += 1
    for coin in coins:
        for total in range(amount+1):
            ways[total] += ways[total-coin]
    return ways[amount]

print(change(200, [1,2,5,10,20,50,100,200]))
