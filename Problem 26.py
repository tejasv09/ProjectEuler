def permute(iterable):
    dp = {i:[] for i in range(1, len(iterable) + 1)}
    dp[1].append(iterable)
    for i in range(2, len(iterable) + 1):
        for k in dp[i - 1]:
            first, second = k[:i], k[i:]
            dp[i].append(first + second)
            for j in reversed(range(0, len(first) - 1)):
                first[-1], first[j] = first[j], first[-1]
                dp[i].append(first + second)
                first[-1], first[j] = first[j], first[-1]


    final = [int(''.join(str(j) for j in i)) for i in dp[10]]
    return sorted(final)[999999]
        
            

print(permute([0,1,2,3,4,5,6,7,8,9]))


            
                
                
            
            
            
                    
                    
                
                
                
                
        
                   
    
    


