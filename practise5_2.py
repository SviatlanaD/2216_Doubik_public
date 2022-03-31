"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк
выполнить подсчёт строк
и слов в каждой строке

"""

doc = 'my_text(1).txt'
my_file = open(doc, 'r')
with my_file as f:
    str_doc = sum(1 for line in f)
print(f'Количеcтво строк в документе {doc} - {str_doc}')
my_file.close()

my_file = open(doc, 'r')
my_file_1 = my_file.read()
word_doc = my_file_1.split()
print(f'Общее количество слов {doc} - {len(word_doc)}')
my_file.close()
