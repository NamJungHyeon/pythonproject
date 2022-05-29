def getScore(arr, diceInfo):
    score = 0
    for i in range(10):
        nowLoc = diceInfo[arr[i]]
        nowCnt = sequence[i]
        # flag = False
        for c in range(nowCnt):
            if nowLoc == 32:  # 마지막 도착
                # flag = True
                break
            if len(diceMap[nowLoc]) == 2 and c == 0:
                look = 1
            else:
                look = 0
            nowLoc = diceMap[nowLoc][look]

        if nowLoc != 32 and visited[nowLoc]:
            return 0
        # if not flag:
        score += diceScore[nowLoc]
        visited[diceInfo[arr[i]]] = False
        diceInfo[arr[i]] = nowLoc
        visited[diceInfo[arr[i]]] = True

    return score


def makePermutation(now, goal, arr):
    global maxScore
    global visited

    if now == goal:
        diceInfo = [0, 0, 0, 0]
        visited = [False for _ in range(33)]
        maxScore = max(maxScore, getScore(arr, diceInfo))
        return

    for i in range(4):
        arr[now] = i
        makePermutation(now + 1, goal, arr)


diceMap = [[] for _ in range(32)]
diceScore = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
visited = [False for _ in range(33)]
sequence = [int(x) for x in input().split()]
maxScore = 0

for i in range(20):
    diceMap[i].append(i + 1)

diceMap[5].append(21)
diceMap[21].append(22)
diceMap[22].append(23)
diceMap[23].append(29)
diceMap[10].append(24)
diceMap[24].append(25)
diceMap[25].append(29)
diceMap[15].append(26)
diceMap[26].append(27)
diceMap[27].append(28)
diceMap[28].append(29)
diceMap[29].append(30)
diceMap[30].append(31)
diceMap[31].append(20)
diceMap[20].append(32)

makePermutation(0, 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(maxScore)