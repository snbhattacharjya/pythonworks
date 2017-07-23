n = int(input())
stack = list()
sum = 0
while (n > 0):
    value = int(input())
    stack.append(value)   
    n -= 1

while (n < len(stack)):
    if(stack[n] != 0):
        sum += stack[n]
    elif(stack[n] == 0 and (n-1) >= 0):
        sum -= stack[n-1]
    n += 1
print(sum)