from ValidadoresMP import Validadores
from crudMP import GerenciadorDados
import json


validador = Validadores()
controleDados = GerenciadorDados()
listaProdutos = controleDados.ler_json()
listaNome = list()
listaNome = GerenciadorDados.retornaListaNomeProduto(controleDados, listaProdutos, listaNome)

produto1 = {
    "nome": "Pao",
    "peso": 5, 
    "UN": "KG",
    "preco": 5.00, 
    "categoria": "Comida"
}

for produtos in listaProdutos:
    print(f"Nome {produtos['nome']}, {produtos['preco']}")

print('----------------')

for nome in listaNome:
    print(nome)


print('----------------')

controleDados.insereProduto(produto1, listaProdutos)

listaNome = GerenciadorDados.retornaListaNomeProduto(controleDados, listaProdutos, listaNome)

for nome in listaNome:
    print(nome)

print('----------------')

for produtos in listaProdutos:
    print(f"Nome {produtos['nome']}, {produtos['preco']}")

print('----------------')