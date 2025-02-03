from collections import deque

class CircularBuffer1:
    """Класс, описывающий циклический буффер и функции pop и push на основе списка"""
    
    def __init__(self, size: int=5):
        self.size = size
        self.buffer = [''] * size
        self.push_pointer = 0
        self.pop_pointer = 0

    def push(self, number: int):
        """ФУнкция для добавления элемента в циклический буффер"""
        # Проверяем крайний случай если размер буффера задан нулевым
        if self.size == 0:
            raise IndexError('The buffer length is ZERO!(')
        # Добавляем элемент в буффер, указатель на место добавления берём по моудлю из-за цикличности
        else:
            # Если указатель на push "догнал" указатель на pop, то смещаем указатель на pop на единицу
            if self.buffer[self.push_pointer] != '':
                self.pop_pointer = self.push_pointer + 1
            self.buffer[self.push_pointer] = number
            self.push_pointer = (self.push_pointer + 1) % self.size

    def pop(self) -> int:
        """ФУнкция для удаления элемента из циклического буффера"""
        # Проверяем крайний случай если размер буффера задан нулевым
        if self.size == 0:
            raise IndexError('The buffer length is ZERO!(')
        # Достаём элементпо указателю на pop
        element = self.buffer[self.pop_pointer]
        # Проверяем крайний случай - есди в буфере не осталось элементов
        if element == '':
            raise IndexError('The buffer is empty(')
        # Если проверка прошла, то нужны нам элемент лежит в element, вернём его и изменим указатель на pop
        else:
            self.buffer[self.pop_pointer] = ''
            self.pop_pointer = (self.pop_pointer + 1) % self.size
            return element

class CircularBuffer2:
    """Класс, описывающий циклический буффер и функции pop и push на основе deque"""

    def __init__(self, size: int=5):
        self.size = size
        self.buffer = deque(maxlen=size)

    def push(self, number: int):
        """ФУнкция для добавления элемента в циклический буффер"""
        # Делаем проверку по size т.к. длина dequea может быть равна нулю даже при ненулевой максимальной длине
        # Проверяем крайний случай если размер буффера задан нулевым
        if self.size == 0:
            raise IndexError('The buffer length is ZERO!(')
        self.buffer.append(number)

    def pop(self) -> int:
        """ФУнкция для удаления элемента из циклического буффера"""
        # Аналогично роверяем крайний случай если размер буффера задан нулевым
        if self.size == 0:
            raise IndexError('The buffer length is ZERO!(')
        # Делаем проверку на пустоту буффера (если все элементы вытащили)
        elif len(self.buffer) == 0:
            raise IndexError('The buffer is empty!(')
        else:
            return self.buffer.popleft()
        
"""
Анализируя варианты реализации я пришёл к таким выводам: Временная сложность работы у обоих реализаций будет одинакова
если судить по ассимтотическим приближениям (О(1) на добавление и удаление элементов по документации Python), однако очевидно
при ооооочень больших индексах операция сложения при рассчёте новых значений индексов в первой реализации будет занимать время.
Нивелируется этот недостаток возможностью модернизировать класс и получать доступ к элементам по индексам (это же и враг списочной
реализации - она занимает всегда >= const * n места, а дек хранит только записанные в него элементы).
"""

if __name__ == "__main__":
    # Вариант использования
    
    buffer_list = CircularBuffer1()
    buffer_deque = CircularBuffer2()

    for i in range(12):
        buffer_list.push(i)
        buffer_deque.push(i)
    
    for i in range(7):
        try:
            print(f'{buffer_list.pop()} - {i}-й элемент списочной реализации')
        except IndexError:
            print('Проверка исключения записи')

    for i in range(7):
        try:
            print(f'{buffer_deque.pop()} - {i}-й элемент списочной реализации')
        except IndexError:
            print('Проверка исключения записи')