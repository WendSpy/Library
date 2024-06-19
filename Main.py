print("Cadastro de livros")

from Livraria import Livraria

# Cadastro de livros
livros = []

def adicionar_livro():
    livraria = Livraria()
    livraria.add_livro()
    livros.append(livraria)
# Localizador de livros
def localizar_livro():
    #Pedir o nome do livro
    nome = input("\nDigite o nome do livro que deseja localizar:")
    #Verificar se o livro foi encontrado ou não
    encontrado = False
    for livro in livros:
        #Se existir algum livro cadastrado com o mesmo nome digitado na procura 
        if livro.livro == nome:
            print("\nLivro encontrado:")
            livro.mostrar_livro()
            encontrado = True
            break
    #Se não existir um livro com o mesmo nome
    if not encontrado:
        print("Livro não encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Localizar livro")
    print("3. Sair")
    opcao = input("Escolha uma opção (1, 2, 3):\n")
    
    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        localizar_livro()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")