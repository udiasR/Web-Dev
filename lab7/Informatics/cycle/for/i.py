sum = 0


nums = list(map(int, input().split()))

for x in range(0, 100):
    sum+=nums[x]

print(sum)