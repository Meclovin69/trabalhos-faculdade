class NodoLista:
    def __init__(self, dado = 0, proximo_nodo = None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self._size = 0

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def index(lista, novo_dado):
            pointer = lista.cabeca
            i = 0
            while(pointer):
                if pointer.dado == novo_dado:
                        return i
                pointer = pointer.proximo
                i = i+1
            raise ValueError(f"{novo_dado} não está na lista")

    def __len__(self):
        return self._size

    def remove(lista, novo_dado):
        if lista.cabeca == None:
            raise ValueError(f"{novo_dado} não está na lista")
        elif lista.cabeca.dado == novo_dado:
            lista.cabeca = lista.cabeca.proximo
            return True
        else:
            ancestor = lista.cabeca
            pointer = lista.cabeca.proximo
            while(pointer):
                if pointer.dado == novo_dado:
                    ancestor.proximo = pointer.proximo
                    pointer.proximo = None
                ancestor = pointer
                pointer = pointer.proximo
            return True
        raise ValueError(f"{novo_dado} não está na lista")   

    def remover(lista):
        return lista.pop()
                

def append(lista, novo_dado):
    if lista.cabeca:
        pointer = lista.cabeca
        while(pointer.proximo):
            pointer = pointer.proximo
        pointer.proximo = NodoLista(novo_dado)
    else:
        lista.cabeca = NodoLista(novo_dado)
    lista._size = lista._size+1
    
lista = ListaEncadeada() 
opcao = 0

while opcao != 5:
  print("1 - Adicionar um elemento")
  print("2 - Remover um elemento")
  print("3 - Verificar tamanho da Fila")
  print("4 - Procurar elemento")
  print("5 - Sair")
  
  opcao = int(input("\nDigite qual acao deseja realizar:"))

  if opcao == 1:
    i = int(input("\nDigite o elemento a ser inserido: "))
    append(lista, i)
    print("Lista atual: ", lista )

  elif opcao == 2:
    e = int(input("\nDigite o elemento a ser deletado: "))
    lista.remove(e)
    print("Elemento removido: ", lista)

  elif opcao == 3:
    d = len(lista)
    print("O tamanho é: ", d)

  elif opcao == 4:
    b = int(input("\nDigite o número que deseja buscar: "))
    c = lista.index(b)
    print("A localização das na lista é:", c)

  elif opcao == 5:
    print("Saindo...\n")
    exit()

  else:
    print("Opcao invalida tente novamente!")
