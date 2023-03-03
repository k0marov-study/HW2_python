n = int(input()) 
has_zero = False 
for _ in range(n): 
    x = int(input()) 
    if x == 0: 
        has_zero = True 
print("YES" if has_zero else "NO") 


