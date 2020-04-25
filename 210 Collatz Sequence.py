def collatzsequence(n):
    L=[n]
    while n>1:
        if n%2==0:
            n=int(n/2)
            L.append(n)
        else:
            n=int((3*n)+1)
            L.append(n)
    return L
x=int(input("Enter Number: "))
print(collatzsequence(x))
