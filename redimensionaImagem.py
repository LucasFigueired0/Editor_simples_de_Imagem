from PIL import Image

img = Image.open("trindade.jpg")

tamanho = (250,250)

img.thumbnail(tamanho)

img.show()
# img.save("img2red.jpg")