a = int(input())
strings = [input() for i in range(a)]
for i in range(0, len(strings)):
    string = []
    num = len(strings[i])
    mid = num / 2
    for j in range(0, num):
        if j % 2 == 0:
            string.append(strings[i][j])
    string.append(" ")
    for j in range(0, num):
        if j % 2 != 0:
            string.append(strings[i][j])

    ans = ''.join(i for i in string)
    print(ans)
