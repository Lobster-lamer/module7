import os
from consoleTextStyle import ConsoleTextStyle as CoTeSt


def custom_write(file_name: str, strings: list) -> dict[tuple[str, int]: str]:
    if os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as test_text_file:
            string_positions = {}
            for string_number in range(len(strings)):
                file_tell = test_text_file.tell()
                test_text_file.write(strings[string_number] + "\n")
                string_number_n_start = [((string_number + 1, file_tell), strings[string_number])]
                string_positions.update(dict(string_number_n_start))
            return string_positions
    else:
        print(f"{CoTeSt.Color.RED}Файла не существует{CoTeSt.REGULAR}")
        return {"Error": "Файла не существует"}


if __name__ == "__main__":
    text_file_name = "module_7_2_text.txt"
    print(custom_write(text_file_name, ["qwe", "er", "ty"]), "\n")
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write(text_file_name, info)
    for elem in result.items():
        print(elem)
