import sys, random
b = 0
n = sys.argv[1]
n = int(n)
for i in range(1, n):
    x = random.uniform(-1, 1)
    a = float('{:.4f}'.format(x))
    print(a)
    b += a
b /= n
print(b)