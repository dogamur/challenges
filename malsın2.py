x=int(input())
while x>1:
    if x%2==0:
     x=x//2
    print(x)

    elif x%2!=0:
     x=x*3+1
    print(x)

print(x)
