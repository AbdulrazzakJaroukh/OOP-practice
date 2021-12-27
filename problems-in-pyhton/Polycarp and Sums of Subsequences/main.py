ss = []
num = input()
for i in range(int(num)):
    ss.append([int(e) for e in input().split(' ')])


for item in ss:
    f = False
    for i in range(len(item) - 1):
        for j in range(i+1, len(item) - 1):
            for k in range(j+1, len(item) - 1):
                if item[i] + item[j] + item[k] == item[len(item)-1]:
                    print(item[i], ' ', item[j], ' ', item[k])
                    f = True
                    break
            if f:
                break
        if f:
            break
