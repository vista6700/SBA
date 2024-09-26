import re
from Shift_Cipher_Decoder import SCD
with open("E:\message1.txt", "r", encoding="utf-8") as settings:
    FileHi = (settings.read())
File = FileHi.lower()
OnlyWord = re.split('\W+', FileHi)
number1 = SCD(OnlyWord)
print(number1)
if __name__ == '__main__':
     print("請打開Main.py")