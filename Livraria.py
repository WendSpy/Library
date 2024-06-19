class Livraria:
    def __init__(self, livro=None, genero=None, prateleira=None, quantidade=0):
        self.livro = livro
        self.genero = genero
        self.prateleira = prateleira
        self.quantidade = quantidade
    
    def add_livro(self):
        self.livro = input("\nNome do livro: ")
        self.genero = input("\nGênero do livro: ")
        self.quantidade = int(input("\nQuantidade de livros: "))
        self.prateleira = input("\nPrateleira do livro: ")
        
        print(f'Livro "{self.livro}" adicionado com sucesso!')
    
    def mostrar_livro(self):
        print(f'Livro: {self.livro}')
        print(f'Gênero: {self.genero}')
        print(f'Prateleira: {self.prateleira}')
        print(f'Quantidade: {self.quantidade}')
