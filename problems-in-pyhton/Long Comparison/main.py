in_data = []
num = input()
for i in range(int(num)):
    in_data.append([])
    in_data[i].append(input())
    in_data[i].append(input())


for i in range(int(num)):
    first = [int(e) for e in in_data[i][0].split(' ')]
    second = [int(e) for e in in_data[i][1].split(' ')]
    power1 = len(str(first[0])) - 1
    full_power1 = power1 + first[1]
    result_1 = first[0] / 10 ** power1

    power2 = len(str(second[0])) - 1
    full_power2 = power2 + second[1]
    result_2 = second[0] / 10 ** power2

    if full_power1 > full_power2:
        print('>')
    elif full_power1 < full_power2:
        print('<')
    elif result_1 > result_2:
        print('>')
    elif result_1 < result_2:
        print('<')
    else:
        print('=')
