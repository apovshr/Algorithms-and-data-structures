import time
import random

# створення масивів з випадковими величинами, зростаючий та спадаючий
def randomnum(n):
    return random.sample(range(1, 10001), n)

def ascending(n):
    return list(range(1, n + 1))

def descending(n):
    return list(range(n, 0, -1))

# функція для перестановки елементів (порівнюючи з опорним)
def partition(A, p, r):
    comparisons = 0
    assignments = 0
    
    mid = (p + r) // 2        # вибираємо середній елемент як опорний
    A[mid], A[r] = A[r], A[mid]
    assignments += 3
    
    x = A[r]                  # опорний елемент
    i = p - 1                 # межа для елементів лівої частини
    for j in range(p, r):
        comparisons += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]   # міняємо місцями
            assignments += 3
    A[i + 1], A[r] = A[r], A[i + 1]   # ставимо опорний елемент на своє місце
    assignments += 3
    return i + 1, comparisons, assignments

# функція виклику перестановок, а також підрахунку порівнянь та присвоювань
def quicksort(A, p, r):
    comparisons = 0
    assignments = 0
    if p < r:
        q, comp, assign = partition(A, p, r)
        comparisons += comp
        assignments += assign
        
        comp_left, assign_left = quicksort(A, p, q - 1)  # сортуємо ліву частину
        comp_right, assign_right = quicksort(A, q + 1, r) # сортуємо праву частину
        
        comparisons += comp_left + comp_right
        assignments += assign_left + assign_right

    return comparisons, assignments

# основна функція з підведенням результатів
def main():
    sizes = [10, 100, 1000, 5000, 10000]
    print("n | Type | Time (s) | Comparisons | Assignments")

    # створюємо масиви
    for n in sizes:
        arrays = {
            "Random": randomnum(n),
            "Ascending": ascending(n),
            "Descending": descending(n)
        }

        # закінчуємо підрахування та виводимо результати
        for name, arr in arrays.items():
            arr_copy = arr.copy()
            start_time = time.perf_counter()  # початок вимірювання часу
            comps, assigns = quicksort(arr_copy, 0, len(arr_copy) - 1)
            time_spent = time.perf_counter() - start_time  # кінець вимірювання часу
            print(n, "|", name, "|", round(time_spent, 6), "|", comps, "|", assigns)

if __name__ == "__main__":
    main()
