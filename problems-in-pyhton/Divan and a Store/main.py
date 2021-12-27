details = []
chocolates = []
num = input()
for i in range(int(num)):
    details.append([int(e) for e in input().split(' ')])
    chocolates.append([int(e) for e in input().split(' ')])

for i in range(int(num)):
    chocolates_trim = sorted([e for e in chocolates[i] if details[i][1] <= e <= details[i][2]])
    to_buy = 0
    for j in range(len(chocolates_trim)):
        if to_buy + chocolates_trim[j] <= details[i][3]:
            to_buy += chocolates_trim[j]
        else:
            print(j)
            break
        if j == len(chocolates_trim) - 1:
            print(len(chocolates_trim))
    if len(chocolates_trim) == 0:
        print(0)

