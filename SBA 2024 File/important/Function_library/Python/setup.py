import os
def setup():
    T = False
    with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "r", encoding="utf-8") as setting:
        setupnum = (setting.readlines())
        if setupnum[2] == "0\n":
            with open("..\\SBA 2024 File\\important\\menu\\setupPH.txt", "r", encoding="utf-8") as PH:
                setupPH= PH.read()
            print(setupPH)
            while T == False:
                put = input()
                if put == "":
                    T = True
                    space1()
                    with open("..\\SBA 2024 File\\important\\menu\\menu0.txt", "r", encoding="utf-8") as lan:
                        language = lan.read()
                    print(language)
                    with open("..\\SBA 2024 File\\important\\language\\language1.txt", "r", encoding="utf-8") as language:
                        lang = language.readlines()
                    languageChange_language = input(lang[1])
                    if languageChange_language.isdigit() == True and int(languageChange_language) <= int(setupnum[1]) and int(languageChange_language) > 0:
                        setupnum[0] = str(languageChange_language) + "\n"
                        setupnum[2] = str(1) + "\n"
                        with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "w", encoding="utf-8") as age:
                            for i in range(0,len(setupnum)):
                                age.write(setupnum[i])
def space1():
    print()
    os.system('cls')
if __name__ == '__main__':
     print("請打開Main.py")