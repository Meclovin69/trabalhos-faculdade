class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeB:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

# Cria uma árvore vazia
tree = TreeB()

while True:
    print("--------MENU--------")
    print("\n1. Inserir")
    print("2. Buscar")
    print("3. Mostrar EM ORDEM")
    print("4. Mostrar PRE ORDEM")
    print("5. Mostrar PÔS ORDEM")
    print("6. Sair")
    print("\n--------------------")

    option = int(input("Escolha uma opção: "))

    if option == 1:
        
        value = int(input("Insira o número: "))
        tree.insert(value)
        
    elif option == 2:
        value = int(input("Insira o número a ser buscado: "))
        
        if tree.search(value):
            print("O número está na árvore")
        else:
            print("O número não está na árvore")
            
    elif option == 3:
        print("Valores da árvore em ordem:")
        tree.in_order(tree.root)
        
    elif option == 4:
        print("Valores da árvore em pré-ordem:")
        tree.pre_order(tree.root)
        
    elif option == 5:
        print("Valores da árvore em pós-ordem:")
        tree.post_order(tree.root)
        
    elif option == 6:
        break
    
    else:
        print("Opção inválida")