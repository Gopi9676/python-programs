def Gcd(a,b):
    if b==0:
        return a
    else:
        return Gcd(b,a%b)
x=input("enter the first integer:")
y=input("enter the second integer:")
if x.isdigit() and y.isdigit():
    a=int(x)
    b=int(y)
    result=Gcd(a,b)
    print(f"the Gcd of {a} and {b} is:",result)
else:
    print("please enter valid integer:")
