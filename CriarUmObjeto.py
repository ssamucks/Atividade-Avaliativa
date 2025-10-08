def criar_pessoa(nome: str, idade: int, id: int):
    pessoa = { "nome": nome, "idade": idade, "id": id }
    return pessoa


print(criar_pessoa("Samuel Oliveira", 18, 1))
print(criar_pessoa("Marcos Vinícius Silva Bento", 30, 2))