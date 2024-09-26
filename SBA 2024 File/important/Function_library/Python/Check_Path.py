import os.path
def check():
    g = 0
    check = os.path.exists("..\\SBA 2024 File\\important\\file_run\\ALLfile_path.txt")
    if check == True:
        with open("..\\SBA 2024 File\\important\\file_run\\ALLfile_path.txt", "r", encoding="utf-8") as filepath:
            File_Path = filepath.readlines()
            i = len(File_Path)
            for j in range(0,i):
                check = os.path.exists(File_Path[j].strip())
                if check == False:
                    g += 1
                    print(File_Path[j].strip())
                    pathERROR(g)
    else:
        d = "d"
        pathERROR(d)
def pathERROR(c):
    a = "缺失以上檔案，可能會運行時錯誤，請重新下載完整檔案，如要繼續運行請輸入大楷(Y)以繼續，檔案缺失總數: "
    a + str(c)
    if c == "d":
        a =("缺失(..\\SBA 2024 File\\important\\file_run\\ALLfile_path.txt)，無法檢查檔案的完整性，一旦有檔案遺失，可能會運行時錯誤，請重新下載完整檔案，如要繼續運行請輸入大楷(Y)以繼續")
    Boo = False
    while Boo == False:
        y = input(a)
        if y == "Y":
            Boo = True
if __name__ == '__main__':
    print("請開啟Main.py")