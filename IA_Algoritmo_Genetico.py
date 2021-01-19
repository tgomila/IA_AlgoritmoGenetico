#Ejercicio de algoritmo genético

import random
import copy


#Probado en 5.000, 10.000, 100.000. No se recomienda 1.000, tampoco +100.000 por tiempos
#Edite la población a su gusto, variarán los tiempos y la cantidad de repeticiones del loop
n_poblacion = 100000
vitalidad = 200
mutaciones = 200
puntuacion_perder = 0.5
puntuacion_castigo = 1
probabilidad_de_vitalidad = 70
loop_maximo = 7

### Limitationes de la tabla ###

#Se tienen las siguientes pistas: Hay
#   cinco casas de diferentes colores
#   cinco profesiones distintas,
#   cinco lenguajes de programación,
#   cinco editores de texto,
#   cinco bases de datos NoSQL distintas.

# 1. El matemático vive en la casa roja
# 2. El hacker programa en Python
# 3. Visual Studio Code es utilizado por elQueViveEnLaCasa verde
# 4. El analista usa Atom
# 5. El que vive en la casa verde, estaALaDerechaDelDeLaCasaNegra
# 6. Es que usa Redis escribe en Java
# 7. El que usa Cassandra vive en la casa amarilla
# 8. El que usa Notepad ++ vive en la casa del medio
# 9. El desarrollador vive en la primer casa
# 10. El que usa Hadoop vive al ladoDelQueEscribe en JavaScript
# 11. Cassandra es usado en la casa alLadoDelQue programa en C#
# 12. La persona que usa Neo4J usa SublimeText
# 13. El ingeniero usa MongoDB
# 14. El desarrollador vive al lado de la casa azul
# 15. El que usa C++ usa Vim

#Quien programa en C++ en Vim?

colores =       ["roja", "verde", "amarilla", "negra", "azul"]
profesiones =   ["matemático", "hacker", "analista", "desarrollador", "ingeniero"]
lenguajes =     ["Python", "Java", "JavaScript", "C#", "C++"]
editores =      ["Visual Studio Code", "Atom", "Notepad ++", "SublimeText", "Vim"]
basesDeDatos =  ["Redis", "Cassandra", "Hadoop", "MongoDB", "Neo4J"]

#               0           1           2         3           4
tablaInfo = [colores, profesiones, lenguajes, editores, basesDeDatos]


