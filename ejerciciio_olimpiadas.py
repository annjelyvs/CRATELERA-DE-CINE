#ronda3
print("CARTELERA DE CINE")


peliculas=["avatar", "titanic","intelestelar"]
peliculas.append(input("ingrese las peliculas que desea: "))
peliculas.append(input("ingrese las peliculas que desea: "))

salas=["sala1","sala2","sala3"]
salas.append(input("ingrese en la sala que lo desea "))
salas.append(input("ingrese en la sala que lo desea "))

#se va añadir una pelicula
if "intelestelar" in peliculas:
    peliculas.append("Duna")
    print(f"lista de peliculas actualizada{peliculas}")
else:
    print("no se cumple")
    
#"se añade una sala     
if "sala3" in salas:
       salas.append("sala VIP")
       print(f"lista de salas actualizada{salas}")
else:
       print("no se cumple")
       
#se elimina una pelicula
if "titanic" in peliculas:
    peliculas.pop(1)
    print(f"lista de peliculas actualizada{peliculas}")
else: 
    print("no se cumple")
    
#se elimina la primera sala 
if len(salas) >3:
    salas.pop(0)
    print(f"la lista de salas despues de la eliminacion quedo {salas}")
else:
    print("no se cumple")
    
#se reemplaza una pelicula
if "avatar" not in peliculas:
    peliculas.remove("avatar")
    peliculas.append("avartar2")
    print(f"se elimino y reemplazo una pelicula y  la lista quedo {peliculas}")
else:
    print("no se cumple la condicion")

print("otras listas ")
estrenos=peliculas[0],peliculas[1]
salas_disponibles=salas[-1],salas[-2]
funcion_especial=()

#se crea una tupla
if "sala VIP" in salas_disponibles:
    funcion_especial=("Duna","sala VIP ")
    print(f"se actualizo las salas disponibles y quedo {salas_disponibles}")
else:
     print("no se cumple")
     
#se añade 3D ala lista
if "avartar2" in estrenos:
        estrenos.append("3D")
        print(f"la lista de estreno esta actualizada {estrenos}")
else:
     print("no se cumples")
     
#se crea un diccionario
if "3D" in estrenos:
    programacion={"peliculas":"avartar2",
                         "sala":"sala2",
                         "formato":"3D"}
    print(f"se creo un diccionario y quedo {programacion}")
else:
     print("no se cumple")
     
#se añade una clave 
if "programacion" in locals():
    programacion.append({"hora":"6:30 PM"})
    print(f"acualizacion del diccionario {programacion}")
else:
     print("no se cumple")
     
#se agrega una sala     
if "sala4" not in salas:
       salas.append("sala4")
       print(f"la actualizacion de las salas queda asi {salas}")
else:
     print("no se cumpled")
     
#se verifica si esta o no una pelicula
if "titanic" not in peliculas: # el not in no ayuda a confirmar si algo esta o no dentro de una variable 
      peliculas.append("titanic")
      print(f"la actualizacion de las peliculas queda asi {peliculas }")
else:
     print("la condicion no se cumple")
     
print(f"actualizacion de peliculas{peliculas}, actualizacion de salas {salas}, actualizacion de salas_disponibles {salas_disponibles}")