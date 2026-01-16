import random
import time

# основні функції заповнення: випадкові знач., зростання, спадіння
def filling(n):
    return random.sample(range(1, 10001), n)

def ascending(n):
    return list(range(1, n + 1))

def descending(n):
    return list(range(n, 0, -1))

def merge_sort(array):
    # лічильники для всієї функції merge_sort
    comparisons = 0
    assignments = 0

    def merge(A, p, q, r):
        nonlocal comparisons, assignments  # тепер можемо змінювати зовнішні лічильники

        n1 = q - p + 1 #к-сть елементів у першій половині
        n2 = r - q #к-сть елементів у другій половині

        # створюємо L та R - масиви для злиття
        L = [0] * (n1 + 1) # кожен з елементів 0
        R = [0] * (n2 + 1)

        # копіюємо дані в L та R
        for i in range(n1):
            L[i] = A[p + i]
            assignments += 1
        for j in range(n2):
            R[j] = A[q + 1 + j]
            assignments += 1

        # додаємо "∞" в кінець
        L[n1] = float('inf')
        R[n2] = float('inf')
        assignments += 2

        i = j = 0
        for k in range(p, r + 1):
            comparisons += 1
            if L[i] <= R[j]:
                A[k] = L[i]
                assignments += 1
                i += 1
            else:
                A[k] = R[j]
                assignments += 1
                j += 1

    # Рекурсивна функція
    def merge_sort_recursive(A, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort_recursive(A, p, q)
            merge_sort_recursive(A, q + 1, r)
            merge(A, p, q, r)

    # вимірювання часу
    start_time = time.perf_counter()
    merge_sort_recursive(array, 0, len(array) - 1)
    end_time = time.perf_counter()

    return end_time - start_time, comparisons, assignments

# Основна функція main
def main():
    sizes = [10, 100, 1000, 5000, 10000]

    print("n | Type | Time(s) | Comparisons | Assignments")

    for n in sizes:
        arrays = {
            "Random": filling(n),
            "Ascending": ascending(n),
            "Descending": descending(n)
        }

        for name, arr in arrays.items():
            arr_copy = arr.copy()
            time_spent, comps, assigns = merge_sort(arr_copy)
            print(n, "|", name, "|", round(time_spent, 6), "|", comps, "|", assigns)

if __name__ == "__main__":
    main()
