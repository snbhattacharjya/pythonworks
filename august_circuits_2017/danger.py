cost=int(input())
danger_val = 0
i = 1
while(i <=cost):
    if((cost % i) == 0):
        danger_val += 1
        print("Incremented When i = ",i)
    i+=1
    
print(danger_val)