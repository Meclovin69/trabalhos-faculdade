class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []    

  def inserir(self, item):
    self.items.insert(0,item)

  def remover(self):
    return self.items.pop()

  def index(self,i):
    return self.items.index(i)

  def tamanho(self):
    return len(self.items.index)

q=Queue()    
opcao = 0

while opcao != 5:
  print("\n------------MENU------------\n")
  print("1 - Adicionar um elemento")
  print("2 - Remover um elemento")
  print("3 - Verificar tamanho da Fila")
  print("4 - Procurar elemento")
  print("5 - SAIR")
  
  opcao = int(input("\nDigite qual acao deseja realizar:"))

  if opcao == 1:
    i = int(input("\nDigite o elemento a ser inserido: "))
    q.inserir(i)
    print("Lista atual: ",q.items)

  elif opcao == 2:
    q.remover()
    print("Lista atual: ",q.items)
    
  elif opcao == 3:
    print("Tamanho da Lista atual: ",q.tamanho() )

  elif opcao == 4:
    f = int(input("\nDigite o numero que deseja buscar: "))
    print("Index da fila: ",q.index(f) )

  elif opcao == 5:
    print("Saindo...\n")
    exit()

  else:
    print("Opcao invalida tente novamente!")
  