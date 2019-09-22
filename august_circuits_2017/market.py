def danger(cost):
    danger_val = 0
    i = 1
    while(i <= cost):
        if((cost % i) == 0):
            danger_val += 1
        i+=1

    return danger_val

def findPairs(cost,L,R):
    pairs = 0
    if(L == R):
        return pairs
    else:
        new_list = cost[L-1:R-1]
        new_list.sort()
        i = 0
        pair_count = 0
        while(i < len(new_list)):
            if(pair_count == 0):
                cmp = new_list

        return pairs    

N = int(input())
cost = input().split(" ")
for i in range(0,len(cost)):
    cost[i] = danger(int(cost[i]))

Q = int(input())
qi = list()
for i in range(0,Q):
    ip = input().split(" ")
    qi.append([int(ip[0]),int(ip[1])])

for i in qi:
    print(findPairs(cost,i[0],i[1]))