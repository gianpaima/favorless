from PIL import Image 


#cargar las dos imagenes desde el directorio donde estoy ejecutando el Script

# Abrir  img  1 

im1 = Image.open("leon.jpg")

# Abir img 2 

im2 = Image.open("leon2.jpg")

# crear una imagen de Fondo que  contiene las dos imagenes

salida  =  Image.new ("RGB", (640,480),(0,0,255)) # imagen de 640*480 de fondo blanco

# redimensionar cada imagenpng para que ocupe el lugar indicado

a = im1.resize((salida.size[0]/2 - 1, salida.size[1]))
b = im2.resize((salida.size[0]/2 - 1, salida.size[1]))

#Ahora copiar cada imagen a la imagen de salida

salida.paste(a,(0,0))
salida.paste(b,(a.size[0] + 2,0))

salida.save("salida.jpg", "JPEG")
salida.save("salida2.jpg",optimize=True)




