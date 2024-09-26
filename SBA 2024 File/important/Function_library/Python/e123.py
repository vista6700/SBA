def e(Fi):
    pt = [0] * 26
    for i in range(0, 26):
        pt[i] = [0, chr(i + 97)]
    for i in range(len(Fi)):
        if Fi[i] >= "a" and Fi[i] <= "z":
            pt[ord(Fi[i]) - 97][0] += 1
    return(sorted(pt, reverse=True))
if __name__ == '__main__':
     print("請打開Main.py")