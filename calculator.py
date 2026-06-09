n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
operation=input("Enter the operation(+,-,*,/):")
if operation=="+":
    result=n1+n2
elif operation=="-":
    result=n1-n2
elif operation=="*":
    result=n1*n2 
elif operation=="/":
    if n2 !=0:
        result=n1/n2
    else:
        result="Divisible by zero is not allowed"
else:
    result="Invalid operation"
print("Result=",result)                          