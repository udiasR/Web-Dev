n = int(input())

nums = list(map(int, input().split()))

ok = False
for x in range(len(nums)-1):
    if (nums[x] > 0 and nums[x+1] > 0) or (nums[x] < 0 and nums[x+1] < 0):
        ok = True

if ok:
    print("YES")
else:
    print("NO")