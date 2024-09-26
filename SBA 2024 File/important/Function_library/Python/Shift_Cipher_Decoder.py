import os
def SCD(OnlyWord):
    global OW
    OW = OnlyWord
    with open("..\\SBA 2024 File\\important\\words\\SIM_words.txt", "r", encoding="utf-8") as SW:
        sim = (SW.readlines())
        sim = sorted(sim)
    for i in range(0,len(sim)):
        sim[i] = sim[i].split()
    number = run(sim)
    if number != False:
        return number
    with open("..\\SBA 2024 File\\important\\words\\ALL_words.txt", "r", encoding="utf-8") as AW:
        all = (AW.readlines())
        all = sorted(all)
    for i in range(0,len(all)):
        all[i] = all[i].split()
        sorted(all)
    number = run(all)
    if number != False:
        return number
    return number
def run(words):
    count = 0
    Fcount = 0
    cy = 0
    a = 0
    midlist = [] * len(OW)
    found = False
    for i in range(0, len(OW)):
        OW1 = ""
        OW2 = ""
        for j in range(0,len(OW[i])):
            OW1 = chr(ord(OW[i][j]) + cy)
            if (ord(OW1) - 97) % 25 > 0:
                OW1 = chr(((ord(OW1) - 97) % 25) + 97)
            OW2 += OW1
        while a < len(words) and not(found):
            first = 0
            last = len(words) - 1
            while not(found) and first <= last:
                mid = int((first + last) / 2)
                if OW2 == words[mid]:
                    found = True
                else:
                    if OW2 < words[mid][0]:
                        a = mid + 1
                    else:
                        last = mid - 1
        if found == True:
            count += 1
            midlist[count] = j
        elif found == False:
            Fcount += 1
    if count < Fcount:
        return False
    elif count > Fcount:
        sorted(midlist, reverse=True)
        a = 0
        b = 0
        for i in range(0,len(midlist)):
            if midlist[i] == midlist[0]:
                a += 1
            else:
                b += 1
    if a > b:
        return a
if __name__ == '__main__':
     print("請打開Main.py")