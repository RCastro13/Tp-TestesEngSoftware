from typing import List, Dict
from Livro import Livro
from Usuario import Usuario
from Repositorio import Repositorio

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.acervo: Dict[str, Livro] = {}
        self.emprestimos: Dict[Livro, Usuario] = {}

    def adicionar_livro_acervo(self, isbn: str, livro: Livro):
        self.acervo[isbn] = livro

    def livro_esta_emprestado(self, livro: Livro) -> bool:
        return livro in self.emprestimos

    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        self.emprestimos[livro] = usuario

    def receber_livro_emprestado(self, livro: Livro):
        if livro in self.emprestimos:
            del self.emprestimos[livro]

    def livros_emprestados_usuario(self, usuario: Usuario) -> List[Livro]:
        return [livro for livro, user in self.emprestimos.items() if user == usuario]
