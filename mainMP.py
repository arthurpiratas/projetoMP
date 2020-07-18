#Importanto bibliotecas e classes que serão usadas. 

from ValidadoresMP import Validadores
from crudMP import GerenciadorDados
import json
from tkinter import *

# Criando frame Cadastro Produto 

class CadastroProduto(Frame): 

    #herdar da classe Frame

    def __init__(self, master):
        super().__init__()

        # Definir variáveis referente label's

        self.texto_nome = StringVar()
        self.texto_peso = StringVar()
        self.texto_valor = StringVar()

        # Definir variáveis para mensagens: 

        self.texto_NomeVazio = StringVar()
        self.texto_NomeJaExiste = StringVar()
        self.texto_ErroPeso = StringVar()
        self.texto_ErroValor = StringVar()        

        # Definir Label

        self.tituloFrame = Label(self, text = "Cadastro Produto", font = "Arial 20",  anchor = NW)

        self.nomeProduto = Label(self, text = "Nome : ", font = "Arial 15")
        self.pesoProduto = Label(self, text = "Peso : ", font = "Arial 15")
        self.unPedido = Label(self, text = "Unidade Medida : ", font = "Arial 15")
        self.preco = Label(self, text = "Preço : ", font = "Arial 15")
        self.categoria = Label(self, text = "Categoria : ", font = "Arial 15")

        # Definir Label Mensagens de Erro

        self.mensagemNomeVazio = Label(self, textvariable = self.texto_NomeVazio)
        self.mensagemValorPeso = Label(self, textvariable = self.texto_NomeJaExiste)
        self.mensagemValorPeso = Label(self, textvariable = self.texto_ErroPeso)
        self.mensagemNomeExiste = Label(self, textvariable = self.texto_ErroValor)

        # Definir Entry 
        self.entradaNome = Entry(self, textvariable = self.texto_nome, font = "Arial 15") 
        self.entradaPeso = Entry(self, textvariable = self.texto_peso, font = "Arial 15") 
        self.entradaCategoria = Entry(self, textvariable = self.texto_valor, font = "Arial 15")
        self.spinboxUN = Spinbox(self, values = ('CM', 'CX', 'RL', 'KG', 'LT', 'M3'), wrap = True, state = 'readonly', font = "Arial 13")
        self.spinboxCategoria = Spinbox(self, values = ('Alimentos', 'Bebidas', 'Carnes', 'Frios', 'Frutas', 'Higiene', 'Legumes',  'Limpeza', 'Padaria', 'Verdura', 'Outros'), wrap = True, state = 'readonly', font = "Arial 13")

        # Definir Botão

        self.botaoSalvar = Button(self, text = "Salvar", command = self.salvar)
        self.botaoLimpar = Button(self, text = "Limpar", command = self.limpar)

        # Definir Layout 

        self.tituloFrame.grid(row = 0, column = 1)

        self.nomeProduto.grid(row = 1, column = 0)
        self.pesoProduto.grid(row = 2, column = 0)
        self.unPedido.grid(row = 3, column = 0)
        self.preco.grid(row = 5, column = 0)
        self.categoria.grid(row = 7, column = 0)

        self.entradaNome.grid(row = 1, column = 1)
        self.entradaPeso.grid(row = 2, column = 1)
        self.entradaCategoria.grid(row = 3, column = 1)
        self.spinboxUN.grid(row = 5, column = 1)
        self.spinboxCategoria.grid(row = 7, column = 1)

        self.mensagemNomeVazio.grid(row = 8, column = 0)
        self.mensagemValorPeso.grid(row = 9, column = 0)
        self.mensagemValorPeso.grid(row = 10, column = 0)
        self.mensagemNomeExiste.grid(row = 11, column = 0)

        self.botaoSalvar.grid(row = 12, column = 0, sticky = W)
        self.botaoLimpar.grid(row = 14, column = 1, sticky = E)

    #função para salvar produto na lista
    def salvar(self):
        print("Salvou")
    
    #função para limpar campos
    def limpar(self):
        self.texto_nome.set('')
        self.texto_peso.set('')
        self.texto_valor.set('')
         
        
    


# Criando Frame Consulta Produto

# Criando função para chamar a tela de cadastro produto: 

def AparecerCadastroProduto(): 
    #frameMorada.grid_forget()
    label_imagem.grid_forget()
    frameCadastroProduto.grid(row = 0, column = 0, sticky = W)

# Definindo propiedades do layout inicial

TelaPrincipal = Tk()
TelaPrincipal.title("Mercado Pirata")
TelaPrincipal.geometry('640x400+450+150')
TelaPrincipal.iconbitmap("Imagens/icon.ico")
img = PhotoImage(file="Imagens/Fundo.png")
TelaPrincipal.resizable(0,0)

# Definindo Menu 

menuPrincipal = Menu(TelaPrincipal)
TelaPrincipal.config(menu = menuPrincipal)

# Definir Frames 

frameCadastroProduto = CadastroProduto(TelaPrincipal) 

# Criar um FileMenu para adicinar as opções do Menu opções Produto

opcaoMenu = Menu(menuPrincipal, tearoff = 0)
opcaoMenu.add_command(label = "Cadastrar Produto", command = AparecerCadastroProduto)
opcaoMenu.add_command(label = "Consultar Produto")

# Adcionando os menus do opcaoMenu no Menu de Opção Produto

menuPrincipal.add_cascade(label="Opções Produto", menu = opcaoMenu)

# Labels criadas para centralizar imagem do menu
labelAux1 = Label(TelaPrincipal, text="                                                                     ")
labelAux2 = Label(TelaPrincipal, text="                                                                     ")
labelAux3 = Label(TelaPrincipal, text="                                                                     ")
label_imagem = Label(TelaPrincipal, image=img)





# Layout 

# Layout Menu inicial
labelAux1.grid(row=0,column=0)
labelAux2.grid(row=1,column=1)
label_imagem.grid(row=3,column=1, sticky = "nsew")
labelAux3.grid(row=2,column=0)





TelaPrincipal.mainloop()