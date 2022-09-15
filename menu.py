#Menu Commit

print('1- Saludar')
print('2- ¿Que desayunaste?')
print('3- Salir')

#Menu Commit
opcion = int(input('Elija una opción: '))

if opcion == 1:
     print(f"Buenos Dias")  

elif (opcion == 2):
    respuesta = input('Indique que desayuno: ')
    print(f'El usuario desayuno: {respuesta} ')

elif opcion == 3:
    print('BYE')
    
else:
        print('Digite una opción valida')
       

