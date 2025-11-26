def addding(num1,num2):
    return num1+num2
try:
    num1 = 10
    num2 = 'pp'
    num =addding(num1,num2)

except TypeError as e: 
    print("Looks like an issue with your inputs", e)

else:
    print("Hooray !")
    print(num)
