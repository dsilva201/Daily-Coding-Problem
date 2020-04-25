s=input("Enter First String: ")
s1=input("Enter Second String:")
s2=''
for i in s:
    if i in s1:
        s2+=i
print(s2)
