d={1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U',
   22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
n=int(input("Enter Any Integer: "))
s=''
while n>0:
    if n>=1 and n<=26:
        s+=d[n]
        break
    elif n>26:
        r=n//26
        while r>26:
            r=r//26
            s+=d[r]
            if r>1:
                r=r%26
                s+=d[r]
        s+=d[r]
        n=n%26
        continue
print(s)
