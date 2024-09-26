def QS():
        with open("..\\SBA 2024 File\important\words\ALL_words.txt", "r", encoding="utf-8") as settings:
                list = (settings.read())
        print(list)
        quick_sort = lambda list: list if len(list) <= 1 else quick_sort([Hi for Hi in list[1:] if Hi <= list[0]]) + [list[0]] + quick_sort([Hi for Hi in list[1:] if Hi > list[0]])
        with open("..\\SBA 2024 File\important\words\ALL_words.txt", "w", encoding="utf-8") as settings:
                settings.write(list)
if __name__ == '__main__':
     QS()
