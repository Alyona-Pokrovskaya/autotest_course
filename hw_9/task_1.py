# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


f1 = open('test_file/task1_data.txt', mode='r', encoding='utf-8')

string = ''
for one_lines in f1.readlines():
    for char in one_lines:
        if not char.isdigit():
            string = string + char

f2 = open('test_file/task1_answer.txt', mode='w', encoding='utf-8')
f2.write(string)
f2.close()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
