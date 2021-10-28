
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import numpy as np
from PIL import ImageTk, Image

janela_inicial = Tk()

menubar = Menu(janela_inicial)

def tela_principal():
    esconderFrames()
    tela_principal.pack(fill="both", expand=1)

def tela_das_receitas():
    esconderFrames()
    tela_das_receitas.pack(fill="both", expand=1)

def esconderFrames():
    tela_principal.pack_forget()
    tela_das_receitas.pack_forget()

bt_entrar = Button(janela_inicial, width=30, text="Entrar", bg="red", command=tela_principal)
bt_entrar.place(x = 500,y = 650)

bt_cadastrar = Button(janela_inicial, width=30, text="Cadastrar", bg="red")
bt_cadastrar.place(x = 220,y = 650)

titulo = Label(janela_inicial, text = "MINHAS RECEITAS", bg="#228B22")
titulo.pack(side = TOP, fill=X)

botaoSair_inicial = Button(janela_inicial, width=30, text="Sair", bg="red", command=janela_inicial.destroy)
botaoSair_inicial.place(x = 800,y = 650)

janela_inicial.iconbitmap("imagens/icon.ico")
janela_inicial.title("Minhas Receitas")
janela_inicial.geometry("1300x720+60+20")

login_lab = Label(janela_inicial, text="Login", width = 30, height=4,bg = 'white')
login_lab.place(x = 30, y = 200)

senha_lab = Label(janela_inicial, text="Senha", width = 30, height=4,bg = 'white')
senha_lab.place(x = 30, y = 320)

login_inicial = Label(janela_inicial, text="", width = 130, height=4,bg = 'white')
login_inicial.place(x = 300, y = 200)

senha_inicial = Label(janela_inicial, text="", width = 130, height=4,bg = 'white')
senha_inicial.place(x = 300, y = 320)



imagem = ImageTk.PhotoImage(Image.open("imagens/download.jpeg"))
imagemL = Label(image=imagem)


tela_principal = Frame(janela_inicial, width=900, height=700, bg='gray')

pesquisar = Label(tela_principal, text="", width = 150, bg = 'white')
pesquisar.place(x = 40, y = 40)

bt_entrar = Button(tela_principal, width=8, text="Entrar", bg="red")
bt_entrar.place(x = 1120, y =37)


cat_3 = Button(tela_principal, text="CATEGORIA 3", width = 40, height=2, bg = 'red', command=tela_das_receitas)
cat_3.place(x = 40, y = 600,)

cat_2 = Button(tela_principal, text="CATEGORIA 2", width = 40, height=2, bg = 'red', command=tela_das_receitas)
cat_2.place(x = 40, y = 500,)

cat_1 = Button(tela_principal, text="CATEGORIA 1", width = 40, height=2 ,bg = 'red', command=tela_das_receitas )
cat_1.place(x = 40, y = 400,)

cat_4 = Button(tela_principal, text="CATEGORIA 4", width = 40, height=2, bg = 'red', command=tela_das_receitas)
cat_4.place(x = 500, y = 400,)

cat_5 = Button(tela_principal, text="CATEGORIA 5", width = 40, height=2, bg = 'red', command=tela_das_receitas )
cat_5.place(x = 500, y = 500,)

cat_6 = Button(tela_principal, text="CATEGORIA 6", width = 40, height=2 ,bg = 'red', command=tela_das_receitas)
cat_6.place(x = 500, y = 600,)

bt_editar = Button(tela_principal, text="EDITAR", width = 40, height=2 ,bg = 'red')
bt_editar.place(x = 900, y = 550,)

bt_apagar = Button(tela_principal, text="DELETAR", width = 40, height=2 ,bg = 'red', )
bt_apagar.place(x = 900, y = 450,)

tela_das_receitas = Frame(janela_inicial, width=900, height=700, bg='brown')

titulo_receita = Label(tela_das_receitas, text="", width = 170, height=4,bg = 'white')
titulo_receita.place(x = 60, y = 40)

descr = Label(tela_das_receitas, text="", width = 170, height=30,bg = 'white')
descr.place(x = 60, y = 150)

bt_editar_1 = Button(tela_das_receitas, text="EDITAR", width = 20, height=2 ,bg = 'red')
bt_editar_1.place(x = 900, y = 630,)

bt_apagar_1 = Button(tela_das_receitas, text="DELETAR", width = 20, height=2 ,bg = 'red', )
bt_apagar_1.place(x = 1100, y = 630,)

bt_voltar_1 = Button(tela_das_receitas, text="VOLTAR", width = 20, height=2 ,bg = 'red',command=tela_principal)
bt_voltar_1.place(x = 700, y = 630,)


janela_inicial.mainloop()