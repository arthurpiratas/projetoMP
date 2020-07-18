class Validadores: 

    #Função para validar se o valor é um Float
    def validaValorFloat(self, valor):
        if((type(valor) == type(1.0)) or (type(valor) == type(1))):
            if(valor >= 1):
                return True
            else:
                return False
        else:
            return False

    #Função para informar erro do valor
    def MensagemValorFloat(self, boleano):
        if(boleano == False): 
            return "O Campo de Preco deve ser um numero real ou inteiro e maior que 0(zero)"
    
    #Função para informar erro do valor
    def MensagemPesoFloat(self, boleano):
        if(boleano == True): 
            return "O Campo de Peso deve ser um numero real ou inteiro"
   
    #Função para verificar se um nome já foi cadastrado
    def VerificaNomeProdutoExite(self, nome, listaNome):
        if (nome.upper()) in listaNome: 
            return True
        else: 
            return False

    #Função para informar erro nome já existe/cadastrado
    def MensagemNomeExiste(self, boleano):
        if(boleano == True): 
            return "O Nome do Produto já foi cadastrado"

    def VerificaNomeVazio(self, nome):
        if nome == "": 
            return True
        else: 
            return False
    
    #Função para informar que o campo não foi preenchido
    def MensagemCampoNaoFoiPreenchido(self, boleano):
        if(boleano == True): 
            return "O Nome do Produto já foi cadastrado"

    #verfica se a lista possui registro
    def VerificaListaVazia(self, listaProduto):
        if(len(listaProduto) > 0): 
            return False
        else: 
            return True