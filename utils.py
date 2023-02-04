from tkinter import *
from tkinter.filedialog import *
from tkinter import filedialog
from PIL import Image, ImageTk
from escala_cinza import grayscale
from desenho import transformar_desenho
import os
# ------------
import cv2


def out_file(filename):
    OUTPUT_DIR = askdirectory()
    return os.path.join(OUTPUT_DIR, filename)

def processaImagem(imagem, alt, larg):
    img = Image.open(imagem)
    tam = (alt, larg)
    img.thumbnail(tam)
    return ImageTk.PhotoImage(img)


def igmCinza(imagem):
    img = Image.open(imagem)
    img2 = grayscale(img)
    tam = (500,500)
    img2.thumbnail(tam)
    
    return  img2
    # ImageTk.PhotoImage(img2)

def imgDesenho(imagem):
    img = transformar_desenho(imagem)
    tam = (500,500)
    img.thumbnail(tam)
    return img

def pegaArquivo():
    imagem = askopenfile()
    print(imagem)
    return str(imagem.name)


def botao(framePai, texto, imagem, efeito, comando, largura, altura, coluna, linha, pad):
    return Button(framePai, image="", text=texto,
                  command=comando,
                  width=largura,
                  height=altura).grid(column=coluna, row=linha, padx=pad)



