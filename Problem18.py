#Problem 18 and 67 Project Euler
with open("Problem18.txt", 'r') as myfile: final = [line.strip().split() for line in myfile][::-1]
print(final)

for i in range(len(final)):
    for j in range(len(final[i])):
        final[i][j] = int(final[i][j])



        
for i in range(len(final) - 1):
    for j in range(1, len(final[i])):
        final[i+1][j-1] += max(final[i][j], final[i][j-1])

print(final[-1])
    
        
  
    
     
    
        
        
