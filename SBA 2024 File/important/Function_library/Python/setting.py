def set(Sett):
    go = [""] * 6
    with open("..\\SBA 2024 File\\important\\setmenu\\" + Sett[0] + ".txt", "r", encoding="utf-8") as menu1:
        setmenu1 = (menu1.read())
    print(setmenu1)
    a = False
    while a == False:
        c = str(input())
        if c == "1" or c == "2" or c == "3":
            if c == "1":
                with open("..\\SBA 2024 File\\important\\set2menu\\" + Sett[1] + ".txt", "r", encoding="utf-8") as menu2:
                    setmenu2 = (menu2.read())
                print(setmenu2)
                sel = str(input())
                if sel == "1" or sel == "2" or sel == "3":
                    word = sel
            elif c == "2":
                with open("..\\SBA 2024 File\\important\\set3menu\\" + Sett[1] + ".txt", "r", encoding="utf-8") as menu3:
                    setmenu3 = (menu3.read())
                    print(setmenu3)
                    sel = str(input())
                    if sel == "1" or sel == "2":
                        if sel == "1":
                            pas = str(input("Passwords: "))
                            if pas == "20240906":
                                more = 1
                            else:
                                print("password is incorrect")
                                d = input("<<<Press any key to continue>>>")
                        elif sel == "2":
                            more = 0
            elif c == "3":
                Sett[0] = str(1)
                Sett[1] = str(3)
                Sett[2] = str(0)
                word = 0
                more = 0
                Sett[5] = str(0)
                with open("..\\SBA 2024 File\\important\\path\\path.txt", "w", encoding="utf-8") as Del:
                    Del.write("")
                a = True
    Sett[3] = str(word)
    Sett[4] = str(more)
    with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "w", encoding="utf-8") as settings:
        for i in range(0,len(Sett)):
            go[i] = Sett[i] + "\n"
        settings.writelines(go)
if __name__ == '__main__':
     print("請打開Main.py")