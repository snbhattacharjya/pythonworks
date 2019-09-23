def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def calculate_sets(n):
    set_count = 0
    if (n < 2):
        return 0
    elif (n == 2):
        return 2
    else:
        for i in range(2,n):
            set_count += int(factorial(n)/factorial(n-i))
        return set_count + factorial(n)

def odd_count(n):
    odd_count = 1
    for i in range(2,n+1):
        if (i%2 != 0):
            odd_count += 1
    return odd_count

def even_count(n):
    even_count = 0
    for i in range(2,n+1):
        if (i%2 == 0):
            even_count += 1
    return even_count

N = int(input())
print(N + calculate_sets(odd_count(N)) + calculate_sets(even_count(N)))