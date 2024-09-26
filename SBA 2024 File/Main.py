import os
import random
from important.Function_library.Python.setup import setup
from important.Function_library.Python.Select import S
from important.Function_library.Python.setting import set
def Drop_databases(Corr):
    space()
    with open("..\\SBA 2024 File\\important\\menu\\menu" + str(Corr).strip() + ".txt", "r", encoding="utf-8") as menu:
        print(menu.read(),end = "")
def Change_language():
    space()
    Drop_databases(0)
    print()
    while SelectFile == False:
        languageChange_language = input(Select[1])
        if languageChange_language.isdigit() == True and int(languageChange_language) <= int(languageCorr[1]) and int(languageChange_language) > 0:
            with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "r+", encoding="utf-8") as language:
                language.write(languageChange_language)
            return
def space():
    print()
    os.system('cls')
def in_put():
    choice = input()
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        choice = input("pls re Enter your choice: ")
    space()
    return choice
def File():
    with open("..\\SBA 2024 File\\important\\path\\path", "r", encoding="utf-8") as a:
        print(a.readlines())
        c = input(Select[5])
pycheck = os.path.exists("..\\SBA 2024 File\\important\\Function_library\\Python\\Check_Path.py")
if pycheck == True:
    from important.Function_library.Python.Check_Path import check
    check()
else:
    t = False
    while t == False:
        y = input("缺失(SBA 2024 File/important/Function_library/Python/Check_Path.py),無法檢查檔案的完整性，一旦有檔案遺失，可能會運行時錯誤,請重新下載完整檔案,如要繼續運行請輸入大楷(Y)以繼續")
        if y == "Y":
            t = True
setup()
SelectFile = False#0 = False, 1 = True
while SelectFile == False:
    with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "r", encoding="utf-8") as settings:
        languageCorr = (settings.readlines())
    with open("..\\SBA 2024 File\\important\\language\\language" + str(languageCorr[0]).strip() + ".txt", "r", encoding="utf-8") as language:
        Select = (language.readlines())
    Drop_databases(languageCorr[0])
    for i in range(0,len(languageCorr)):
        languageCorr[i] = languageCorr[i].strip()
    N = in_put()
    match N:
        case "5":
            set(languageCorr)
        case "4":
            SelectFile = True
            with open("..\\SBA 2024 File\\important\\language\\bye.txt", "r", encoding="utf-8") as BYE:
                bye = (BYE.readlines())
            print(bye[random.randint(0, (len(bye) - 1))])
        case "3":
            Change_language()
        case "2":
            File()
        case "1":
            S(languageCorr)