keyboards = []
words = []
num = input()
for i in range(int(num)):
    keyboards.append(input())
    words.append(input())

for i in range(int(num)):
    keyboard = keyboards[i]
    word = words[i]
    summ = 0
    for j in range(len(word) - 1):
        summ += abs(keyboard.index(word[j+1]) - keyboard.index(word[j]))
    print(summ)
