# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов 
# внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся 
# буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os

def group_rename(new_name, digits, extension, final_ext, range_name, path):
    counter = 1
    for file in os.listdir(path):
        if file.endswith(extension):
            old_name = os.path.splitext(file)[0]
            letters_range = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f'{letters_range}{new_name}{str(counter).zfill(digits)}{final_ext}'
            os.rename(os.path.join(path, file), os.path.join(path, new_filename))
            counter += 1


group_rename('newest', 2, '.py', '.ktk', [3, 6], r'C:\Users\Misha\Python2\HW\HW7\New_dir')


