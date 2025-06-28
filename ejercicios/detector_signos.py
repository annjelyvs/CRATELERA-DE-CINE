#ronda 1 
print("deterctor de signos") 


num1=int(input("ingrese un numero negativo o positivo: "))
num2=int(input("ingrese otro numero positivo o negativo: "))

if num1 >0 and num2>0:
    print(f"el numero{num1} y {num2} son positivos")

elif num1 <0 and num2 <0 :
    print(f"el numero {num1} y {num2} son negativos")

elif num1 >0 and num2 <0 :
    print(f"el numero {num1} es positivo y {num2} es negativo")

else:
    print(f"el numero {num2} es positivo y {num1} es negativo")