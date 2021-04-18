from PIL import Image,ImageEnhance

# ouvrir une image hébergée sur internet
im = Image.open("hunterxhunter2.jpg")

im_new = Image.open("hunter-x-hunter.jpg")

# informations sur l'image
print(im.format, im.size, im.mode)

en = ImageEnhance.Color(im)
im = en.enhance(0.0)

en = ImageEnhance.Contrast(im_new)
im_new = en.enhance(2.7)

# taille de l'image
width, height = im.size


def gris():
    for y in range(92, 277):
        for x in range(165, 495):
            pixel = im.getpixel((x, y))
            im_new.putpixel((x, y), pixel)
    im_new.show()


# affichage de l'image
print(gris())
