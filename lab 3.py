import random

# проводимо розрахунки по розмірам
N = 15 * 5 + 50
S = int(N * 0.75)

# формуємо геш таблицю з випадковими числами
hash_table = {}

for i in range(N):
    key = random.randint(0, S-1)
    value = random.randint(0, 1000)
    hash_table[key] = value

# основні функції: вставка, видалення, пошук
def insert(key, value):
    hash_table[key] = value
    print(f'New element was added to hash table: value: {value}, key: {key} ')

def delete(key):
    if key in hash_table:
        del hash_table[key]
        print(f'Element with a key: {key} was successfuly deleted!')
    else:
        print(f'Error! Could not find a key {key}')

def search(key):
    if key in hash_table:
        print(f'Found an element! Key: {key}, value: {hash_table[key]}')
    else:
        print(f'Error! Could not find a value for key {key}')

# виводимо початкову таблицю на екран
print('Hash table: \n')
print(hash_table)

# меню з виборами дій
def main ():
    menu = True
    while menu:
        choice = int(input('\n\nChoose an action: 1 - insert, 2 - delete, 3 - search, 4 - exit: '))
        if choice not in [1, 2, 3, 4]:
            choice = int(input('Error! Please choose a number of action (1-4): '))

        match choice:
            case 1:
                key = int(input('Enter a new key: '))
                value = int(input('Enter new value: '))
                insert(key, value)
            case 2:
                key = int(input('Enter a key for delition: '))
                delete(key)
            case 3:
                key = int(input('Enter a key for searching: '))
                search(key)
            case 4:
                menu = False

main()

# формування нової таблиці з непарними значеннями
for key in list(hash_table.keys()):
    if hash_table[key] % 2 == 0:
        del hash_table[key]

print('\nNew hash table with uneven values: ', hash_table)

