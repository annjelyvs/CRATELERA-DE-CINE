print("identificador de carcateres ")
caracteres=input("ingrese un caracter especifico: ")

if caracteres.isLetter():
    print(f"{caracteres} es una letra")

elif caracteres.isdigit():
    print(f"{caracteres} es un digito ")
 
elif caracteres == " ":
    print(f"{caracteres} es un espacio")

else:
    print(f"{caracteres} es un simbolo")