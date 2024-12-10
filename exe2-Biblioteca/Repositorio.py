from abc import ABC, abstractmethod
from typing import List
from Livro import Livro
from Usuario import Usuario

class Repositorio(ABC):
    @abstractmethod
    def adicionar_livro_acervo(self, isbn: str, livro: Livro):
        pass

    @abstractmethod
    def livro_esta_emprestado(self, livro: Livro) -> bool:
        pass

    @abstractmethod
    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        pass

    @abstractmethod
    def receber_livro_emprestado(self, livro: Livro):
        pass

    @abstractmethod
    def livros_emprestados_usuario(self, usuario: Usuario) -> List[Livro]:
        pass