class Tabla:

        # Inicializar / Constructor, se usa __init__ para constructor #
        def __init__(self):
                self.tabla = [[0 for x in range(5)] for x in range(5)] 
                self.puntuacion = 20
                self.aprobar = 0

        def getTabla(self, x, y):
                return self.tabla[x][y]

        #Este random te asegura que la tabla sea de distintos colores, profesiones, etc.
        def cargarTablaRandom(self):
                #Para cada elemento fila de la tabla
                for x in range(0,5):
                        self.tabla[x] = random.sample(tablaInfo[x], 5)
        
        def mutar(self):
                x  = random.randint(0,4)
                y = random.randint(0,4)
                temp = self.tabla[x][y]
                self.tabla[x][y] = self.tabla[x][(y+1)%5]
                self.tabla[x][(y+1)%5] = temp
                random.shuffle(self.tabla[x])

        def probar(self):
                #Reset de puntuacion
                self.aprobar = 0
                self.puntuacion = 20
                #probar consistencia de los datos
                for x in range(0,5):
                        if len(self.tabla[x])!=len(set(self.tabla[x])):
                                self.puntuacion -= 2*puntuacion_castigo;
                                #self.aprobar -= 2*puntuacion_castigo;

                # 1. El matemático vive en la casa roja
                try:
                        #tabla[ 1 ] es "profesiones"
                        i = self.tabla[1].index('matemático')
                        #tabla[ 0 ] es "colores"
                        if self.tabla[0][i] == 'roja':
                                #print(' 1. El matemático vive en la casa roja')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo

                # 2. El hacker programa en Python
                try:
                        i = self.tabla[1].index('hacker')
                        if self.tabla[2][i] == 'Python':
                                #print(' 2. El hacker programa en Python')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                
                # 3. Visual Studio Code es utilizado por el que vive en la casa verde
                #Lo cambio a "El que vive en la casa verde usa Visual studio code"
                try:
                        #tabla[ 3 ] es "editores"
                        #tabla[ 0 ] es "colores"
                        i = self.tabla[0].index('verde')
                        if self.tabla[3][i] == 'Visual Studio Code':
                                #print(' 3. Visual Studio Code es utilizado por el que vive en la casa verde')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 4. El analista usa Atom
                try:
                        #tabla[ 1 ] es "profesiones"
                        i = self.tabla[1].index('analista')
                        #tabla[ 3 ] es "editores"
                        if self.tabla[3][i] == 'Atom':
                                #print(' 2. El hacker programa en Python')
                                self.puntuacion += 1
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 5. El que vive en la casa verde, esta a la derecha del de la casa negra
                try:
                        #tabla[ 0 ] es "colores"
                        i = self.tabla[0].index('verde')
                        #tabla[ 3 ] es "editores"
                        if self.tabla[0][i-1] == 'negra':
                                #print(' 5. El que vive en la casa verde, esta a la derecha del de la casa negra')
                                self.puntuacion += 1
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                
                # 6. Es que usa Redis escribe en Java
                try:
                        #tabla[ 4 ] es "baseDeDatos"
                        i = self.tabla[4].index('Redis')
                        #tabla[ 2 ] es "lenguajes"
                        if self.tabla[2][i] == 'Java':
                                #print(' 6. Es que usa Redis escribe en Java')
                                self.puntuacion += 1
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                
                # 7. El que usa Cassandra vive en la casa amarilla
                try:
                        i = self.tabla[0].index('amarilla')
                        if self.tabla[4][i] == 'Cassandra':
                                #print(' 3. Visual Studio Code es utilizado por el que vive en la casa verde')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                
                # 8. El que usa Notepad ++ vive en la casa del medio
                try:
                        if self.tabla[3][2] == 'Notepad ++':
                                #print(' 8. El que usa Notepad ++ vive en la casa del medio')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                
                # 9. El desarrollador vive en a primer casa
                try:
                        if self.tabla[1][0] == 'desarrollador':
                                #print(' 9. El desarrollador vive en a primer casa')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 10. El que usa Hadoop vive al lado del que escribe en JavaScript
                try:
                        i = self.tabla[4].index('Hadoop')
                        if self.tabla[2][i-1] == 'JavaScript':
                                #print(' 10. El que usa Hadoop vive al lado del que escribe en JavaScript')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                if self.tabla[2][i+1] == 'JavaScript':
                                        #print(' 10. El que usa Hadoop vive al lado del que escribe en JavaScript')
                                        self.puntuacion += 1
                                        self.aprobar +=1
                                else:
                                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 11. Cassandra es usado en la casa al lado del que programa en C#
                #Cassandra = derecha, C# = izquierda
                try:
                        i = self.tabla[4].index('Cassandra')
                        if self.tabla[2][i-1] == 'C#':
                                #print(' 11. Cassandra es usado en la casa al lado del que programa en C#')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                if self.tabla[2][i+1] == 'C#':
                                        #print(' 11. Cassandra es usado en la casa al lado del que programa en C#')
                                        self.puntuacion += 1
                                        self.aprobar +=1
                                else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 12. La persona que usa Neo4J usa SublimeText
                try:
                        i = self.tabla[4].index('Neo4J')
                        if self.tabla[3][i] == 'SublimeText':
                                #print(' 12. La persona que usa Neo4J usa SublimeText')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 13. El ingeniero usa MongoDB
                try:
                        i = self.tabla[1].index('ingeniero')
                        if self.tabla[4][i] == 'MongoDB':
                                #print(' 13. El ingeniero usa MongoDB')
                                self.puntuacion += 1    
                                self.aprobar +=1
                        else:
                                        self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo
                        
                # 14. El desarrollador vive al lado de la casa azul
                #desarrollador = derecha, casa azul = izquierda
                try:
                        i = self.tabla[1].index('desarrollador')
                        if self.tabla[0][i-1] == 'azul':
                                #print(' 14. El desarrollador vive al lado de la casa azul')
                                self.puntuacion += 1
                                self.aprobar +=1
                        else:
                                if self.tabla[0][i+1] == 'azul':
                                        #print(' 14. El desarrollador vive al lado de la casa azul')
                                        self.puntuacion += 1
                                        self.aprobar +=1
                                else:
                                        self.puntuacion -= puntuacion_perder
                                
                except:
                        self.puntuacion -= puntuacion_castigo

                # 15. El que usa C++ usa Vim
                try:
                        i = self.tabla[2].index('C++')
                        if self.tabla[3][i] == 'Vim':
                                #print(' 15. El que usa C++ usa Vim')
                                self.puntuacion += 1
                                self.aprobar +=1
                        else:
                                self.puntuacion -= puntuacion_perder
                except:
                        self.puntuacion -= puntuacion_castigo

                

                #tablaInfo = [colores, profesiones, lenguajes, editores, baseDeDatos]
                #               0           1           2         3           4

                

                #print(self.tabla)
                #print(self.puntuacion)

