def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def sum(g,row,col,n):
    if(row == 0):
        top = 0
    else:
        top = g[row-1][col]
    if(col == 0):
        left = 0
    else:
        left = g[row][col-1]
    if(col == n-1):
        right = 0
    else:
        right = g[row][col+1]
    if(row == n-1):
        bottom = 0
    else:
        bottom = g[row+1][col]
    
    return top+left+right+bottom


n = int(input())
g = list()
li = list()
prime_cells = 0
for i in range(0,n):
    ip = input().split(" ")
    for j in range(0,n):
        ip[j]=int(ip[j])

    g.append(ip)
for i in range(n):
    for j in range(n):
        if(isPrime(sum(g,i,j,n))):
            prime_cells += 1
print(prime_cells)