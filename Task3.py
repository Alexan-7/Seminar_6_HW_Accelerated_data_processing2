'''
Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11
'''

def summa_float(numf):
    return sum(map(int, numf.replace('.','').replace(',','').replace('-','')))

numf = input('Введите вещественное число: ')
print(f'Сумма цифр в числе: {summa_float(numf)}')