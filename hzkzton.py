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
         n_r=p_vert
         n_v=p_bleu
         n_b=p_rouge

# modification du pixel de coordonnées x, y
         im_new.putpixel((x,y),(n_r,n_v,n_b))
         #((x,y),(n_r,n_v,n_b))
         rep=input("quelle couleur veut tu?rouge,vert,bleu")
         return rep:
            if rep==rouge:
            im_new.putpixel(x,y),(n_r)
            if rep==vert:
            im_new.putpixel(x,y),(n_v)
            if rep==bleu:
            im_new.putpixel(x,y),(n_b)


# affichage de l'image
im_new.save("sortie.png")
im_new.show()
