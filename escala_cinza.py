from PIL import Image

def grayscale(colored):
    w,h = colored.size

    img = Image.new("RGB",(w,h))
    
    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            img.putpixel((x,y), (lum,lum,lum))
    
    return img

