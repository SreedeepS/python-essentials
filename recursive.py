
#Iterative
def fibonacci_iterative(n):
    current = 1
    previous = 0
    for i in range(n-1):
        current_old = current
        current = previous + current
        previous = current_old
    return current

#Using recursion. 
def fibonacci_recursive(n):
    if n == 0 or n==1:
        return n
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

#Above two functions will slow down with higher values (>50 or >100)
#Dynamic Programming

stored = {0: 0, 1: 1} 
def fibonacci_dynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fibonacci_dynamic(n - 2) + fibonacci_dynamic(n - 1)
        return stored[n]

if __name__ == 'main':
    print("Iterative :",fibonacci_iterative(3))
    print("Recursive :",fibonacci_recursive(3))
    print("Dynamic: ",fibonacci_dynamic(3))