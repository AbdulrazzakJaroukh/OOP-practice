
ss = []
num = input()
for i in range(int(num)):
    ss.append(input())

for i in range(int(num)):
    if not len(ss[i]) % 2 == 0:
        print('NO')
    elif ss[i][:len(ss[i])//2] == ss[i][len(ss[i])//2:]:
        print('YES')
    else:
        print('NO')
