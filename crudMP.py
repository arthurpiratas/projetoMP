import json

class GerenciadorDados: 

    #Função para ler arquivo Json
    def ler_json(self):
        with open('meu_arquivo.json', 'r', encoding='utf-8') as f: 
            return  json.load(f)

    def escrever_json(self, lista):
        with open('meu_arquivo.json', 'w') as f:
            json.dump(lista, f)

    #Função para inserir produto na lista
    def insereProduto(self, produto, listaProdutos ):
        listaProdutos.append(produto)

    #Função para remover Produto
    def removeProduto(self, produto, listaProdutos):
        listaProdutos.remove(produto)
    
    #Função para buscar produto
    def buscaProduto(self, nomeProduto, listaProduto):
        for cont in range(0,len(listaProduto)):
            if(nomeProduto.upper() == listaProduto[cont]['nome'].upper()):
                return   {'nome': listaProduto[cont]['nome'], 'peso': listaProduto[cont]['peso'], 'UN': listaProduto[cont]['UN'], 'preco': listaProduto[cont]['preco'], 'categoria': listaProduto[cont]['categoria']}

    # retorna lista de nome de produtos 
    def retornaListaNomeProduto(self, listaProduto, listaNomeProduto):
        listaNomeProduto.clear()

        for produto in listaProduto:
            listaNomeProduto.append(produto['nome'].upper())
        
        return listaNomeProduto
   
   