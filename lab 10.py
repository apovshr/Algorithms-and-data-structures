from collections import Counter

# Текст для кодування
text = "Моржа коржами кормили"

# Підрахунок частот символів та вивід на екран
frequencies = Counter(text)
print("Частоти символів:")
for char, freq in frequencies.items():
    print(f"'{char}': {freq}")

# ставимо символи та залишаємо місце для кодів
nodes = [[c, frequencies[c]] for c in frequencies]  

# функція з методом Гаффмана
while len(nodes) > 1:

    # Знаходимо два символи з найменшою частотою
    nodes = sorted(nodes, key=lambda x: x[1])  # сортуємо за частотою
    first = nodes.pop(0)
    second = nodes.pop(0)

    # Створюємо новий батьківський вузол
    new_char = (first[0], second[0])  # зберігаємо дітей 
    new_freq = first[1] + second[1]
    nodes.append([new_char, new_freq])

codes = {}

def build_codes(node, prefix=""):

    # Якщо вузол — символ (рядок), присвоюємо код
    if isinstance(node, str):
        codes[node] = prefix
    else:
        # вузол з двох дітей
        build_codes(node[0], prefix + "0")  # ліва гілка - 0
        build_codes(node[1], prefix + "1")  # права гілка - 1

build_codes(nodes[0][0])
print("Коди Гаффмана:", codes)

# Кодуємо текст
encoded = ""
for c in text:
    encoded += codes[c]
print("Закодований текст:", encoded)

# Декодуємо текст
decoded = ""
current = ""
rev_codes = {v: k for k, v in codes.items()} 
for bit in encoded:
    current += bit
    if current in rev_codes:
        decoded += rev_codes[current]
        current = ""
print("Декодований текст:", decoded)
