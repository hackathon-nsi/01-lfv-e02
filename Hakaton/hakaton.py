from PIL import Image


# ouvrir une image hébergée sur internet
im = Image.open("Hunter-x-Hunter.jpg")

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (512, 512), (128, 128, 128))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
pixel = im.getpixel((x, y))

# valeurs des couleurs rouge, vert, bleu
p_rouge = pixel[0]
p_vert =  pixel[1]
p_bleu =  pixel[2]

# modification du pixel de coordonnées x, y
im.putpixel((x,y),(r,g,b))

# affichage de l'image
display(im)