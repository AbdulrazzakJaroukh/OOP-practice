ss = []
num = input()
for i in range(int(num)):
    ss.append(input())

count = 0
qualified = []
teams_dict = {}
result = []
for item in ss:
    uni, team = item.split(' ')
    if uni not in teams_dict:
        teams_dict[uni] = 1
    else:
        teams_dict[uni] += 1
    if teams_dict[uni] <= 4 and uni == 'MSU' and uni != 'SCH':
        result.append(uni+' '+team)
        count += 1
    elif teams_dict[uni] <= 2 and uni != 'SCH':
        result.append(uni+' '+team)
        count += 1
    if count == 10:
        break

print(count)
for res in result:
    print(res)

