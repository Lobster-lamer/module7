import os


def custom_write(file_name: str, strings: list) -> dict[tuple[str, int]: str]:
    if os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as test_text_file:
            string_positions = {}
            for string_number in range(len(strings)):
                test_text_file.write(strings[string_number] + "\n")
                file_tell = test_text_file.tell()
                string_number_n_start = [((string_number, file_tell), strings[string_number])]
                string_positions.update(dict(string_number_n_start))
            return string_positions
    else:
        print("Файла не существует")
        return


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
