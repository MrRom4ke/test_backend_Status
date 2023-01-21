"""
Тестовое задание в компанию Статус на вакансию backend developer Python
ЗАДАНИЕ
Есть массив объектов, которые имеют поля id и parent,
через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
 - getAll() Должен возвращать изначальный массив элементов.
 - getItem(id) Принимает id элемента и возвращает сам объект элемента;
 - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
 - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
в идеале, прямой доступ к элементам без поиска их в массиве.
"""
from typing import List


class TreeStore:
    def __init__(self, ts_item: List[dict]) -> None:
        """
        Конструктор массива.
        """
        self.ts_item = ts_item

    def getAll(self):
        """
        Возвращает изначальный массив элементов.
        """
        return self.ts_item

    def getItem(self, id):
        """
        Принимает id элемента и возвращает сам объект элемента.
        """
        return next((elem for elem in self.ts_item if elem.get('id') == id), None)

    def getChildren(self, id):
        """
        Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
        чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив.
        """
        return [elem for elem in self.ts_item if elem.get('parent') == id]

    def getAllParents(self, id):
        """
        Принимает id элемента и возвращает массив из цепочки родительских элементов,
        начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
        т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок эл-тов важен!
        """
        all_parent = []
        ancestor = self.ts_item[id - 1].get('parent')
        while ancestor != 'root':
            all_parent.append(self.ts_item[ancestor - 1])
            ancestor = self.ts_item[ancestor - 1].get('parent')
        return all_parent


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# Примеры использования:
#  - ts.getAll() // [
#  {"id":1,"parent":"root"},
#  {"id":2,"parent":1,"type":"test"},
#  {"id":3,"parent":1,"type":"test"},
#  {"id":4,"parent":2,"type":"test"},
#  {"id":5,"parent":2,"type":"test"},
#  {"id":6,"parent":2,"type":"test"},
#  {"id":7,"parent":4,"type":None},
#  {"id":8,"parent":4,"type":None}
#  ]
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#  - ts.getAllParents(7) // [
#  {"id":4,"parent":2,"type":"test"},
#  {"id":2,"parent":1,"type":"test"},
#  {"id":1,"parent":"root"}
#  ]
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))