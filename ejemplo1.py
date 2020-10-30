import cv2 #Biblioteca para el manejo de imágenes

imagen = cv2.imread('imagen.jpeg')#leer el archivo  (ORDEN: bgr)
imegen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB) #Cambia orden
print(imagen.shape) #longitud del archivo
#print(imagen[0,0])#primer pixel
print(imagen[0][0][0]) #valor en específico 

#modificar tamaño
imagen = cv2.resize(imagen,(256,256))
#solo m y l
cv2.imwrite('resizeimagen.jpeg',imagen)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
 
