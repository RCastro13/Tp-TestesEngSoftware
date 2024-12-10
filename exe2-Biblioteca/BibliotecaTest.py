import pytest
from Biblioteca import Biblioteca
from RepositorioMemoria import RepositorioMemoria
from Livro import Livro
from Usuario import Usuario
from ExcecaoLivroEmprestado import ExcecaoLivroEmprestado

@pytest.fixture
def setup_biblioteca():
    repo = RepositorioMemoria()
    bib = Biblioteca(repo)
    livro1 = Livro("isbn1", "ESM")
    livro2 = Livro("isbn2", "GoF")
    livro3 = Livro("isbn3", "XP")
    bib.adicionar_livro_acervo(livro1)
    bib.adicionar_livro_acervo(livro2)
    bib.adicionar_livro_acervo(livro3)
    return bib, livro1, livro2, livro3

def test_emprestar_livro(setup_biblioteca):
    bib, livro1, livro2, _ = setup_biblioteca
    usuario = Usuario("usu1", "João")
    bib.emprestar_livro(livro1, usuario)
    bib.emprestar_livro(livro2, usuario)
    emprestados = bib.livros_emprestados_usuario(usuario)
    assert len(emprestados) == 2
    assert livro1 in emprestados
    assert livro2 in emprestados

def test_emprestimo_vazio(setup_biblioteca):
    bib, _, _, _ = setup_biblioteca
    usuario = Usuario("usu1", "João")
    emprestados = bib.livros_emprestados_usuario(usuario)
    assert len(emprestados) == 0

def test_emprestimo_e_devolucao(setup_biblioteca):
    bib, livro1, livro2, _ = setup_biblioteca
    usuario = Usuario("usu1", "João")
    bib.emprestar_livro(livro1, usuario)
    bib.emprestar_livro(livro2, usuario)
    bib.receber_livro_emprestado(livro1)
    emprestados = bib.livros_emprestados_usuario(usuario)
    assert len(emprestados) == 1
    assert livro1 not in emprestados
    assert livro2 in emprestados

def test_emprestar_livro_ja_emprestado(setup_biblioteca):
    bib, livro1, _, _ = setup_biblioteca
    usuario1 = Usuario("usu1", "João")
    usuario2 = Usuario("usu2", "Maria")
    bib.emprestar_livro(livro1, usuario1)
    with pytest.raises(ExcecaoLivroEmprestado):
        bib.emprestar_livro(livro1, usuario2)
