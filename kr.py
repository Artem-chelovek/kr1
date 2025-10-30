"""
Блочная(корзинная сортировка)
"""
def insertion_sort(bucket):
    """Используется для сортировки отдельного бака."""
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    """Основная функция блочной сортировки."""
    if not arr or len(arr) <= 1:
        return arr
    
    # Определим максимальный и минимальный элементы
    max_value = max(arr)
    min_value = min(arr)
    
    # Число баков и ширина диапазона для каждого бака
    bucket_count = len(arr)
    bucket_size = (max_value - min_value) / bucket_count
    
    # Создание пустых баков
    buckets = [[] for _ in range(bucket_count)]
    
    # Распределение элементов по бакам
    for value in arr:
        # Выбираем правильный бак для каждого элемента
        index = int((value - min_value) // bucket_size)
        if index != bucket_count:
            buckets[index].append(value)
        else:
            buckets[-1].append(value)  # крайний случай, последний элемент попадает в последний бак
    
    # Сортировка каждого бака
    final_result = []
    for bucket in buckets:
        final_result.extend(insertion_sort(bucket))
    
    return final_result

# Тестирование
numbers = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)
"""
Вывод:

[0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
"""



"""
Блинная сортировка
"""
def flip(arr, k):
    """Перевернуть первые k элементов массива"""
    left = 0
    right = k - 1
    while left < right:
        # Меняем местами левый и правый элементы
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def pancake_sort(arr):
    """Осуществляет блинную сортировку массива"""
    current_size = len(arr)
    
    # Продолжаем сортировку, пока не останется один элемент
    while current_size > 1:
        # Находим индекс наибольшего элемента в текущей несортированной части
        max_index = arr.index(max(arr[:current_size]))
        
        # Если максимум уже на вершине, перевернем всю текущую часть массива
        if max_index != current_size - 1:
            # Переворот верхней части массива, чтобы максимум попал на вершину
            flip(arr, max_index + 1)
            
            # Теперь переворачиваем всю текущую часть массива, чтобы максимум опустился вниз
            flip(arr, current_size)
        
        # Уменьшаем размер несортированной части
        current_size -= 1
    
    return arr

# Пример использования
arr = [3, 6, 2, 4, 5, 1]
pancake_sorted_arr = pancake_sort(arr)
print(pancake_sorted_arr)

"""
Вывод:

[1, 2, 3, 4, 5, 6]
"""

"""

"""