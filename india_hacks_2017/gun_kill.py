def killPerson(person,target,end):
    if(target > len(person)):
        target -= len(person)
    del(person[target])
    end = len(person)

ip = input().split(" ")

N,K,X = int(ip[0]),int(ip[1]),int(ip[2])

person = list()
for i in range(1,N):
    person.append(int(i))
start = 1
end = N  

while(start != end):
    for i in range(1,(X%K)):
        killPerson(person,(X+1),end)