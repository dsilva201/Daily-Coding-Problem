import re
n=input("Enter String: ")
p=input("Enter Pattern: ")
res=[i.start() for i in re.finditer(p,n)]
print(res)
