import time, random
from functools import wraps
import sys

sys.setrecursionlimit(3000)

"""Ввиду большой схожести по сложности популярных алгоритмов сортировки:
у всех самых быстрых временная сложность О(N*logN) мой подход будет основан на статистике
и аналитике. Ниже проведены испытания трёх конкурирующих алгоритмов, а именно:
Быстрая соритровка, Сортировка слиянием, Сортировка кучей
Всего я проведу по 10 испытаний для случайных 
списков и 2 испытания для отсоритрованного и частично отсортированного списков соответственно"""

def heapify(arr, n, i):
    """Преобразует поддерево с корнем в узле i в кучу."""
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый дочерний узел
    right = 2 * i + 2  # Правый дочерний узел

    # Если левый дочерний узел больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний узел больше наибольшего элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно преобразуем затронутое поддерево в кучу
        heapify(arr, n, largest)

def heap_sort(arr):
    """Сортировка массива с помощью кучи и возврат нового отсортированного массива."""
    n = len(arr)
    # Создаем копию исходного массива для сортировки
    arr_copy = arr.copy()

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]  # Перемещаем текущий корень в конец
        heapify(arr_copy, i, 0)  # Вызываем heapify на уменьшенной куче

    return arr_copy  # Возвращаем отсортированный массив

def merge(left, right):
    """Сливает два отсортированных массива в один отсортированный."""
    sorted_array = []
    i = j = 0

    # Сравниваем элементы из обоих массивов и добавляем меньший в результирующий массив
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левой половины
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правой половины
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

def merge_sort(arr):
    """Сортирует массив с помощью сортировки слиянием и возвращает новый отсортированный массив."""
    if len(arr) <= 1:
        return arr  # Если массив пустой или содержит один элемент, он уже отсортирован

    mid = len(arr) // 2  # Находим середину массива
    left_half = merge_sort(arr[:mid])  # Рекурсивно сортируем левую половину
    right_half = merge_sort(arr[mid:])  # Рекурсивно сортируем правую половину

    return merge(left_half, right_half)  # Сливаем и возвращаем отсортированный массив

def quick_sort(arr):
    """Сортирует массив с помощью быстрой сортировки и возвращает новый отсортированный массив."""
    if len(arr) <= 1:
        return arr  # Если массив пустой или содержит один элемент, он уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (средний элемент)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного

    # Рекурсивно сортируем и объединяем
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    quick_sort_time = 0
    merge_sort_time = 0
    heap_sort_time = 0

    for i in range(20):
        arr = [random.randint(0, 10000) for _ in range(500000)]
        start_time = time.time()
        quick_sort(arr)
        end_time = time.time()
        quick_sort_time += end_time - start_time
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        merge_sort_time += end_time - start_time
        start_time = time.time()
        heap_sort(arr)
        end_time = time.time()
        heap_sort_time += end_time - start_time

    quick_sort_time_avg = quick_sort_time / 10
    merge_sort_time_avg = merge_sort_time / 10
    heap_sort_time_avg = heap_sort_time / 10

    print(f"Среднее время Быстрой сортировки {quick_sort_time_avg:.6f} секунд.")
    print(f"Среднее время Сортировки слиянием {merge_sort_time_avg:.6f} секунд.")
    print(f"Среднее время Сортировки кучей {heap_sort_time_avg:.6f} секунд.")

    '''Проведя первый тест несколько раз(параметры системы приложу ниже) я выяснил, что 
    самой быстрой оказалась, как бы тавтологично ни звучало, быстрая сортировка, выдающая
    в среднем 1 секунду времени, на втором месте сортировка слиянием 1,8 сек., на третьем кучей 3 сек.
    Каждый прогон являет собой выборку из 20 случайно сгенерированных списков, длиной 500000 каждый,
    числа не умаляя общности используются целые. Посмотрим на случай частично отсортированных и отсортированных массивов'''

    arr = [i for i in range(1000000)]
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    quick_sort_time = end_time - start_time
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    merge_sort_time = end_time - start_time
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    heap_sort_time = end_time - start_time

    print(f"Время Быстрой сортировки для отсортированного массива {quick_sort_time:.6f} секунд.")
    print(f"Время Сортировки слиянием для отсортированного массива {merge_sort_time:.6f} секунд.")
    print(f"Время Сортировки кучей для отсортированного массива {heap_sort_time:.6f} секунд.")

    '''В этом случае наблюдается прирост скорости порядка 20% у соритровки слиянием, 
    незначительный прирост у Быстрой сортировки и то же время осталось у сортировки кучейц.
    Рассмотрим сортировку частично упорядоченных списков'''

    arr = [i for i in range(333333, 666666)] + [i for i in range(333333)] + [i for i in range(666666, 1000000)]
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    quick_sort_time = end_time - start_time
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    merge_sort_time = end_time - start_time
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    heap_sort_time = end_time - start_time

    print(f"Время Быстрой сортировки для частично отсортированного массива {quick_sort_time:.6f} секунд.")
    print(f"Время Сортировки слиянием для частично отсортированного массива {merge_sort_time:.6f} секунд.")
    print(f"Время Сортировки кучей для частично отсортированного массива {heap_sort_time:.6f} секунд.")

    '''Последний тест показывает неутешительные результаты... Быстрая сортировка сдаёт позиции,
    конечно это было ожидаемо, во многих источниках пишется о нестабильной работе с частично отсортирванными 
    списками. Выводы сделаны в файле SortingAlgorithm.'''