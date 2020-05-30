a=eval(input("Enter 1st Integer: "))
b=eval(input("Enter 2nd Integer: "))
maximum=(int(a>b))*a + (int(b>a))*b
minimum=(int(a<b))*a + (int(b<a))*b
print("Maximum is: ",maximum)
print("Minimum is: ",minimum)
