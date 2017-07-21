print ("Welcome to the World of Python\n")
input_var = int(input("Please Enter any Number: "))
count = 0
count1 = 0
result = ""
while (count < input_var):
    while (count1 <= count):
        result += "*"
        count1 += 1
    count1 = 0
    count += 1
    print (result)
    result = ""


print ("Good bye!")

print ("Thanks...Visit us Again")
