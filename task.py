import timeit
import random
from typing import List
from statistics import mean
from textwrap import dedent

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Реалізація сортування вставками.
    
    Принцип роботи:
    1. Проходимо по масиву починаючи з другого елементу
    2. Порівнюємо поточний елемент з попередніми
    3. Вставляємо елемент у відповідну позицію
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    """
    Реалізація сортування злиттям.
    
    Принцип роботи:
    1. Рекурсивно розділяємо масив навпіл
    2. Сортуємо кожну половину
    3. Зливаємо відсортовані половини
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Допоміжна функція для злиття двох відсортованих масивів."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr: List[int]) -> List[int]:
    """Використання вбудованого сортування Python (Timsort)."""
    return sorted(arr)

def generate_test_data(size: int, case: str = 'random') -> List[int]:
    """Генерує тестові дані різних типів."""
    if case == 'random':
        return [random.randint(0, 1000000) for _ in range(size)]
    elif case == 'sorted':
        return list(range(size))
    elif case == 'reversed':
        return list(range(size, 0, -1))
    elif case == 'nearly_sorted':
        arr = list(range(size))
        # Вносимо невеликі зміни
        for _ in range(size // 20):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

def measure_time(func, arr: List[int], number: int = 3) -> float:
    """Вимірює час виконання функції сортування."""
    # Створюємо копію масиву для кожного тесту
    test_code = f"func(arr.copy())"
    return timeit.timeit(test_code, globals={'func': func, 'arr': arr}, number=number) / number

def format_results(results: List[dict]) -> str:
    """Форматує результати у вигляді текстової таблиці."""
    # Створюємо заголовок таблиці
    header = f"{'Size':<10} {'Case':<15} {'Algorithm':<15} {'Time (seconds)':<15}"
    separator = "-" * 55
    
    # Форматуємо кожний рядок результатів
    rows = [header, separator]
    for r in results:
        time_str = f"{r['Time']:.6f}" if r['Time'] != float('inf') else "Too long"
        row = f"{r['Size']:<10} {r['Case']:<15} {r['Algorithm']:<15} {time_str:<15}"
        rows.append(row)
    
    return "\n".join(rows)

def main():
    # Визначаємо параметри тестування
    sizes = [100, 1000, 5000, 10000]
    cases = ['random', 'sorted', 'reversed', 'nearly_sorted']
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Timsort': timsort
    }
    
    # Збираємо результати
    results = []
    for size in sizes:
        print(f"\nТестування на розмірі {size}...")
        for case in cases:
            data = generate_test_data(size, case)
            
            for algo_name, algo_func in algorithms.items():
                # Пропускаємо повільні алгоритми на великих масивах
                if algo_name == 'Insertion Sort' and size > 5000:
                    time = float('inf')
                else:
                    time = measure_time(algo_func, data)
                
                results.append({
                    'Size': size,
                    'Case': case,
                    'Algorithm': algo_name,
                    'Time': time
                })
    
    # Виводимо результати
    print("\nРезультати тестування:")
    print(format_results(results))
    
    # Створюємо README.md з результатами та висновками
    readme_content = dedent(f"""
    # Порівняльний аналіз алгоритмів сортування

    ## Методологія
    - Тестування проводилось на розмірах масивів: {sizes}
    - Типи даних: випадкові, відсортовані, зворотньо відсортовані, майже відсортовані
    - Для кожного тесту проводилось {3} вимірювань, результат усереднювався

    ## Результати
    ```
    {format_results(results)}
    ```

    ## Висновки
    1. Timsort показує найкращу загальну продуктивність, особливо на великих масивах
    2. Сортування вставками ефективне на малих масивах та майже відсортованих даних
    3. Сортування злиттям показує стабільну продуктивність, але поступається Timsort
    4. На відсортованих та майже відсортованих даних Timsort показує найкращі результати

    ## Рекомендації
    1. Для загального використання рекомендується використовувати вбудовані функції sorted() або list.sort()
    2. При роботі з маленькими масивами (до 100 елементів) сортування вставками може бути хорошим вибором
    3. Якщо потрібна стабільна продуктивність незалежно від вхідних даних, можна використовувати сортування злиттям
    """)
    
    with open('readme.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("\nРезультати збережено у файлі README.md")

if __name__ == "__main__":
    main()