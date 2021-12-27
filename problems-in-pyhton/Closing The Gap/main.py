num_of_buildings = []
buildings = []
num = input()
for i in range(int(num)):
    num_of_buildings.append(int(input()))
    buildings.append([int(e) for e in input().split(' ')])

for i in range(int(num)):
    if sum(buildings[i]) % num_of_buildings[i] == 0:
        print(0)
    else:
        print(1)
