from os import system
from math import factorial
system("cls")
'''
Условие:
Из колоды в 52 карты извлекаются случайным образом 4 карты.
    a) Найти вероятность того, что все карты – крести.
    б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
'''

# Формула подсчета количества сочетаний по k элементов из множества n
#    C(nk) = n!/(k!*(n - k)!)


def f_combination(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


'''
a)  P(A)=m/n - общее количество исходов определяется кол-ом сочетаний из 52 возможных 4 карты , 
    а количество благоприятных исходов - из 13 возможных 4 крести .
'''


m = f_combination(13, 4)  # m = из "13" "4"
n = f_combination(52, 4)  # n = из "52" "4"
P = m / n
print('a) Найти вероятность того, что все карты – крести:')
print(
    f'\nKоличество благоприятных исходов - 4 карты крести из 13 возможных = {int(m)}')
print(f'Общее количество исходов 4 карты из 52 = {int(n)}')
print(
    f'\n<<< Вероятность того, что все карты – крести = {round(P*100,3)}% >>>')

'''
б)  Вероятность, что из 4х карт достанем хотябы одного туза, а может туза и не оказаться: 
    Р(А)+Р(-А)=1 сумма вероятностей противоположных событий равна 1.
    Вероятность, что тузов не окажется совсем - это сочетание из 48 карт (без тузов) 4 карты.
    P(A)=m/n - общее количество исходов определяется кол-ом сочетаний из 52 возможных 4 карты.
'''

m = f_combination(48, 4)  # m = из "48" "4"
n = f_combination(52, 4)  # n = из "52" "4"

P = 1-m / n  # Р(А)=1-Р(-А)
print("\n" + "=" * 70)
print('\nб) Найти вероятность, что среди 4-х карт окажется хотя бы один туз:')
print(
    f'\nKоличество способов извлечь 4 карты из колоды без тузов = {int(m)}')
print(f'Общее количество исходов 4 карты из 52 = {int(n)}')
print(
    f'\n<<< Вероятность извлеч одного или больше тузов = {round(P*100,3)}% >>>')
