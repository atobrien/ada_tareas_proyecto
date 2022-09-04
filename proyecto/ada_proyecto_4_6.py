[Probar_en]:https://replit.com/@AnthonyO6/PersonalClassicPoints#main.py
    
# Proyecto integrador 4------------------------------------------
    
# Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.

# import readchar
# import replit
# import random

# def createMap(path):
#   """
#   This saves the map as a string vector:
  
#   open file reader
#   read file into content
#   close file reader
#   turn the contents into single characters
#   remove the new line characrters '\n'
#   remove the white spaces left behind 
#   """
#   with open(path, 'r') as file:
#     contents = file.read()  
#   # f = open(path)
#   # contents = f.read()
#   # f.close()
#   # https://www.pythonpool.com/python-remove-newline-from-list/ (used to remove \n)
# # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings (used to remove white spaces)
#   res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]
#   return res

# def createMatrix(rowCount, colCount, dataList):   
#     """
#     This turns the string map to a matrix
#     """
#     mat = []
#     for i in range(rowCount):
#         rowList = []
#         for j in range(colCount):
#             if dataList[j] not in mat:          #https://stackoverflow.com/questions/40120892/creating-a-matrix-in-python-without-numpy
#               rowList.append(dataList[rowCount * i + j])
#         mat.append(rowList)
#     return mat 

# def matrixMap():
#   """
#   This registers the string map and then 
#   turns it into a matrix
#   From here we can update the matrix before 
#   printing it
#   """
#   alpha = createMap(path = "mydata" + str(random.randint(1,4)) + ".txt")
#   mat = createMatrix(21,21,alpha) 
#   return(mat)


# def movements():
#   """
#   This will:
#   Save matrix map to mat 2 
#   Then save the location of ther person into p_location
#   Then update P location into matrix first at (0,0)
#   and then with "." and then with 'P' in
#   one direction relative to the key press 
#   """
#   # Iniciar en P en (0,0)
#   p_location = list([0,0])
#   mat2 = matrixMap()
#   mat2[0][0] = 'P'
#   # test = None

#   while True:
#     kp = readchar.readkey()
    
#     if kp == 'D' and mat2[p_location[0]][p_location[1]+1] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]][p_location[1]+1] = 'P' 
#       p_location[1] += 1  
#     elif kp == 'S' and mat2[p_location[0]+1][p_location[1]] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]+1][p_location[1]] = 'P'   
#       p_location[0] += 1  
#     elif kp == 'A' and mat2[p_location[0]][p_location[1]-1] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]][p_location[1]-1] = 'P' 
#       p_location[1] -= 1  
#     elif kp == 'W' and mat2[p_location[0]-1][p_location[1]] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]-1][p_location[1]] = 'P'
#       p_location[0] -= 1  
#     elif kp == 'Q':
#       return kp
#     elif kp == 'D' and mat2[p_location[0]][p_location[1]+1] == '#':
#       replit.clear()
#       pass
#     elif kp == 'S' and mat2[p_location[0]+1][p_location[1]] == '#':
#       replit.clear()
#       pass
#     elif kp == 'A' and mat2[p_location[0]][p_location[1]-1] == '#':
#       replit.clear()
#       pass
#     elif kp == 'W' and mat2[p_location[0]-1][p_location[1]] == '#':
#       replit.clear()
#       pass
#     # testing index error boundries not solved as yet
#     # elif p_location in [1,0]:
#     #   #global test
#     #   test = 'D'
#     #   #continue

#     for line in mat2:
#       mapst =  '  '.join(map(str, line)) 
#       print(mapst)   
#       # print(p_location)
#       # print(test)

# def main(): 
#   # print map once 
#   mat3 = matrixMap()
#   mat3[0][0] = 'P'
#   for line in mat3:
#     mapst =  '  '.join(map(str, line))
#     print(mapst)
    
#   # print movement on map
#   movements()

# if __name__ == "__main__":
#     main()


# # Proyecto integrador 5------------------------------------------

# # Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.

# import readchar
# import replit
# import random
# from dataclasses import dataclass, field

# @dataclass
# class Juego:
#   p_location: list = field(default_factory=lambda: [0,0])
#   rowCount: int = 21
#   colCount: int = 21
  
#   def path():
#     path = "mydata" + str(random.randint(1,4)) + ".txt"
#     return path
    
#   with open(path(), 'r') as file:
#     contents = file.read()   
#   res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]

#   def createMatrix(self):   
#       mat = []
#       for i in range(self.rowCount):
#           rowList = []
#           for j in range(self.colCount):
#               if self.res[j] not in mat:         
#                 rowList.append(self.res[self.rowCount * i + j])
#           mat.append(rowList)
#       return mat
  
#   def movements(self):
#     mat2 = self.createMatrix()
#     mat2[0][0] = 'P'

#     while True:
#       kp = readchar.readkey()

#       if self.p_location[0]+1 == 21:
#         continue

#       if self.p_location[1]+1 == 21:
#         continue

#       if self.p_location[1]-1 == -2:
#         continue

#       if self.p_location[0]-1 == -2:
#         continue     
      
