n = 0
s = 0

a = int(input())
while a != 0:
    n += 1
    s += a
    a = int(input())

if n:
    print(s/n)
else:
    print(0)
