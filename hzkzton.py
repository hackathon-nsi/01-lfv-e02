from PIL import Image
#from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
im = Image.open('hunter-x-hunter.jpg')

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (660, 370), (128, 128, 128))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
for x in range(660) :
    for y in range (370):
         pixel = im.getpixel((x,y))

# valeurs des couleurs rouge, vert, bleu
         p_rouge = pixel[0]
         p_vert =  pixel[1]
         p_bleu =  pixel[2]
         n_r=v
         n_v=b
         n_b=r

# modification du pixel de coordonnées x, y
         im_new.putpixel((x,y),(p_rouge,p_vert,p_bleu))
         ((x,y),(n_r,n_v,n_b))


# affichage de l'image
im_new.save("sortie.png")
im_new.show()
