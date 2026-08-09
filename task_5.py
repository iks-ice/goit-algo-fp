import uuid
import collections
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Робота з деревом"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Отримуємо кольори та мітки безпосередньо з атрибутів вузлів графа
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14, fontweight='bold')
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(steps):
    colors = []
    if steps <= 0:
        return colors
    if steps == 1:
        return ["#1296F0"]
        
    for i in range(steps):
        ratio = i / (steps - 1)
        r = int(18 + ratio * (170 - 18))    # Зміна від темно-синього
        g = int(50 + ratio * (210 - 50))    # до світло-блакитного
        b = int(100 + ratio * (255 - 100))
        
        # Форматуємо у 16-ковий рядок HEX вигляду #RRGGBB
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        colors.append(hex_color)
    return colors

def count_nodes(root):
    if not root:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return count

def dfs_visualize(root):
    if not root:
        return
    
    total_nodes = count_nodes(root)
    color_palette = generate_colors(total_nodes)
    
    stack = [root]
    visited_count = 0
    
    while stack:
        node = stack.pop()
        
        node.color = color_palette[visited_count]
        visited_count += 1
      
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs_visualize(root):
    if not root:
        return
        
    total_nodes = count_nodes(root)
    color_palette = generate_colors(total_nodes)
    
    queue = collections.deque([root])
    visited_count = 0
    
    while queue:
        node = queue.popleft()
        
        node.color = color_palette[visited_count]
        visited_count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def create_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

if __name__ == "__main__":
    tree_dfs = create_sample_tree()
    dfs_visualize(tree_dfs)
    print("Візуалізація DFS активована. Закрийте вікно графіка, щоб перейти до BFS.")
    draw_tree(tree_dfs, title="DFS")
    
    tree_bfs = create_sample_tree()
    bfs_visualize(tree_bfs)
    draw_tree(tree_bfs, title="BFS")
