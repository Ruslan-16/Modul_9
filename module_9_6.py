
def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):  # Длина подпоследовательностей
        for i in range(n - length + 1):  # Начальный индекс
            yield text[i:i + length]  # Срез от i до i + length

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)


