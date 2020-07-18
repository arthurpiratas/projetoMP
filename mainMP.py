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
        self.entradaPreco = Entry(self, textvariable = self.texto_valor, font = "Arial 15")
        self.spinboxUN = Spinbox(self, values = ('CM', 'CX', 'RL', 'KG', 'LT', 'M3'), wrap = True, state = 'readonly', font = "Arial 15")
        self.spinboxCategoria = Spinbox(self, values = ('Alimentos', 'Bebidas', 'Carnes', 'Frios', 'Frutas', 'Higiene', 'Legumes',  'Limpeza', 'Padaria', 'Verdura', 'Outros'), wrap = True, state = 'readonly', font = "Arial 15")

        # Definir Botão

        self.botaoSalvar = Button(self, text = "Salvar", command = self.salvar, font = "Arial 15")
        self.botaoLimpar = Button(self, text = "Limpar", command = self.limpar, font = "Arial 15")

        # Definir Layout 

        self.tituloFrame.grid(row = 0, column = 1)

        self.nomeProduto.grid(row = 1, column = 0)
        self.pesoProduto.grid(row = 2, column = 0)
        self.unPedido.grid(row = 3, column = 0)
        self.preco.grid(row = 4, column = 0)
        self.categoria.grid(row = 5, column = 0)

        self.entradaNome.grid(row = 1, column = 1)
        self.entradaPeso.grid(row = 2, column = 1)
        self.spinboxUN.grid(row = 3, column = 1)
        self.entradaPreco.grid(row = 4, column = 1)
        self.spinboxCategoria.grid(row = 5, column = 1)

        self.mensagemNomeVazio.grid(row = 6, column = 0)
        self.mensagemValorPeso.grid(row = 7, column = 0)
        self.mensagemValorPeso.grid(row = 8, column = 0)
        self.mensagemNomeExiste.grid(row = 9, column = 0)

        self.botaoSalvar.grid(row = 10, column = 0, sticky = W)
        self.botaoLimpar.grid(row = 10, column = 1, sticky = E)

        self.nomeProduto.focus()

    #função para salvar produto na lista
    def salvar(self):
        print("Salvou")
    
    #função para limpar campos
    def limpar(self):
        self.texto_nome.set('')
        self.texto_peso.set('')
        self.texto_valor.set('')
         

# Criando Frame Consulta Produto

class ConsultaProduto(Frame): 

    #herdar da classe Frame

    def __init__(self, master):
        super().__init__()

        # Definir variáveis referente label's

        self.texto_nome = StringVar()
        self.texto_peso = StringVar()
        self.texto_valor = StringVar()
        self.texto_UN = StringVar()
        self.texto_categoria = StringVar()
     

        # Definir Label

        self.tituloFrame = Label(self, text = "Consulta Produto", font = "Arial 20",  anchor = NW)

        self.nomeProduto = Label(self, text = "Nome : ", font = "Arial 15")
        self.pesoProduto = Label(self, text = "Peso : ", font = "Arial 15")
        self.unPedido = Label(self, text = "Unidade Medida : ", font = "Arial 15")
        self.preco = Label(self, text = "Preço : ", font = "Arial 15")
        self.categoria = Label(self, text = "Categoria : ", font = "Arial 15")


        # Definir Entry 

        self.entradaNome = Entry(self, textvariable = self.texto_nome, font = "Arial 15",  state = 'readonly') 
        self.entradaPeso = Entry(self, textvariable = self.texto_peso, font = "Arial 15", state = 'readonly') 
        self.entradapreco = Entry(self, textvariable = self.texto_valor, font = "Arial 15", state = 'readonly')
        self.entradaUN = Entry(self, textvariable = self.texto_UN, font = "Arial 15", state = 'readonly')
        self.entradaCategoria = Entry(self, textvariable = self.texto_categoria, font = "Arial 15", state = 'readonly')

        # Definir Botão

        self.botaoExcluir = Button(self, text = "Excluir", command = self.excluir, font = "Arial 15")
        self.botaoSelecionar = Button(self, text = "Selecionar", command = self.selecionar, font = "Arial 15")

        # Definir listBox

        self.listaBox = Listbox(self)

        # Definir Layout 

        self.tituloFrame.grid(row = 0, column = 1)

        self.nomeProduto.grid(row = 1, column = 0)
        self.pesoProduto.grid(row = 2, column = 0)
        self.unPedido.grid(row = 3, column = 0)
        self.preco.grid(row = 4, column = 0)
        self.categoria.grid(row = 5, column = 0)

        self.entradaNome.grid(row = 1, column = 1)
        self.entradaPeso.grid(row = 2, column = 1)
        self.entradaUN.grid(row = 3, column = 1)
        self.entradapreco.grid(row = 4, column = 1)
        self.entradaCategoria.grid(row = 5, column = 1)
        
        self.listaBox.grid(row = 6 , column = 0)

        self.botaoExcluir.grid(row = 6, column = 1)
        self.botaoSelecionar.grid(row = 6, column = 2)

         

    #função para salvar produto na lista
    def selecionar(self):
        print("Salvou")
    
    #função para limpar campos
    def excluir(self):
        self.limpar()
    
    def limpar(self):
        self.texto_nome.set('')
        self.texto_peso.set('')
        self.texto_valor.set('')
        self.texto_UN.set('')
        self.texto_categoria.set('')

# Criando função para chamar a tela de cadastro produto: 

def AparecerCadastroProduto(): 
    frameConsultaProduto.grid_forget()
    frameCadastroProduto.limpar()
    label_imagem.grid_forget()
    labelAux1.grid_forget()
    labelAux2.grid_forget()
    labelAux3.grid_forget()
    frameCadastroProduto.grid(row = 0, column = 0, sticky = W)

# Criando função para chamar a tela de cadastro produto: 

def AparecerConsultaProduto(): 
    frameCadastroProduto.grid_forget()
    frameConsultaProduto.limpar()
    label_imagem.grid_forget()
    labelAux1.grid_forget()
    labelAux2.grid_forget()
    labelAux3.grid_forget()
    frameConsultaProduto.grid(row = 0, column = 0, sticky = W)

# Criar função para chamar menu inicial

def AparecerMenuInicial(): 
    frameConsultaProduto.grid_forget()
    frameCadastroProduto.grid_forget()
    labelAux1.grid(row=0,column=0)
    labelAux2.grid(row=1,column=1)
    label_imagem.grid(row=3,column=1, sticky = "nsew")
    labelAux3.grid(row=2,column=0)

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
frameConsultaProduto = ConsultaProduto(TelaPrincipal)

# Criar um FileMenu para adicinar as opções do Menu opções Produto

opcaoMenu = Menu(menuPrincipal, tearoff = 0)
opcaoMenu.add_command(label = "Cadastrar Produto", command = AparecerCadastroProduto)
opcaoMenu.add_command(label = "Consultar Produto", command = AparecerConsultaProduto)
opcaoMenu.add_command(label = "Menu Inicial",  command = AparecerMenuInicial)

# Adcionando os menus do opcaoMenu no Menu de Opção Produto

menuPrincipal.add_cascade(label="Opções", menu = opcaoMenu)

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