class Programadores:

        def __init__(self):
                 self.poblacion = []

        def resolver(self, intento):

                self.generar(n_poblacion)
                x = 0
                # inicializo  [nro aprobar anterior, cantidad de veces seguidas que salio]
                #si salio 5 veces seguidas, se reinicia resolver
                anterior = [-1, 1]
                
                while True:
                        #Algoritmo principal
                        x += 1
                        print('Iteracion  %d' %x)
                        self.probar()#Armo puntuacion y aprobar, ordeno poblacion de mayor a menor
                        aprobar =  self.poblacion[0].aprobar

                        if(aprobar < 15):
                                self.crossOver(vitalidad, n_poblacion)
                                self.mutar()
                                #aprobar =  self.poblacion[0].aprobar
                        #Fin principal

                        #verifico loop
                        if(anterior[0] == aprobar):
                                anterior[1] += 1
                        else:
                                anterior[0] = aprobar
                                anterior[1] = 0

                        print(anterior)
                        #verifico si las iteraciones anteriores se repitio el mismo aprobar n veces seguidas
                        if(anterior[1] >= loop_maximo):
                                intento += 1
                                print("Loop: Se reinicia el proceso de generación de población despues de", loop_maximo, "repeticiones. Intento nro", intento)
                                self.poblacion = []
                                progra = Programadores()
                                progra.resolver(intento)
                                aprobar = -1
                                break

                        if aprobar >= 15:
                                break

                if(aprobar >= 15):
                        #self.probar()
                        #PRINTS RESULTADOS
                        print (self.poblacion[0].tabla)
                        print (self.poblacion[0].aprobar)
                        print ("Intentos:", intento)
                        print()
                        #Imprimo datos de manera ordenada
                        print('\n'.join([''.join(['{:20}'.format(item) for item in row]) for row in self.poblacion[0].tabla]))
                        print()
                        self.poblacion[0].probar()
                        print("Posee puntuacion:", self.poblacion[0].aprobar," cumpliendo todas las restricciones")

                        #Quien programa en C++ en Vim?
                        rta = self.poblacion[0].tabla
                        i = self.poblacion[0].tabla[2].index('C++')

                        print()
                        print()
                        
                        print("¿Quién programa en C++ en Vim? Respuesta:")

                        print("El",self.poblacion[0].tabla[1][i],
                              "vive en la casa de color",self.poblacion[0].tabla[0][i],
                              ", utiliza" ,self.poblacion[0].tabla[4][i],
                              ",",self.poblacion[0].tabla[3][i],
                              "y programa en",self.poblacion[0].tabla[2][i])

                
                
        def mutar(self):
                for x in range(0,mutaciones):
                        y = random.randint(0,len(self.poblacion)-1)
                        self.poblacion[y].mutar()
                

        def generar(self, i):
                for x in range(0,i):
                        nuevaTablaIndividuo = Tabla()
                        nuevaTablaIndividuo.cargarTablaRandom()
                        self.poblacion.append(nuevaTablaIndividuo)

        def crossOver(self, i, limite):
                
                buenaPoblacion = []
                i = 0
                while len(buenaPoblacion)<vitalidad:
                        if random.randint(0,100)<probabilidad_de_vitalidad:
                                buenaPoblacion.append(self.poblacion[i])
                        i += 1 
                        i %= len(self.poblacion)

                nuevaGeneracion = []
                while len(nuevaGeneracion) <= limite:
                        primero = buenaPoblacion[random.randint(0,len(buenaPoblacion)-1)]
                        segundo = buenaPoblacion[random.randint(0,len(buenaPoblacion)-1)]
                        tercero = buenaPoblacion[random.randint(0,len(buenaPoblacion)-1)]
                        nuevaTablaIndividuo = self.cross(primero, segundo, tercero)
                        nuevaGeneracion.append(nuevaTablaIndividuo)

                self.poblacion = nuevaGeneracion

        def cross(self, primero, segundo, tercero):
                nuevaTablaIndividuo = Tabla()
                for x in range(0,5):
                        for y in range(0,5):

                                i = random.randint(0,2)
                                if i == 0:
                                        nuevaTablaIndividuo.tabla[x][y] = primero.getTabla(x,y)
                                elif i == 1:
                                        nuevaTablaIndividuo.tabla[x][y] = segundo.getTabla(x,y)
                                else:
                                        nuevaTablaIndividuo.tabla[x][y] = tercero.getTabla(x,y)
                return nuevaTablaIndividuo

        def probar(self):
                #Le pone puntuacion a cada poblacion random
                for x in range(0,len(self.poblacion)):
                        self.poblacion[x].probar()

                #ordena mayor a menor
                self.poblacion.sort(key=lambda x: x.puntuacion, reverse=True)
                for x in range(0,1):
                        print (self.poblacion[x].aprobar)

print("Poblacion inicial:", n_poblacion)
print("Este algoritmo llevará su tiempo, aguarde y tome cafecito")
print()
progra = Programadores()
progra.resolver(1) #1 es 1er intento
