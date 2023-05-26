fib1 = 1
fib2 = 1

n = 40

i = 0

for i in range(1, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print("Значення цього елементу:", fib2)
