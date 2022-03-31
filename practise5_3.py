"""
Создать текстовый файл (не программно)
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк)
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
 # Иванов 23543.12
 # Петров 13749.32
"""
my_file = open('my_text_5_3.txt', encoding='utf-8')
with my_file as f:
    aver_salary = 0
    my_file_list = f.readlines()
    for line in my_file_list:
        surname, salary = line.split()
        aver_salary += float(salary)
        if float(salary) < 20000:
            print(f'Sotrudnik {surname} imeet zarplatu menshe 20000')
    aver_salary = aver_salary / len(my_file_list)
    print(f'Srednyay zarplata sostavlyaet {aver_salary}')
my_file.close()
