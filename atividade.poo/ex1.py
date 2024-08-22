'''1. Suponha que você está desenvolvendo um sistema de biblioteca. Crie a
classe Livro com as seguintes características:
○ Atributos: titulo, autor, ano_publicacao.
○ Métodos: exibir_detalhes.
'''
class livro:
    def __init__(self,titulo,autor,ano_publiacao):
       self.titulo = titulo
       self.autor = autor 
       self.ano_publicacao = ano_publiacao
    def exibir_detalhes(self):
        print(f"titulo:{self.titulo}.\n autor:{self.autor}.\n ano_pulicacao:{self.ano_publicacao}.")

livro1 = livro("Dom casmuro","machado de assis ",1899)       
livro2 = livro("Mobdky","paula",2002)
livro1.exibir_detalhes()
print("-"*10)
livro2.exibir_detalhes() 
#para coleta o nome do titulo 
print(f'O nome do livro 1 é ', livro1.titulo)
        
        