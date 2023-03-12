x = int(input())

found = False
for d in range(2, int(x**0.5)+1):
    if x % d == 0:
        print(d)
        found = True
        break

if not found:
    print(x)
