def factorial(num):
    res = 1
    for i in range(1,num):
        res += res * i
    return res

ip = input().split(" ")
N,M = int(ip[0]),int(ip[1])

print(int(factorial(M) / factorial(N%M) * factorial(N-M)))