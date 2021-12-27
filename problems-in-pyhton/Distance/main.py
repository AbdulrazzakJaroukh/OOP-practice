in_data = []
num = input()
for i in range(int(num)):
    in_data.append([int(e) for e in input().split(' ')])

for i in range(int(num)):
    xb = in_data[i][0]
    yb = in_data[i][1]
    for xc in range(51):
        found = False
        for yc in range(51):
            if xc + yc == (xb + yb)/2 and abs(xb - xc) + abs(yb - yc) == (xb + yb)/2:
                print(xc, yc)
                found = True
                break
        if found:
            break
    if not found:
        print(-1, -1)
