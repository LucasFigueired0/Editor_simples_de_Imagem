import cv2
from PIL import Image, ImageTk

def transformar_desenho(arquivo):
    image = cv2.imread(arquivo)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverter = cv2.bitwise_not(grey_image)
    blur = cv2.GaussianBlur(inverter, (21,21),0)
    inverteBlur = cv2.bitwise_not(blur)
    imagem_final = cv2.divide(grey_image, inverteBlur, scale=256.0)

    pil_image = Image.fromarray(imagem_final)
    return pil_image