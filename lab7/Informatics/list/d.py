n = int(input())

nums = list(map(int, input().split()))

last = nums[0]

cnt = 0
for x in nums:
    if x > last:
        cnt+=1
    last = x

print(cnt)