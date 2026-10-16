def fib_recursive(n): #tc = O(2^n), sc = O(n)
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n): #tc = O(n), sc = O(1)
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))

print("Recursive:")
for i in range(n):
    print(fib_recursive(i), end=" ")

print("\nIterative:")
fib_iterative(n)