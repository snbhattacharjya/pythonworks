ipstr = input()
opstr = ''

for chr in ipstr:
    opstr = chr + opstr

if ipstr == opstr:
    print("YES")
else:
    print("NO")