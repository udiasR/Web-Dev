n = int(input())

arr = list(map(int, input()).split())

res = []

for x in range(len(arr)):
    if arr[x]%2==0:
        res.append(arr[x])
        
print(res)