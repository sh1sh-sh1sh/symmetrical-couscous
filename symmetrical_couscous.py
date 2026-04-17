"""
🍝 Symmetrical Couscous - Расширенная версия
Алгоритмический эксперимент на грани абсурда и красоты
"""

import random
import math

def symmetrical_couscous(arr):
    """
    Классический симметрично-кускусный алгоритм.
    Зеркально отражает элементы с плавающим шагом.
    """
    n = len(arr)
    mid = n // 2
    result = arr[:]
    
    for i in range(mid):
        if i % 2 == 0:
            result[i], result[n - 1 - i] = result[n - 1 - i], result[i]
    
    return result


def chaotic_couscous(arr):
    """
    🌪️ Хаотичный кускус - случайные перестановки
    Каждая крупинка ищет своё хаотичное место
    """
    result = arr[:]
    random.shuffle(result)
    return result


def golden_couscous(arr):
    """
    ✨ Золотой кускус - на основе золотого сечения (φ = 1.618)
    Математически совершенная перестановка
    """
    if not arr:
        return arr
    
    n = len(arr)
    golden_ratio = (1 + math.sqrt(5)) / 2
    result = [0] * n
    
    for i in range(n):
        new_index = int((i * golden_ratio) % n)
        result[new_index] = arr[i]
    
    return result


def fractal_couscous(arr):
    """
    🧬 Фрактальный кускус - рекурсивная симметрия
    Кускус внутри кускуса внутри кускуса...
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = fractal_couscous(arr[:mid])
    right = fractal_couscous(arr[mid:])[::-1]
    
    return left + right


def spiral_couscous(arr):
    """
    🐌 Спиральный кускус - закручивает массив по спирали
    """
    if not arr:
        return arr
    
    result = []
    left, right = 0, len(arr) - 1
    
    while left <= right:
        if left == right:
            result.append(arr[left])
            break
        result.append(arr[right])
        result.append(arr[left])
        left += 1
        right -= 1
    
    return result


def visualize_couscous(arr, algorithm=symmetrical_couscous, name="Классический"):
    """Визуализирует работу любого алгоритма кускуса"""
    print(f"🍝 {name} кускус:")
    print(f"   Исходный: {arr}")
    print(f"   Результат: {algorithm(arr)}")
    print("-" * 50)


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("\n" + "="*50)
    print("🍚 СИММЕТРИЧНО-КУСКУСНЫЙ КОМБАЙН 🍝")
    print("="*50 + "\n")
    
    algorithms = [
        (symmetrical_couscous, "Симметричный"),
        (chaotic_couscous, "Хаотичный"),
        (golden_couscous, "Золотой"),
        (fractal_couscous, "Фрактальный"),
        (spiral_couscous, "Спиральный")
    ]
    
    for algo, name in algorithms:
        visualize_couscous(test_array, algo, name)
