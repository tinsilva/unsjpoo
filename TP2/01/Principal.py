from ClaseEmail import *
import csv

def menu():
    os.system('cls') # clear en linux
    print("Bienvenido al Ejercicio Nro.1 de POO sobre creacion de clase e instancia de email \n\n")
    print("\n\t1 - Crear un email y cambiar pass")
    print("\n\t2 - Crear un objeto de clase Email, a partir de una dirección de correo")
    print("\n\t3 - Buscar cantidad de Dominios y leer CSV")
    print("\n\t4 - Salir")

def opcion1(): # crear correo
    nombre=input("Ingrese su nombre :")
    idCuenta=input("Ingrese Nombre de cuenta o ID: ")
    dominio=input("Ingrese Dominio: ")
    tipoDominio=input("Ingrese tipo de dominio: ")
    contrasena=input("Ingrese Contrasena: ")
    correo1 = Email(idCuenta,dominio,tipoDominio,contrasena) #creo objeto instancia
    print(id(correo1)) # imprime identidicador unico de objeto para test
    print("Estimado {} te enviaremos tus mensajes a la direccion {}".format(nombre,correo1.retornaEmail()))
    print('\n *************************************************************')
    print("MODIFICAR CONTRASENA DE ",format(correo1.retornaEmail()))
    contra = input("Ingrse la contrasena ACTUAL :" )
    Email.setContrasena(contra) # Paso por parametro la contrasena actual para verificar

def opcion2(): # Crear email a partir de ingreso de correo electronico
    emailx = input("Ingrese email: ")
    Email.SepararCrear(emailx)

def opcion3():
    dominio=input("Dominio a buscar: ")
    arch=open("archivo.csv")
    cont=0
    reader=csv.reader(arch,delimiter=",")
    for i in reader:
        if i[1]==dominio:
            cont+=1
    print("cantidad de emails con el dominio ingresado: ",cont)
    input("Press any key to continue....")
    arch.close()

if __name__ == '__main__':
    while(True):
        menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1": #crear primer objeto email y cambiar pass
            opcion1()
        elif opcion == "2": # Crear correo a partir de ingreso de string
            opcion2()
        elif opcion == "3": # Buscar Dominio y leer archivo csv
            opcion3()
        elif opcion == "4": # Salir
            print ("bye, see you soon ... ")
            break
        else:
            print("bad choice, try again")

