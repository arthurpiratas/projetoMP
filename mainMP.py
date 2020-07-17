#Importanto bibliotecas e classes que serão usadas. 

from ValidadoresMP import Validadores
from crudMP import GerenciadorDados
import json
from tkinter import *

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

# Criar um FileMenu para adicinar as opções do Menu opções Produto

opcaoMenu = Menu(menuPrincipal)
opcaoMenu.add_command(label = "Cadastrar Produto")
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