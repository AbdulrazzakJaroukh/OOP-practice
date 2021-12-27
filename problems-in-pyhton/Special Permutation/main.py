in_data = []
num = input()
for i in range(int(num)):
    in_data.append([int(e) for e in input().split(' ')])

for i in range(int(num)):
    result = [e for e in range(1, in_data[i][0] + 1) if e != in_data[i][2] and e != in_data[i][1]]
    result.reverse()
    result.append(in_data[i][2])
    result = [in_data[i][1]] + result
    if in_data[i][1] == min(result[0:in_data[i][0]//2]) and in_data[i][2] == max(result[in_data[i][0]//2:in_data[i][0]]):
        print(" ".join([str(e) for e in result]))
    else:
        print(-1)
