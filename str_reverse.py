#!usr/bin/python3

def strReverse (ipStr):
	'Function for Reversing an input String'
	count = 0
	result = ""
	while (count < len(ipStr)):
		result = ipStr[count] + result
		count += 1
	return result

ipStr = input("Enter any String: ")
revStr = strReverse(ipStr)

print("The Reverse Output: ",revStr)