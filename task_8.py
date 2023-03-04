n = int(input()) 
counts = [] 
for _ in range(n): 
    counts.append(int(input()))

answer = 0 
for i in range(n): 
    for j in range(n-1, i, -1): 
        min_count = min(counts[i:j+1])
        amount = j-i+1
        answer += (amount-1)*(min_count)
        for el in range(i, j+1): 
            counts[el] -= min_count

print(answer)


        



