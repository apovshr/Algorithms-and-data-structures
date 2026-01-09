import random #

#створюємо пустий стек з конкретним розміром
sizef = 15 * 5 + 50 
stack = []

#робимо перевірку на розмір та вводимо рандомні числа + виводимо стек на екран
check = True
while check == True:
    if len(stack) <= sizef:
        stack.append(random.randint(0,1001))
    else: 
        check = False

print('Initial stack: ', stack)

#робимо ще два стеки для сортування
stack_even = []
stack_uneven = []

#функція сортування на парні та непарні числа + вивід на екран
for number in stack:
    if number % 2 == 0:
        stack_even.append(number)
    else:
        stack_uneven.append(number)

print('\n\nStack with even numbers: ', stack_even)
print('\n\nStack with uneven numbers: ', stack_uneven)