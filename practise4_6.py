import itertools
print('Итеретор, генерирующий целые числа, начиная с 3. При достижении числа 10 - завершаем цикл.')
for el in itertools.count(3):
    print(el)
    if el == 10:
        break

print('Итеретор, повторяющий элементы некоторого списка. При повторении всех элементов по 3 раза - завершаем цикл')
counter = 0
for element in itertools.cycle(['mama', 'papa', 'son']):
    print(element)
    counter += 1
    if counter == 9:
        break
