# імпортуємо бібліотеки для
from collections import deque # черг
import random # генерування випадкових чисел
import math # рахування простих чисел

# створюємо чергу й зазаначаємо розмір
queue = deque()
itssize = 15 * 5 + 50

# заповнюємо чергу віпадковими числами
while itssize >= len(queue):
    queue.append(random.randint(1,1000))

# усі стандартні операції
def enqueue():
    queue.append(int(input('Enter a number you want to add to queue: ')))
    print('\nUpdated queue: \n', queue)

def dequeue():
    queue.popleft()
    print('\nUpdated queue: \n', queue)

def peek():
    print(queue[0])

def isfull():
    if len(queue) == itssize:
        print('Queue is full!')
    else:
        print('Queue is not full')

def isempty():
    if len(queue) == 0:
        print('Queue is empty')
    else:
        print('Queue is not empty')

# вивід новостворенної черги
print('Initial queue: \n', queue)

# основне меню, де можна викликати усі основні функції
def main():
    menu = True
    while menu:
        n = input('\n\nWhat do you wanna do? '
                '1 - equeue, 2 - dequeue, 3 - peek, 4 - check if queue is full,'
                '5 - check if queue is empty, 6 - exit: ')
        while n not in ['1', '2', '3', '4', '5', '6']:
            n = input('There is not such an option, please choose option from (1-6): ')
    
        match n:
            case '1':
                enqueue()
            case '2':
                dequeue()
            case '3':
                peek()
            case '4':
                isfull()
            case '5':
                isempty()
            case '6':
                menu = False

# виклик основного меню           
main()

# вивід зміненної черги 
print('\n\nQueue now: \n', queue)

# працюємо над новою чергою з простими числами, для цього створюємо нову чергу та пишемо умову, 
# використовуючи математичну бібліотеку, користувачу виводимо результат
print('\n\nQueue with only prime numbers: \n\n')

newqueue = deque()

for i in queue:
    if i > 1 and all(i % d != 0 for d in range(2, int(math.sqrt(i)) + 1)):
        newqueue.append(i)

print(newqueue)
