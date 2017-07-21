ip_str = input()
op_str = ''
for chr in ip_str:
    if chr.islower():
        op_str += chr.upper()
    else:
        op_str += chr.lower()
print(op_str)