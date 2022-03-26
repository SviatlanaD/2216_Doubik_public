my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# не знаю правильно ли это решение. Я отталкивалась от логики:
# что первого числа никогда в списке не будет, так как его не с чем сравнивать
my_list_1 = my_list[1:]
new_list = [el for el in my_list_1 if el > my_list[my_list.index(el)-1]]
print(new_list)

# если предыдущее не верно, вот еще одно:
new_list_1 = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        (new_list_1.append(my_list[i]))
print(new_list_1)
