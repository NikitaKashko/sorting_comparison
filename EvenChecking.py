import random
def isEven(value):
    return bin(value)[-1] == '0'

'''Суть работы функции если копать глубоко схожа со сравнением остатка от деления на 2
Но на высоком уровне мы совершаем разные действия: 
сравниваем именно остаток от деления при делении с остатком, 
и проверяем крайний бит в этой реализации. Преимуществом этой реализации будет отсутствие 
арифметических действий над числом. Однако есть и недостаток - временная сложность 
появляется во внутрянке функции bin - O(log(N)), и необходимость выделения памяти не 
только под число, но и под его двоичное представление. Я нашел разные сведения касательно 
сложности функции bin(), но считаю что она все таки не константная, ведь предела на хранимое число 
с 3 версии Python если не ошибаюсь нет.'''
