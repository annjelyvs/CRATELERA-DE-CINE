print("CARTELERA DE CINE")

peliculas=["avatar","titanic","intelestelar"]
salas=["sala1","sala2","sala3"]

if "intelestelar" in peliculas:
    peliculas.append("Duna")
    print(f"lista de peliculas actualizada{peliculas}")
else:
    print("no se cumple")

if "sala3" in salas:
       salas.append("sala VIP")
       print(f"lista de salas actualizada{salas}")
else:
       print("no se cumple")

if "titanic" in peliculas:
    peliculas.pop(1)
    print(f"lista de peliculas actualizada{peliculas}")
else: 
    print("no se cumple")

if len(salas) >3:
    salas.pop(0)
    print(f"la lista de salas despues de la aliminacion quedo {salas}")
else:
    print("no se cumple")

if "avatar" in peliculas:
    peliculas.remove("avatar")
    peliculas.append("avartar2")
    print(f"se elimino y reemplazo una pelicula y  la lista quedo {peliculas}")
else:
    print("no se cumple la condicion")

print("otras listas ")
estrenos=peliculas[0],peliculas[1]
salas_disponibles=salas[-1],salas[-2]

if "sala VIP" in salas_disponibles :
    funcion_especial=("Duna","sala VIP ")
    print(f"se actualizo las salas disponibles y quedo {salas_disponibles}")
else:
     print("no se cumple")
if "avartar2" in estrenos:
        estrenos.append("3D")
        print(f"la lista de estreno esta actualizada {estrenos}")
else:
     print("no se cumple")
if "3D" in estrenos:
    programacion={"peliculas":"avartar2",
                         "sala":"sala2",
                         "formato":"3D"}
    print(f"se creo un diccionario y quedo {programacion}")
else:
     print("no se cumple")
if programacion in programacion:
    programacion.append({"hora":"6:30 PM"})
    print(f"acualizacion del diccionario {programacion}")
else:
     print("no se cumple")
if "sala4" in salas:
       salas.append("sala4")
else:
     print("no se cumple")
if "titanic" in peliculas:
      peliculas.append("titanic")
else:
     print("la condicion no se cumple")
print(f"actualizacion de peliculas{peliculas}, actualizacion de salas {salas}, actualizacion de salas_disponibles {salas_disponibles}, tuplas {funcion_especial},diccionario{programacion}")