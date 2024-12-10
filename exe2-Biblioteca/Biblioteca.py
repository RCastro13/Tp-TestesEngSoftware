from typing import List
from Repositorio import Repositorio
from Livro import Livro
from Usuario import Usuario
from ExcecaoLivroEmprestado import ExcecaoLivroEmprestado

class Biblioteca:
    def __init__(self, repo: Repositorio):
        self.repo = repo

    def adicionar_livro_acervo(self, livro: Livro):
        self.repo.adicionar_livro_acervo(livro.get_isbn(), livro)

    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        if self.repo.livro_esta_emprestado(livro):
            raise ExcecaoLivroEmprestado("Livro já está emprestado!")
        self.repo.emprestar_livro(livro, usuario)

    def receber_livro_emprestado(self, livro: Livro):
        self.repo.receber_livro_emprestado(livro)

    def livros_emprestados_usuario(self, usuario: Usuario) -> List[Livro]:
        return self.repo.livros_emprestados_usuario(usuario)