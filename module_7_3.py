import os
import re
from consoleTextStyle import ConsoleTextStyle as CoTeSt


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            if os.path.exists(file):
                with open(file, "r", encoding="utf-8") as _file:
                    read_file = _file.read()
                    _words = re.split("|".join([',', '\.', '=', '\!', '\?', ';', ':', ' - ', ' ', '\n']),
                                      read_file.lower())
                    _words = list(filter("".__ne__, _words))
                    all_words.update(([(file, _words)]))
            else:
                print(f"{CoTeSt.Color.RED}Файла не существует{CoTeSt.REGULAR}")
                continue
        return all_words

    def find(self, word_to_find: str) -> int or None:
        files_words = self.get_all_words()
        for file_name in files_words.keys():
            if word_to_find.lower() in files_words[file_name]:
                return {file_name: files_words[file_name].index(word_to_find.lower())+1}
            else:
                continue
        else:
            print("Такого слова нет в файле")

    def count(self, word_to_find: str):
        files_words = self.get_all_words()
        for file_name in files_words.keys():
            if word_to_find.lower() in files_words[file_name]:
                return {file_name: files_words[file_name].count(word_to_find.lower())}
            else:
                continue
        else:
            print("Такого слова нет в файле")


if __name__ == "__main__":
    files = ("products.txt", "module_7_2_text.txt")
    words = WordsFinder(*files)
    print(words.get_all_words())
    print(words.find("TELL"))
    print(words.count("vegetable"))

    print()

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
