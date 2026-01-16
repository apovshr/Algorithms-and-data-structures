import random 
import time

# функція для заповнення списків випадковими номерами
def filling(n):
    return random.sample(range(1, 10001), n)

# функція зростання
def ascending(n):
    return list(range(1, n + 1))


# функція спадання
def descending(n):
    return list(range(n, 0, -1))


# усі масиви з заповненням та відсортовуванням
def insertion_sort(array):
    comparisons = 0
    assignments = 0

    start_time = time.perf_counter() # початок рахунку часу

    # функція на зростання
    for j in range(1, len(array)):
        key = array[j]
        assignments += 1
        i = j - 1

        while i >= 0 and array[i] > key:
            comparisons += 1
            array[i + 1] = array[i]
            assignments += 1
            i -= 1
        comparisons += 1  # останнє порівняння, коли while не спрацював
        array[i + 1] = key
        assignments += 1

    end_time = time.perf_counter()  # кінець часу
    return end_time - start_time, comparisons, assignments

# основна функція main
def main():

    # задаємо розміри усім масивам
    sizes = [10, 100, 1000, 5000, 10000]

    print("n | Type | Time(s) | Comparisons | Assignments")

    # працюємо над кожним масивом (випадкове заповнення, зростання, спадіння)
    for n in sizes:
        arrays = {
            "Random": filling(n),
            "Ascending": ascending(n),
            "Descending": descending(n)
        }

        for name, arr in arrays.items():
            arr_copy = arr.copy()  # щоб оригінал не змінювався
            time_spent, comps, assigns = insertion_sort(arr_copy)
            print(n, "|", name, "|", round(time_spent, 6), "|", comps, "|", assigns)

# Запуск
if __name__ == "__main__":
    main()



