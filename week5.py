#normal
a = 1
b = 2
sum = a + b
minus = b - a
multiply = a * b
divide = b / a



#print(divide)
#print("Hello World")

#OOP
def SUM(a,b,c):
    sum = int(a) + int(b) + int(c)
    return sum

def MINUS(a, b):
    sum = int(a) - int(b)
    return sum

def MULTIPLY(a, b):
    sum = int(a) * int(b)
    return sum

def DIVIDE(a, b):
    sum = int(a) / int(b)
    return sum

operate = input("1 = Sum :, 2 = Minus :, 3 = Multiply :, 4 = Divine :")

if(operate == "1"):  
    inp1 = input("A : ")
    inp2 = input("B : ")
    inp3 = input("C : ")
    print("SUM = ",SUM(inp1, inp2, inp3))  
elif(operate == "2"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print("MINUS = ",MINUS(inp1, inp2,))
elif(operate == "3"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print("MULTIPLY = ",MULTIPLY(inp1, inp2,))
elif(operate == "4"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print("DIVIDE = ",DIVIDE(inp1, inp2,))
else:
    print("Not found")


#รับค่า keyboard
#inp1 = input("A : ")
#inp2 = input("B : ")
#inp3 = input("C : ")
#print("SUM = ",SUM(inp1, inp2, inp3))



#print("SUM = ", SUM(10, 11, 12))
#print("MINUS = ", MINUS(10 ,11))
#print("MULTIPLY = ", MULTIPLY(10 ,11))
#print("DIVIDE = ", DIVIDE(10 ,11))