import time
import random

# створення масивів з випадковими величинами, зростаючий та спадаючий
def randomn(n):
    return random.sample(range(1, 10001), n)

def ascending(n):
    return list(range(1, n + 1))

def descending(n):
    return list(range(n, 0, -1))

# основна функція з сортування
def sorting(array):
    comparisons = 0 # лічильник порівняння
    assignments = 0 # лічильник присвоєння

    def sortdeeper(array, n, i):
        nonlocal comparisons, assignments
        largest = i # кажемо, що поточний елемент найбільший
        left = 2 * i + 1 # розрахунок лівого вузла
        right = 2 * i + 2 # розрахунок правого вузла

        # якщо лівий вузол у межах масиву, то порівнюємо з найбільшим
        if left < n:
            comparisons += 1
            if array[left] > array[largest]:
                largest = left

        # якщо правий вузол у межах масиву, то порівнюємо з найбільшим
        if right < n:
            comparisons += 1
            if array[right] > array[largest]:
                largest = right

        # якщо найбільший вузол змінився, то змінюємо місцями
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            assignments += 3
            sortdeeper(array, n, largest)

    n = len(array)
    start_time = time.perf_counter() # початок вимірювання часу

    # виклик функції сортування (елементи без дітей не враховуємо)
    for i in range(n // 2 - 1, -1, -1):
        sortdeeper(array, n, i)

    # ставимо найбільші елементи у кінець масиву
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        assignments += 3
        sortdeeper(array, i, 0)

    elapsed_time = time.perf_counter() - start_time # кінець вимірювання часу
    return elapsed_time, comparisons, assignments  # порядок як у твоєму прикладі


# основна функція
def main():
    sizes = [10, 100, 1000, 5000, 10000]

    print("n | Type | Time (s) | Comparisons | Assignments")

    # заповнюємо масиви
    for n in sizes:
        arrays = {
            "Random": randomn(n),
            "Ascending": ascending(n),
            "Descending": descending(n)
        }

        # виводимо на екран результати 
        for name, arr in arrays.items():
            arr_copy = arr.copy()
            time_spent, comps, assigns = sorting(arr_copy)
            print(n, "|", name, "|", round(time_spent, 6), "|", comps, "|", assigns)


# виклик головної main функції одразу на початку роботи програми
if __name__ == "__main__":
    main()
