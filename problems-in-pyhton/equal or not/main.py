
ss = []
num = input()
for i in range(int(num)):
    ss.append(input())

results = []
for i in range(int(num)):
    count = 0
    for letter in ss[i]:
        if letter == 'N':
            count += 1
    if count == 1:
        print('NO')
    else:
        print('YES')



