import random as rd

def reSult(ac):
    yut = ["도", "개", "걸", "윷", "모", "빽도", "낙"]
    ect = ["0", "1", "null"]
    zCount = 0
    oCount = 0
    nCount = 0
    pivo = rd.randint(0, 35)
    i = 0
    while((zCount+oCount+nCount) < 4):
        if ac[i] == ect[0]:
            zCount = zCount + 1
        elif ac[i] == ect[1]:
            oCount += 1
        elif ac[i] == ect[2]:
            nCount += 1
        i = i + 1
        if nCount == 1:
            if oCount != 3:
                zCount += 1
                nCount = 0

    if pivo == 24:
        return yut[6]
    if zCount == 4:
        ops = 3
        return yut[3]
    elif zCount == 3:
        return yut[2]
    elif zCount == 2:
        return yut[1]
    elif oCount >= 3:
        if nCount == 1:
            return yut[5]
        elif zCount == 1:
            return yut[0]
        else:
            return yut[4]

def yutNol():
    y = [ ["0", "1"],["0", "1"],["0", "1"],
    ["0", "1","0", "1","0", "1","0", "1","0", "1","null"] ]
    result = list()
    y1 = list(rd.choice(y[0]))
    y2 = list(rd.choice(y[1]))
    y3 = list(rd.choice(y[2]))
    y4 = list()
    y4.append(rd.choice(y[3]))
    print("{}, {}, {}, {} ".format(y1, y2, y3, y4))
    result = y1 + y2 + y3 + y4
    cam = reSult(result)
    print(cam)
    return cam


def mainloop(tag):
    cam = ["ui"]
    while tag:
        cam = yutNol()
        if (cam == "윷") or (cam == "모"):
            print(" {}! 한번 더 돌립니다.".format(cam))
            cam = yutNol()
            if (cam == "윷") or (cam == "모"):
                print(" {}! 한번 더 돌립니다.".format(cam))
                cam = yutNol()
                if (cam != "윷") or (cam != "모"):
                    break
                else:
                    print("이거 띄우면 죽일거임")
                    yutNol()
                    break
        if (cam == "낙"):
            print(" {}! 다음 기회에(벌레 컷)".format(cam))
        tag = 0
        return cam