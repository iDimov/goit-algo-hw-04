
    # Порівняльний аналіз алгоритмів сортування

    ## Методологія
    - Тестування проводилось на розмірах масивів: [100, 1000, 5000, 10000]
    - Типи даних: випадкові, відсортовані, зворотньо відсортовані, майже відсортовані
    - Для кожного тесту проводилось 3 вимірювань, результат усереднювався

    ## Результати
    ```
Size       Case            Algorithm       Time (seconds) 
-------------------------------------------------------
100        random          Insertion Sort  0.000176       
100        random          Merge Sort      0.000107       
100        random          Timsort         0.000007       
100        sorted          Insertion Sort  0.000008       
100        sorted          Merge Sort      0.000079       
100        sorted          Timsort         0.000001       
100        reversed        Insertion Sort  0.000345       
100        reversed        Merge Sort      0.000084       
100        reversed        Timsort         0.000001       
100        nearly_sorted   Insertion Sort  0.000033       
100        nearly_sorted   Merge Sort      0.000091       
100        nearly_sorted   Timsort         0.000004       
1000       random          Insertion Sort  0.017654       
1000       random          Merge Sort      0.001094       
1000       random          Timsort         0.000064       
1000       sorted          Insertion Sort  0.000074       
1000       sorted          Merge Sort      0.000757       
1000       sorted          Timsort         0.000005       
1000       reversed        Insertion Sort  0.030110       
1000       reversed        Merge Sort      0.000762       
1000       reversed        Timsort         0.000006       
1000       nearly_sorted   Insertion Sort  0.002063       
1000       nearly_sorted   Merge Sort      0.000972       
1000       nearly_sorted   Timsort         0.000034       
5000       random          Insertion Sort  0.427920       
5000       random          Merge Sort      0.006649       
5000       random          Timsort         0.000394       
5000       sorted          Insertion Sort  0.000386       
5000       sorted          Merge Sort      0.004309       
5000       sorted          Timsort         0.000028       
5000       reversed        Insertion Sort  0.816147       
5000       reversed        Merge Sort      0.004520       
5000       reversed        Timsort         0.000030       
5000       nearly_sorted   Insertion Sort  0.054273       
5000       nearly_sorted   Merge Sort      0.006038       
5000       nearly_sorted   Timsort         0.000178       
10000      random          Insertion Sort  Too long       
10000      random          Merge Sort      0.014557       
10000      random          Timsort         0.000861       
10000      sorted          Insertion Sort  Too long       
10000      sorted          Merge Sort      0.009100       
10000      sorted          Timsort         0.000054       
10000      reversed        Insertion Sort  Too long       
10000      reversed        Merge Sort      0.009456       
10000      reversed        Timsort         0.000058       
10000      nearly_sorted   Insertion Sort  Too long       
10000      nearly_sorted   Merge Sort      0.012782       
10000      nearly_sorted   Timsort         0.000366       
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
