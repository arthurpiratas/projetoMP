import json

class GerenciadorDados: 

    #Função para ler arquivo Json
    def ler_json(self):
        with open('meu_arquivo.json', 'r', encoding='utf-8') as f: 
            return  json.load(f)

    #Função para inserir produto na lista
    def insereProduto(self, produto, listaProdutos ):
        listaProdutos.append(produto)

    #Função para remover Produto
    def removeProduto(self, produto, listaProdutos):
        listaProdutos.remove(produto)
    
    #Função para buscar produto
    def buscaProduto(self, nomeProduto, listaProduto):
        for cont in range(0,len(listaProduto)):
            if(nomeProduto == listaProduto[cont]['nome']):
                return   {'nome': listaProduto[cont]['nome'], 'UN': listaProduto[cont]['UN'], 'preco': listaProduto[cont]['preco'], 'categoria': listaProduto[cont]['categoria'], 'peso': listaProduto[cont]['peso']}

    # retorna lista de nome de produtos 
    def retornaListaNomeProduto(self, listaProduto, listaNomeProduto):
        listaNomeProduto.clear()

        for produto in listaProduto:
            listaNomeProduto.append(produto['nome'])
        
        return listaNomeProduto
   
   