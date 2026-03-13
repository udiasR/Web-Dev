n = int(input())


nums = list(map(int, input().split()))


cnt = 0
for x in nums:
    if x> 0:
        cnt+=1

print(cnt)