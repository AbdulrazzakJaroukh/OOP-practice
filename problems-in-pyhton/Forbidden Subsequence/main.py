ss = []
num = input()
for i in range(2*int(num)):
    ss.append(input())

letters = ['a', 'b', 'c']
substr = []
for a in letters:
    for b in letters:
        for c in letters:
            substr.append(a+b+c)

for i in range(len(ss)):
    if not ss[i+1] in ss[i]:
        print(''.join(sorted(ss[i])))
        i += 1
    else:
        index = ss[i].find(ss[i+1])
        element = ''.join(sorted(ss[i]))
        setstr = set(element)
        for sub in substr:
            element[index:index+2] = sub
            if setstr == set(element):
                print(element)
                i += 1
                break