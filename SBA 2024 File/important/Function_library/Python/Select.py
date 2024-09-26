import os
import re
from important.Function_library.Python.e123 import e
def S(languageCorr1):
     banner = False
     global languageCorr
     global Select
     global FileHi
     languageCorr = languageCorr1
     with open("..\\SBA 2024 File\\important\\language\\language" + str(languageCorr[0]).strip()+ ".txt", "r", encoding="utf-8") as language:
          Select = (language.readlines())
     while banner == False:  
          File_Name = str(input(Select[2]))
          if File_Name[0] != '"':
               File_Name = '"' + File_Name
          File_Name = File_Name.split('"')
          banner = True
          if os.path.splitext(File_Name[1])[1] == ".txt":
               try:
                    with open(File_Name[1], "r", encoding="utf-8") as a:
                         FileHi = a.read()
                    banner = True
                    File = FileHi.lower()
                    SelectFunction(File)
               except IOError:
                    print(Select[3])
                    c = input(Select[5])
          else:
            print(Select[4])
            c = input(Select[5])
def SelectFunction(FH):
     g = 0
     k = [0] * 26
     if languageCorr[3] == "1":
          from important.Function_library.Python.Shift_Cipher_Decoder import SCD
     OnlyWord = re.split('\W+', FH)
     if len(OnlyWord) - 1 >= 200:
          print(Select[14])
          c = input(Select[5])
          if languageCorr[3] == "1":
               number1 = SCD(OnlyWord)
     number = e(FH)
     for i in range(0,26):
          k[i] = 101 - ord(number[i][1])
          if k[i] < 0:
               k[i] + 26
     for i in range(0,6):
          print(str(i) + ", K: " + str(k[i] + 26))
     L = k[0]
     c = input(Select[15])
     if c == "A":
          for i in range(0,len(k)):
               print(str(i) + ", K: " + str(k[i] +26))
          f = input(str(Select[16]))
          for i in range(1,27):
               if f == str(i):
                    L = int(i)
                    g = 3
          if g != 3:
               C = input(Select[17])
     saveFile(L)
     if languageCorr[3] == "1":
          number1 = SCD(OnlyWord)
          saveFile(number1)
def saveFile(number):
     abc = False
     SF = ""
     F = ""
     for i in range(0,len(FileHi)):
          if "A" <= FileHi[i] <= "Z":
               SF = chr(ord(FileHi[i]) + number)
               if SF < "A":
                    SF = chr(ord(SF) + 26)
               if SF > "Z":
                    SF = chr(ord(SF) - 26)
               F += SF
          elif "a" <= FileHi <= "z":
               SF = chr(ord(FileHi[i]) + number)
               if SF < "a":
                    SF = chr(ord(SF) + 26)
               if SF > "z":
                    SF = chr(ord(SF) - 26)
               F += SF
          else:
               F += FileHi[i]
     if languageCorr[4] == "0":
          if len(F) >= 300:
               for i in range(0,300):
                    print(F[i], end = "")
          else:
               print(F)
          print()
          print(Select[6])
          c = input(Select[7])
          check(c, F)
     elif languageCorr[4] == "1":
          print(Select[6])
          c = input(Select[7])
          check(c, F)
     elif languageCorr[4] == "2":
          print(F)
          c = input(Select[7])
          while abc == False:
               if c == "S":
                    abc = True
                    save(F)
def check(c, F):
     abc = False
     while abc == False:
          if c == "Y":
               space()
               print(F)
               abc = True
               c = input(Select[5])
               save(F)
          elif c == "S":
               abc = True
               save(F)
          c = input()
def save(txt):
     go = [""]*7
     space()
     a = False
     while a == False:
          c = input(Select[8])
          if c == "Y":
               path = input(Select[9])
               Hi = os.path.exists(path)
               if Hi == False:
                    try:
                         with open(path, "w", encoding="utf-8") as Hello:
                              Hello.write(txt)
                         with open("..\\SBA 2024 File\\important\\path\\path.txt", "a", encoding="utf-8") as Jack:
                              Jack.write(path)
                         a = True
                    except FileNotFoundError:
                         print(Select[13])
               else:
                    g = input(Select[11])
          if c == "N":
               A = True
               print(Select[11])
               with open("..\\SBA 2024 File\\Output_File\\" + str(int(languageCorr[5]) + 1) +".txt", "w", encoding="utf-8") as age:
                    age.write(txt)
               with open("..\\SBA 2024 File\\important\\path\\path.txt", "a", encoding="utf-8") as Jack:
                    Jack.write("..\\SBA 2024 File\\Output_File\\" + str(int(languageCorr[5]) + 1))
               d = int(languageCorr[5]) + 1
               languageCorr[5] = str(d)
               print(Select[12] + str(languageCorr[5]))
               with open("..\\SBA 2024 File\\important\\file_run\\settings.txt", "w", encoding="utf-8") as settings:
                    for i in range(0,len(languageCorr)):
                         go[i] = languageCorr[i] + "\n"
                    settings.writelines(go)
               c = input(Select[5])
               a = True
def space():
    print()
    os.system('cls')
if __name__ == '__main__':
     print("請打開Main.py")