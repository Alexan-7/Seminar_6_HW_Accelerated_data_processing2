'''
2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
'''

list1 = [12,'sadf', 5643, 'FoFi', 5, 'LSF', 21]
list2 = []

list2 = list(filter(lambda x: type(x) == int, list1))
list3 = list(filter(lambda x: type(x) == str, list1))

print(f'Первоначальный список: {list1}\nЧисла в списке: {list2}\nБуквы в списке: {list3}')