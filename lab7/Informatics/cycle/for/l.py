s = input()

res = 0

k = 1

s = s[::-1]

for x in range(len(s)):
    if s[x] =='1':
        res+=k
    k*=2

print(res)