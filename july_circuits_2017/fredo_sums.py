def formPairs(ip,N,op):
    for i in range(N):
        for j in range(i+1,N):
            #op.append([i,j,abs(int(ip[i])-int(ip[j]))]) 
            op.append([i,j])

def formUniquePairs(ip,N,op):
    unique_set = list()
    for i in len(ip):
        unique_set.append(ip[i])
        for j in range(i+1,len(ip)):
            if(foundUnique(ip[j],ip[i])):
                if(len(unique_set) != int(N/2)):
                    unique_set.append(ip[j])
                else:
                    
    for i in range(0,len(op)):
        op[i] = op[i][2] + op[i][5]


def foundUnique(ip,op):
    retVal = True
    for li in ip:
        if(li in op):
            retVal = False
    
    return retVal



T = int(input())
all_pairs = list()
unique_pairs = list()
for i in range(0,T):
    N = int(input())
    A = input().split(" ")
    if(N == 2):
        print(abs(int(A[0])-int(A[1])),abs(int(A[0])-int(A[1])))
    else:
        formPairs(A,N,all_pairs)
        #formUniquePairs(all_pairs,N,unique_pairs)
        print(len(unique_pairs))
        #print(min(unique_pairs),max(unique_pairs))

    