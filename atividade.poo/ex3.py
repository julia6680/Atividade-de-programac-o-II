'''3'' Desenvolva um sistema de estoque que possui a Classe produtos com as
seguintes características:
○ Atributos: nome, preco, quantidade e codigo.
○ Métodos: calcular_total, atualizar_preco e verificar_disponibilidade.'''

class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo
    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"Valor total em estoque do produto '{self.nome}' (Código: {self.codigo}): R${total:.2f}")
        return total
    def atualizar_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
            print(f"Preço do produto '{self.nome}' (Código: {self.codigo}) atualizado para R${self.preco:.2f}")
        else:
            print("O preço deve ser positivo.")
    def verificar_disponibilidade(self):
        if self.quantidade > 0:
            print(f"Produto '{self.nome}' (Código: {self.codigo}) está disponível. Quantidade em estoque: {self.quantidade}")
        else:
            print(f"Produto '{self.nome}' (Código: {self.codigo}) está esgota:{self.quantidade}")
                  
produto1 = Produto(nome="Camiseta", preco=29.90, quantidade=100, codigo="123")
produto2 = Produto(nome="Tênis", preco=199.90, quantidade=0, codigo="456")


produto1.calcular_total()

produto1.atualizar_preco(50.40)

produto1.verificar_disponibilidade()

produto2.verificar_disponibilidade()