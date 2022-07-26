import readchar
import replit

# Proyecto integrador 2------------------------------------------

# Instrucciones: Escribir un programa que corra un bucle infinito leyendo e 
# imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ 
# indicada como 

# !pip install readchar
# import readchar

# while True:
#   keypress = readchar.readkey()
#   if keypress == readchar.key.UP:
#     break
#   else:
#     print(keypress)


# Proyecto integrador 3------------------------------------------

# Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

i = 0
while True:
  keypress = readchar.readkey()
  if keypress == 'n':
    i += 1
    replit.clear()
    if i == 51:
      break
    for k in range(-1+i,i):
      print(k)
      continue
    

    
    
          
      
      

