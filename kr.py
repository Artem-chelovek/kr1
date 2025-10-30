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

"""
