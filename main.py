from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from PIL import Image, ImageTk
from escala_cinza import grayscale
from desenho import transformar_desenho
from utils import *
# ------------
import cv2

tituloTeste = "Selecionar arquivo"
imagem_salvar = ""
img = ""
efeito1 = ""
imagem = ""
img_cinza = ""
option = ""
cont = 0


def telaPrincipal():
    # Função para pegar imagem----------------------------------------------------------
    def pegarArquivo():
        global imagem
        imagem = pegaArquivo()
        exibeImagem("inicio", imagem)

    def guardarImagem(option, imagemEfeito):
        global cont
        if (option == ""):
            aviso = Label(text="Nenhuma imagem selecionada!")
        elif option == "cinza" or option=="desenho":
            imagemEfeito.save(out_file(f"Imagem_{cont}.jpg"))
            cont = + 1

    def exibeImagem(opcao, imagem):
        global imagem_salvar
        global option
       

        if (opcao == "inicio"):
            # imagem0 = pegaArquivo()
            tituloTeste = "Selecionar outro arquivo"
            print(tituloTeste)

            # imagem = pegaArquivo()
            img = processaImagem(imagem, 500, 500)

            frameImagem.destroy()

            frameImagem1 = Frame(tela,
                                 width=700,
                                 height=400,
                                 )
            frameImagem1.grid(column=2, row=0, pady=20)
            label_imagem = Label(frameImagem1, image=img, width=700,
                                 height=400).grid().grid(column=2, row=0, padx=20)

        elif (opcao == "cinza"):
            
            global img_cinza
            global option
            option = "cinza"
            img_cinza = igmCinza(imagem)

            imagem_salvar = img_cinza

            img_cinza2 = ImageTk.PhotoImage(img_cinza)

            print("ImagemCinza: "+imagem)

            frameImagem2 = Frame(tela,
                                 width=700,
                                 height=400,
                                 )
            frameImagem2.grid(column=2, row=0, pady=20)
            label_imagem = Label(frameImagem2, image=img_cinza2, width=700,
                                 height=400).grid().grid(column=2, row=0, padx=20)
        else:
            #ERRO AQUI
            option = "desenho"
            imagem_desenho = imgDesenho(imagem)

            imagem_salvar = imagem_desenho

            img_desenho = ImageTk.PhotoImage(imagem_desenho)
            frameImagem3 = Frame(tela,
                                 width=700,
                                 height=400,
                                 )
            frameImagem3.grid(column=2, row=0, pady=20)
            label_imagem = Label(frameImagem3, image=img_desenho, width=700,
                                 height=400).grid().grid(column=2, row=0, padx=20)

    # tela principal
    tela = Tk()
    tela.title("Aplicação-Imagens")
    tela.configure(background="#89709C")
    tela.geometry("1000x550")
    tela.minsize(1000, 550)

    # -----------------------Itens reserva------------------------
    label_imagem = Label(tela, width=0)

    # ------------------------------------------------------------
    # seção de imagens e botões
    frameBotao = Frame(tela,  width=141)
    frameBotao.grid(column=0, row=0, padx=10, pady=15)
    frameBotao.configure(background="#89709C")

    txt_seleciona_efeito = Label(
        frameBotao, text="Selecione um efeito", font="-weight bold", foreground='white')
    txt_seleciona_efeito.grid(column=0, row=0)
    txt_seleciona_efeito.configure(background="#89709C")

    # botao 1             framePai txt  img   efeito com

    btnEfeito01 = Button(frameBotao, text="Escala de cinza",
                         command=lambda: exibeImagem("cinza", imagem),
                         width=25,
                         height=5).grid(column=0, row=1, padx=10)

    # botao 2
    btnEfeito02 = Button(frameBotao, text="Transformar imagem em desenho",
                         command=lambda: exibeImagem("desenho", imagem),
                         width=25,
                         height=5).grid(column=0, row=2, padx=10)

    # botao 3
    btnEfeito02 = Button(frameBotao, text="Mostrar original",
                         command=lambda: exibeImagem("inicio", imagem),
                         width=25,
                         height=5).grid(column=0, row=3, padx=10)

    # Seção onde fica a imagem
    frameImagem = Frame(tela,
                        width=700,
                        height=400,
                        )

    frameImagem.grid(column=2, row=0, pady=20)

# Seção onde ficarão os botões
    frameBotoesinferiores = Frame(master=tela, width=548, height=60)
    frameBotoesinferiores.grid(column=2, row=2, pady=10)
    frameBotoesinferiores.configure(background="#89709C")

    # Botão para selecionar arquivo
    btnSelecionaArquivo = Button(master=frameBotoesinferiores, text=tituloTeste,
                                 command=pegarArquivo,
                                 width=20,
                                 height=2)

    btnSelecionaArquivo.grid(column=0, row=0, padx=20)

    # Botão para aplicar efeito
    salvarArquivo = Button(master=frameBotoesinferiores, text="Salvar imagem",
                           command=lambda: guardarImagem(
                               option, imagem_salvar),
                           width=20,
                           height=2)

    salvarArquivo.grid(column=1, row=0, padx=20)

    tela.mainloop()


telaPrincipal()

print("Imagem cinza ", img_cinza)
