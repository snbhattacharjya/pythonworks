N = int(input())
H = input().split(" ")

grp_count = 0
grp_end = 0
grp_start = 0
for i in H:
    if(grp_end == 0):
        grp_count += 1
        grp_end = int(i)

    if(int(i) < grp_end):
        grp_count += 1

    grp_end = int(i)
    

print(grp_count)