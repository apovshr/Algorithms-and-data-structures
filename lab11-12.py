# алгоритми Прима і Крускала для мінімального остовного дерева

def MST_Kruskal(V, E):
    A = []                  # список ребер остовного дерева
    parent = {}

    # створюємо окрему множину для кожної вершини
    for v in V:
        parent[v] = v

    # пошук множини
    def Find_Set(v):
        while parent[v] != v:
            v = parent[v]
        return v

    # обʼєднання двох множин
    def Union(u, v):
        parent[Find_Set(v)] = Find_Set(u)

    # сортуємо ребра за зростанням ваг
    E.sort(key=lambda x: x[2])

    # проходимо всі ребра
    for (u, v, w) in E:
        if Find_Set(u) != Find_Set(v):
            A.append((u, v, w))
            Union(u, v)

    return A


def MST_Prim(V, E, r):
    INF = 10**9
    key = {}
    prev = {}

    # початкові значення
    for v in V:
        key[v] = INF
        prev[v] = None

    key[r] = 0
    Q = V.copy()

    # поки є вершини для обробки
    while Q:
        u = Q[0]
        for x in Q:
            if key[x] < key[u]:
                u = x

        Q.remove(u)

        # переглядаємо всі суміжні вершини
        for (a, b, w) in E:
            if a == u:
                v = b
            elif b == u:
                v = a
            else:
                continue

            if v in Q and w < key[v]:
                prev[v] = u
                key[v] = w

    return prev, key


def main():
    V = [1,2,3,4,5,6,7,8,9,10]

    # усі ребра та їх вага
    E = [
        (3,5,12), (3,2,10),
        (2,4,2), (2,1,5),
        (1,6,4), (1,7,6),
        (4,6,11), (4,5,9),
        (4,8,7), (5,8,5),
        (8,9,10), (9,10,11),
        (8,10,5), (6,8,13),
        (6,9,15), (6,7,15),
        (7,9,16), (7,10,9)
    ]

    print("Мінімальне остовне дерево за алгоритмом Крускала")
    mst_k = MST_Kruskal(V, E)
    for e in mst_k:
        print(e)

    print("\nМінімальне остовне дерево за алгоритмом Прима")
    prev, key = MST_Prim(V, E, 1)
    for v in V:
        if prev[v] is not None:
            print(prev[v], "-", v, "вага", key[v])


main()
