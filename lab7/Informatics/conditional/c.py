a = input()

b = int(input())

if(len(a) != 4 and b != 1): print("YES")
else:
    if(len(a) == 4):
        c = int(a)
        if(c%100 == c/100 and b == 1):
            print("YES")
        else: 
            print("NO")
    else: 
        print("NO")