#       if kp == 'D' and mat2[self.p_location[0]][self.p_location[1]+1] != '#':
#         replit.clear()
#         mat2[self.p_location[0]][self.p_location[1]] = '.'
#         mat2[self.p_location[0]][self.p_location[1]+1] = 'P' 
#         self.p_location[1] += 1  
#       elif kp == 'S' and mat2[self.p_location[0]+1][self.p_location[1]] != '#':
#         replit.clear()
#         mat2[self.p_location[0]][self.p_location[1]] = '.'
#         mat2[self.p_location[0]+1][self.p_location[1]] = 'P'   
#         self.p_location[0] += 1  
#       elif kp == 'A' and mat2[self.p_location[0]][self.p_location[1]-1] != '#':
#         replit.clear()
#         mat2[self.p_location[0]][self.p_location[1]] = '.'
#         mat2[self.p_location[0]][self.p_location[1]-1] = 'P' 
#         self.p_location[1] -= 1  
#       elif kp == 'W' and mat2[self.p_location[0]-1][self.p_location[1]] != '#':
#         replit.clear()
#         mat2[self.p_location[0]][self.p_location[1]] = '.'
#         mat2[self.p_location[0]-1][self.p_location[1]] = 'P'
#         self.p_location[0] -= 1  
#       elif kp == 'Q':
#         return kp
#       elif kp == 'D' and mat2[self.p_location[0]][self.p_location[1]+1] == '#':
#         replit.clear()
#         pass
#       elif kp == 'S' and mat2[self.p_location[0]+1][self.p_location[1]] == '#':
#         replit.clear()
#         pass
#       elif kp == 'A' and mat2[self.p_location[0]][self.p_location[1]-1] == '#':
#         replit.clear()
#         pass
#       elif kp == 'W' and mat2[self.p_location[0]-1][self.p_location[1]] == '#':
#         replit.clear()
#         pass
  
#       for line in mat2:
#         mapst =  '  '.join(map(str, line)) 
#         print(mapst)   

#   def main(self): 
#     mat3 = self.createMatrix()
#     mat3[0][0] = 'P'
    
#     for line in mat3:
#       mapst =  '  '.join(map(str, line))
#       print(mapst)

#     self.movements()
  
# if __name__ == "__main__":
#   juego = Juego()
#   print(juego.main())


## Parte 2

# En lugar de almacenar el mapa en el mismo código, podemos guardarlo en archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera línea del archivo, de esta manera los componentes de la aplicación estarán separados y podremos mejorar la experiencia del juego.

# import readchar
# import replit
# import random
# from dataclasses import dataclass, field

# @dataclass
# class Juego():
#   p_location: list = field(default_factory=lambda: [0,0])
#   rowCount: int = 21
#   colCount: int = 21
  
#   def movements(self, matrix):

#     while True:
#       kp = readchar.readkey()

#       if self.p_location[0]+1 == 21:
#         continue

#       if self.p_location[1]+1 == 21:
#         continue

#       if self.p_location[1]-1 == -2:
#         continue

#       if self.p_location[0]-1 == -2:
#         continue     
      
#       if kp == 'D' and matrix[self.p_location[0]][self.p_location[1]+1] != '#':
#         replit.clear()
#         matrix[self.p_location[0]][self.p_location[1]] = '.'
#         matrix[self.p_location[0]][self.p_location[1]+1] = 'P' 
#         self.p_location[1] += 1  
#       elif kp == 'S' and matrix[self.p_location[0]+1][self.p_location[1]] != '#':
#         replit.clear()
#         matrix[self.p_location[0]][self.p_location[1]] = '.'
#         matrix[self.p_location[0]+1][self.p_location[1]] = 'P'   
#         self.p_location[0] += 1  
#       elif kp == 'A' and matrix[self.p_location[0]][self.p_location[1]-1] != '#':
#         replit.clear()
#         matrix[self.p_location[0]][self.p_location[1]] = '.'
#         matrix[self.p_location[0]][self.p_location[1]-1] = 'P' 
#         self.p_location[1] -= 1  
#       elif kp == 'W' and matrix[self.p_location[0]-1][self.p_location[1]] != '#':
#         replit.clear()
#         matrix[self.p_location[0]][self.p_location[1]] = '.'
#         matrix[self.p_location[0]-1][self.p_location[1]] = 'P'
#         self.p_location[0] -= 1  
#       elif kp == 'Q':
#         return kp
#       elif kp == 'D' and matrix[self.p_location[0]][self.p_location[1]+1] == '#':
#         replit.clear()
#         pass
#       elif kp == 'S' and matrix[self.p_location[0]+1][self.p_location[1]] == '#':
#         replit.clear()
#         pass
#       elif kp == 'A' and matrix[self.p_location[0]][self.p_location[1]-1] == '#':
#         replit.clear()
#         pass
#       elif kp == 'W' and matrix[self.p_location[0]-1][self.p_location[1]] == '#':
#         replit.clear()
#         pass

#       for line in matrix:
#         mapst =  '  '.join(map(str, line)) 
#         print(mapst)          

