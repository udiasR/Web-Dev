n = int(input())

nums = list(map(int, input().split()))

cnt = 0

for x in range(len(nums)):
    if x+1 < len(nums) and x-1 >= 0 and nums[x] > nums[x+1] and nums[x] > nums[x-1]:
        cnt+=1

print(cnt)