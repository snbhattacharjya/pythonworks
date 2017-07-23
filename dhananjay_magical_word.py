def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def findUpperMagicLetter(asc_val):
    lower = 0
    ret_val = 0
    if(asc_val in upper_magic_list):
        return asc_val
    for ml in upper_magic_list:
        if (lower == 0):
            lower = abs(asc_val - ml)
            ret_val = ml
        elif(lower > abs(asc_val - ml)):
            lower = abs(asc_val - ml)
            ret_val = ml

    return ret_val

def findLowerMagicLetter(asc_val):
    lower = 0
    ret_val = 0
    if(asc_val in lower_magic_list):
        return asc_val
    for ml in lower_magic_list:
        if (lower == 0):
            lower = abs(asc_val - ml)
            ret_val = ml
        elif(lower > abs(asc_val - ml)):
            lower = abs(asc_val - ml)
            ret_val = ml

    return ret_val

upper_magic_list = list()
lower_magic_list = list()
for i in range(65,90):
    if(isPrime(i)):
        upper_magic_list.append(i)

for i in range(97,122):
    if(isPrime(i)):
        lower_magic_list.append(i)

t = int(input())
op = ""
res = list()
while(t > 0):
    n = int(input())
    s = input()
    for li in range(0,n):
        if(ord(s[li])>=97 and ord(s[li])<=122):
            op += chr(findLowerMagicLetter(ord(s[li])))
        elif(ord(s[li])>=65 and ord(s[li])<=90):
            op += chr(findUpperMagicLetter(ord(s[li])))
        elif(ord(s[li])<65 ):
            op += 'C'
        elif(ord(s[li])>122 ):
            op += 'q'
       elif(ord(s[li])>=91 and ord(s[li])<=93):
            op += 'Y'
        elif(ord(s[li])>=94 and ord(s[li])<=96):
            op += 'a'
    t -= 1
    res.append(op)
    op = ''

for i in (range(0,len(res))):
    print(res[i])