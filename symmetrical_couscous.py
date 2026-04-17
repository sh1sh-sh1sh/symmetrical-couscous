def symmetrical_couscous(arr):
    """
    Превращает массив в симметрично-кускусную форму.
    
    Алгоритм зеркально отражает элементы с плавающим шагом,
    создавая уникальную "кускусную" симметрию.
    
    Параметры:
    arr (list): Входной массив чисел
    
    Возвращает:
    list: Симметрично-кускусный массив
    """
    n = len(arr)
    mid = n // 2
    result = arr[:]
    
    for i in range(mid):
        # Симметричный обмен с лёгкой "кускусной деформацией"
        if i % 2 == 0:
            result[i], result[n - 1 - i] = result[n - 1 - i], result[i]
    
    return result


def visualize_couscous(arr):
    """Визуализирует процесс преобразования"""
    print("🍝 Исходный массив:", arr)
    print("🪞 Симметрично-кускусный:", symmetrical_couscous(arr))
    print("-" * 40)


if __name__ == "__main__":
    # Примеры использования
    test_arrays = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [10, 20, 30, 40, 50],
        [1, 1, 2, 3, 5, 8, 13]
    ]
    
    print("🍝🍚 СИММЕТРИЧНО-КУСКУСНЫЙ АЛГОРИТМ 🍚🍝\n")
    
    for arr in test_arrays:
        visualize_couscous(arr)
