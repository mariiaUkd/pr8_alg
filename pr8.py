class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self._count = 0

    def add(self, value):
        new_node = Node(value)
        self._count += 1

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else: 
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def contains(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def remove(self, value):
        parent = None
        current = self.root

        while current is not None and current.value != value:
            parent = current
            current = current.left if value < current.value else current.right

        if current is None:
            return False

        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.value = successor.value

            if successor_parent.left is successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            child = current.left if current.left is not None else current.right

            if parent is None:
                self.root = child
            elif parent.left is current:
                parent.left = child
            else:
                parent.right = child

        self._count -= 1
        return True

    def get_all(self):
        """Повертає список усіх елементів у порядку зростання (in-order)."""
        result = []

        def walk(node):
            if node is not None:
                walk(node.left)
                result.append(node.value)
                walk(node.right)

        walk(self.root)
        return result

    def print_all(self):
        print("Елементи дерева:", self.get_all())

    def max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def count(self):
        return self._count


if __name__ == "__main__":
    tree = BinaryTree()

    print("=== Додавання елементів ===")
    for x in [3, 1, 9, 7, 10, 6, 8, 2]:
        tree.add(x)
        print(f"Додано: {x}")
    tree.print_all()

    print("\n=== Пошук ===")
    for x in (7, 5):
        print(f"Елемент {x} {'є' if tree.contains(x) else 'відсутній'} в дереві")

    print("\n=== Найбільший та найменший ===")
    print("Найбільший:", tree.max())
    print("Найменший:", tree.min())

    print("\n=== Кількість ===")
    print("Кількість елементів:", tree.count())

    print("\n=== Видалення ===")
    print("Видаляємо 2 (листок):", tree.remove(2))
    tree.print_all()
    print("Видаляємо 7 (один нащадок):", tree.remove(7))
    tree.print_all()
    print("Видаляємо 3 (корінь, два нащадки):", tree.remove(3))
    tree.print_all()
    print("Видаляємо 100 (немає в дереві):", tree.remove(100))

    print("\nКількість після видалення:", tree.count())
    print("Найбільший:", tree.max(), "| Найменший:", tree.min())