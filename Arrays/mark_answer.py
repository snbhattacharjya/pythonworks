ip = input()
ip = ip.split(" ")
N,X = int(ip[0]),int(ip[1])

ip = input()
ip = ip.split(" ")

if(len(ip) != N):
    print("Mismatching N!!! ",len(ip),N)
    quit()

skip_flag = 0
attempt_count = 0

for Ai in ip:
    if(int(Ai) <= X):
        attempt_count +=1
    elif(int(Ai) > X and skip_flag == 0):
        skip_flag = 1
    elif(skip_flag != 0 and int(Ai) > X):
        break
        

print(attempt_count)
