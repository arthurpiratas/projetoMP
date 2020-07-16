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

nome1 = "Açucar"
peso1 = "5"
un1 = "KG"
preco1 = 5.00
categoria = "Comida"




for produtos in listaProdutos:
    print(f"Nome {produtos['nome']}, {produtos['preco']}")

print('----------------')

for nome in listaNome:
    print(nome)


print('----------------')

controleDados.insereProduto(produto1, listaProdutos)


listaNome = GerenciadorDados.retornaListaNomeProduto(controleDados, listaProdutos, listaNome)

for produtos in listaProdutos:
    print(f"Nome {produtos['nome']}, {produtos['preco']}")

print('----------------')

for nome in listaNome:
    print(nome)

print('----------------')

if(validador.VerificaNomeProdutoExite(nome1, listaNome)):
    print(validador.MensagemNomeExiste(True))
else: 
    produto2 = {
        "nome": nome1,
        "peso": peso1, 
        "UN": un1,
        "preco": preco1, 
        "categoria": categoria
    }
    controleDados.insereProduto(produto2, listaProdutos)
    listaNome = GerenciadorDados.retornaListaNomeProduto(controleDados, listaProdutos, listaNome)

print('----------------')

for produtos in listaProdutos:
    print(f"Nome {produtos['nome']}, {produtos['preco']}")

print('----------------')

for nome in listaNome:
    print(nome)

print('----------------')