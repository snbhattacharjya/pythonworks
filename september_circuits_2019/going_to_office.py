def calculate_online_taxi_cost(D,Oc,Of,Od):
    if (Of > D):
        return Oc
    else:
        return Oc + (Od * (D - Of))

def calculate_classic_taxi_cost(D,Cs,Cb,Cm,Cd):
    return Cb + ((D/Cs) * Cm) + (D *Cd)

D = int(input())
online_taxi = input().split(" ")
Oc = int(online_taxi[0])
Of = int(online_taxi[1])
Od = int(online_taxi[2])

classic_taxi = input().split(" ")
Cs = int(classic_taxi[0])
Cb = int(classic_taxi[1])
Cm = int(classic_taxi[2])
Cd = int(classic_taxi[3])

online_taxi_cost = calculate_online_taxi_cost(D,Oc,Of,Od)
classic_taxi_cost = calculate_classic_taxi_cost(D,Cs,Cb,Cm,Cd)
if (online_taxi_cost <= classic_taxi_cost):
    print('Online Taxi')
else:
    print('Classic Taxi')