# @dataclass
# class Archivo(Juego):

#   def path():
#     path = "mydata" + str(random.randint(1,4)) + ".txt"
#     return path
    
#   with open(path(), 'r') as file:
#     contents = file.read()   
#   res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]

#   def createMatrix(self):   
#       mat = []
#       for i in range(self.rowCount):
#           rowList = []
#           for j in range(self.colCount):
#               if self.res[j] not in mat:         
#                 rowList.append(self.res[self.rowCount * i + j])
#           mat.append(rowList)
#       return mat

#   def main(self): 
#     mat3 = self.createMatrix()
#     mat3[0][0] = 'P'
    
#     for line in mat3:
#       mapst =  '  '.join(map(str, line))
#       print(mapst)

#     mat2 = self.createMatrix()
#     mat2[0][0] = 'P'

#     Juego.movements(self,matrix=mat2)

# if __name__ == "__main__":
#   juego = Archivo()
#   juego.main()   


# # Proyecto integrador 6------------------------------------------

# 1. Reescribir la función que convierte el laberinto de cadena a matriz para que en vez de usar un bucle, haga uso de la función map

# 2. Reescribir la función que lee el mapa usando la función readlines para leerlo todo en una sola operación, cargar las coordenadas y usar reduce para concatenar las filas leídas en una sola cadena, en otras palabras sustituir el bucle de lectura del mapa en forma de candena para usar la función reduce.


import readchar, replit, random, functools as ft
from dataclasses import dataclass, field


@dataclass
class Juego():
  p_location: list = field(default_factory=lambda: [0,0])
  rowCount: int = 21
  colCount: int = 21
  
  def movements(self, matrix):

    while True:
      kp = readchar.readkey()

      if self.p_location[0]+1 == 21:
        continue

      if self.p_location[1]+1 == 21:
        continue

      if self.p_location[1]-1 == -2:
        continue

      if self.p_location[0]-1 == -2:
        continue     
      
      if kp == 'D' and matrix[self.p_location[0]][self.p_location[1]+1] != '#':
        replit.clear()
        matrix[self.p_location[0]][self.p_location[1]] = '.'
        matrix[self.p_location[0]][self.p_location[1]+1] = 'P' 
        self.p_location[1] += 1  
      elif kp == 'S' and matrix[self.p_location[0]+1][self.p_location[1]] != '#':
        replit.clear()
        matrix[self.p_location[0]][self.p_location[1]] = '.'
        matrix[self.p_location[0]+1][self.p_location[1]] = 'P'   
        self.p_location[0] += 1  
      elif kp == 'A' and matrix[self.p_location[0]][self.p_location[1]-1] != '#':
        replit.clear()
        matrix[self.p_location[0]][self.p_location[1]] = '.'
        matrix[self.p_location[0]][self.p_location[1]-1] = 'P' 
        self.p_location[1] -= 1  
      elif kp == 'W' and matrix[self.p_location[0]-1][self.p_location[1]] != '#':
        replit.clear()
        matrix[self.p_location[0]][self.p_location[1]] = '.'
        matrix[self.p_location[0]-1][self.p_location[1]] = 'P'
        self.p_location[0] -= 1  
      elif kp == 'Q':
        return kp
      elif kp == 'D' and matrix[self.p_location[0]][self.p_location[1]+1] == '#':
        replit.clear()
        pass
      elif kp == 'S' and matrix[self.p_location[0]+1][self.p_location[1]] == '#':
        replit.clear()
        pass
      elif kp == 'A' and matrix[self.p_location[0]][self.p_location[1]-1] == '#':
        replit.clear()
        pass
      elif kp == 'W' and matrix[self.p_location[0]-1][self.p_location[1]] == '#':
        replit.clear()
        pass

      for line in matrix:
        mapst =  '  '.join(map(str, line)) 
        print(mapst)          

@dataclass
class Archivo(Juego):

  def path(self):
    path = "mydata" + str(random.randint(1,4)) + ".txt"
    return path

  def textMap(self):  
    f = open(self.path(), "r")
    res = ft.reduce(lambda a,b: a+b, (x for x in map(lambda x: x.rstrip(), f.readlines())))
    return(res)

  def createMatrix(self): 
    res = self.textMap()
    temp = (res[index: index + Juego.colCount] for index in range(0, len(res), Juego.colCount))
    mat = list(map(lambda y: list(y), temp))
    return mat

# Metodo alternativo sin ft.reduce para hacerlo lo arriba en 1 linea
  # def createMatrix(self):
  #   mat = list(map(lambda y: list(y), (list(map(lambda x: x.rstrip(), (open("mydata" + str(random.randint(1,4)) + ".txt", "r")).readlines())))))
  #   return mat

  def main(self): 
    mat3 = self.createMatrix()
    mat3[0][0] = 'P'
    
    for line in mat3:
      mapst =  '  '.join(map(str, line))
      print(mapst)

    mat2 = self.createMatrix()
    mat2[0][0] = 'P'

    Juego.movements(self,matrix=mat2)

if __name__ == "__main__":
  juego = Archivo()
  juego.main()   
