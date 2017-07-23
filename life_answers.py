ip_lock = 0
op = list()
while(ip_lock == 0):
    ip = int(input())
    if(ip != 42):
        op.append(ip)
    else:
        ip = int(input())
        ip_lock = 1

for Ai in op:
    print(Ai)