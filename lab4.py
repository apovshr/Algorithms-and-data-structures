class Tree:
    # це функція для формування вузла
    def __init__(self, value):
        self.value = value # значення вузла
        self.left = None   # ліва дитина
        self.right = None  # права дитина
        self.parent = None # чи є батьки

    #функція додавання дитини
    def add_child(self, child):
        if child.value < self.value:
            if self.left:
                self.left.add_child(child) # якщо лівий вузол існує, йдемо глибше
            else:
                child.parent = self
                self.left = child
        else:
            if self.right:
                self.right.add_child(child) # якщо правий вузол існує, йдемо глибше
            else:
                child.parent = self # призничаємо батька для дитини (поточний вузол)
                self.right = child # призначаємо дитину у правий вузол

    #початкове дерево
    def initial_tree(self):
        root = Tree(10) #корінь
        leftchild = Tree(5) #ліва дитина
        rightchild = Tree(12) #права дитина

        #через метод додавання додали дітей до вузла (10)
        root.add_child(leftchild)
        root.add_child(rightchild)
        return root # повертаємо дерево, щоб можна було користуватися за цією функцією

    #функція пошуку
    def search(self, child_find):
        if self.value == child_find:
            return self  # повертаємо вузол

        # дивимося чи дитя у лівому вузлі
        if child_find < self.value and self.left:
            return self.left.search(child_find)
        
        # дивимочя чи дитя у правому вузлі
        elif child_find > self.value and self.right:
            return self.right.search(child_find)
        else:
            return None

    #видалення дитини
    def delete_child(self, value):
        node = self.search(value)
        if node:
            # випадок: вузол без дітей
            if not node.left and not node.right:
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                return True

            # випадок: вузол з однією дитиною
            if node.left and not node.right:
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = node.left
                    else:
                        node.parent.right = node.left
                node.left.parent = node.parent
                return True
            if node.right and not node.left:
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = node.right
                    else:
                        node.parent.right = node.right
                node.right.parent = node.parent
                return True

            # випадок: вузол з двома дітьми
            # знаходимо мінімальний вузол правого піддерева
            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            successor.delete_child(successor.value)
            return True
        else:
            return False

    #функція для рівня, для оформлення дерева при виводі
    def get_level(self):
        level = 0 # рівень
        p = self.parent # беремо батька поточного вузла
        while p:
            level += 1
            p = p.parent # переходимо до батька батька
        return level

    # функція для гарного виведення дерева
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3 # рахуємо відступи
        prefix = spaces + '|__ ' if self.parent else "" # гарно виставляємо
        print(prefix + str(self.value))

        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


# головна функція
if __name__ == '__main__':
    root = Tree(0).initial_tree() # отримуємо посилання на початкове дерево
    root.print_tree() # виводимо дерево на екран

    choice = True

    # меню з опціями
    while choice:
        choice = int(input('\n\nChoose an action: 1 - Add a child, 2 - Delete a child, ' \
        '3 - Search for a child, 4 - Exit: '))

        # перевірка вибору
        while choice not in [1, 2, 3, 4]:
            choice = int(input('Error! Please choose on of options (1 - Add a child, 2 - Delete a root or a child,' \
            ' 3 - Search for a root/child, 4 - Exit):  '))

        # виклик функцій в залежності від вибору
        match choice:
            case 1:
                child_value = int(input("Enter the value of the new child: "))
                root.add_child(Tree(child_value))  

            case 2:
                value = int(input('Enter a child for deletion: '))
                if root.delete_child(value):
                    print(f'Node {value} deleted!')
                else:
                    print(f'Node {value} not found!')

            case 3:
                value = int(input('Enter a child for finding: '))
                if root.search(value):
                    print(f'Child {value} was found!')
                else:
                    print(f'Child {value} was not found')

            case 4:
                break

    # вивід кінцевого дерева
    root.print_tree()
