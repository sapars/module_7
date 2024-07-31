
def custom_write(file_name, string_list):
    file_pos, string_num = 0, 0
    string_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in string_list:
            file_pos = file.tell()
            string_num += 1
            string_positions[(string_num, file_pos)] = string
            file.write(string + '\n')
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)