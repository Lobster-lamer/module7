"""
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.
"""
import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        if os.path.isfile(r"%s" % os.path.join(root, file)):
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath},'
                  f' Размер: {filesize} байт, Время изменения: {formatted_time},'
                  f' Родительская директория: {parent_dir}')


# Не видит файлы кроме как в корне!