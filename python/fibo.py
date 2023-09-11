print("Fibonacci Sequence\n>>>\n")

def fibo(n):
    if n < 2:
        return n
    a, b = 0, 1
    for z in range(n - 1):
        a, b = b, a + b
    return b

i = int(input('Input last number: '))
#i = 10

print("\n")

# Case 1
print('# Case 1')
a = []
for y in range(0, i):
    a.append(fibo(y))
print(a, "\n")

# Case 2
print('# Case 2')
b = [0, 1]
if y > 2:
    for y in range(2, i):
        b.append(b[-1] + b[-2])
print(b, "\n")

# Case 3
print('# Case 3')
c = [0, 1]
for y in range(1, i - 1):
    c.append(c[y - 1] + c[y])
print(c, "\n")

del i, a, b, c