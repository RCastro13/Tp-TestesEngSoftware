class Livro:
    def __init__(self, isbn: str, nome: str):
        self.isbn = isbn
        self.nome = nome

    def get_isbn(self) -> str:
        return self.isbn
