nums = []
num = input()
for i in range(int(num)):
    nums.append(int(input()))


for i in range(int(num)):
    num_here = nums[i]
    print(' '.join([str(e+2) for e in range(num_here)]))
