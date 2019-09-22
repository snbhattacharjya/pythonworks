def P(s,i):
    op = formatS(s,i)
    px = 0
    k = 0
    for j in op:
        px += ((ord(j)-96) * (2**(-1 * k)))
        k+=1
    return px


def formatS(s,i):
    if(i == (len(s)-1)):
        return s
    else:
        return s[i+1:len(s)]+s[0:i+1]


S = input()
max = 0
max_s = ''

for i in range(0,len(S)):
    
    if(max == 0):
        max = P(S,i)
        max_s = formatS(S,i)
    elif(max < P(S,i)):
        max = P(S,i)
        max_s = formatS(S,i)
    
 

print(max_s)

#for i in range(0,len(S)):
    #print(formatS(S,i))