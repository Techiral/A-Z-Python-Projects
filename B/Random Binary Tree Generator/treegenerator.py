import random 
  
  
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None
  
def generate_random_binary_tree(size): 
    if size == 0: 
        return None
  
    # Choose random sizes for left and right subtrees 
    left_size = random.randint(0, size-1) 
    right_size = size - 1 - left_size 
  
    # Generate left and right subtrees recursively 
    left_subtree = generate_random_binary_tree(left_size) 
    right_subtree = generate_random_binary_tree(right_size) 
  
    # Create new node with random value 
    root = Node(random.randint(0, 100)) 
  
    # Assign left and right subtrees to children 
    root.left = left_subtree 
    root.right = right_subtree 
  
    return root 
  
  
def print_tree(node, level=0): 
    if node is not None: 
        print_tree(node.right, level + 1) 
        print(" " * 4 * level + "->", node.value) 
        print_tree(node.left, level + 1) 
  
  
tree = generate_random_binary_tree(input('Enter the size of binary tree')) 
print_tree(tree) 