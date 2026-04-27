from collections import deque


class TreeNode:
    "Класс узла бинарного дерева."

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    "Прямой обход: Корень -> Лево -> Право."
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    "Симметричный обход: Лево -> Корень -> Право."
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    "Обратный обход: Лево -> Право -> Корень."
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]



def level_order(root):
    "Обход по уровням с использованием очереди."
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result



def calculate_all_paths_sum(root, current_sum=0):
    """
    Вычисляет сумму значений по всем путям от корня до листьев.
    Если путь 1 -> 2 -> 4, его сумма = 7.
    """
    if not root:
        return 0

    current_sum += root.val

    if not root.left and not root.right:
        return current_sum

    return calculate_all_paths_sum(root.left, current_sum) + \
        calculate_all_paths_sum(root.right, current_sum)



if __name__ == "__main__":
    # Создаем дерево:
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    2   7     20

    root = TreeNode(10)
    root.left = TreeNode(5, TreeNode(2), TreeNode(7))
    root.right = TreeNode(15, None, TreeNode(20))

    print("--- Результаты обходов ---")
    print(f"Прямой:      {preorder(root)}")
    print(f"Симметричный: {inorder(root)}")
    print(f"Обратный:   {postorder(root)}")
    print(f"По уровням:       {level_order(root)}")

    print("\nСвойства дерева ")
    total_sum = calculate_all_paths_sum(root)
    print(f"Сумма всех путей от корня до листьев: {total_sum}")
