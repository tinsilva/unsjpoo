import re

# Se crea la clase email
class Email:
    __idCuenta=" "
    __dominio=" "
    __tipoDominio=" "
    __contrasena=" "

# Se inicializa los atributos de clase
    def __init__(self,idCuenta,dominio,tipoDominio,contrasena):
        self.__idCuenta = idCuenta #nombre de la cuenta
        self.__dominio = dominio # gmail , hotmail , etc
        self.__tipoDominio = tipoDominio # com , com.ar, etc
        self.__contrasena = contrasena

    def __str__(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio

# Metodo que retorna el dominio
    def get_Dominio(self):
        return self.__dominio

# Metodo que retorna el tipo de dominio
    def get_TipoDominio(self):
        return self.__tipoDominio

# Metodo que devuelve el correo construido
    def retornaEmail(self):
        """ siempre que es get o sea retorna va un return """
        return '{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio)

# Metodo que devuelve contrasena
    def getContrasena(self):
        return self.__contrasena

# Metodo modifica contrasena
    def setContrasena(self,contra): 
        """ siempre que setea algo es que asigna un valor """
        while(self.__contrasena == contra):
            self.__contrasena = input('Ingrese password nuevo')
            print("\n Su nueva contrasena es: {}".format(self.__contrasena))
            print("La contrasena ha sido creada con exito")
            input("Press a key to continue...")
            break
        else:
            print("Contrasena INCORECTA\n")
            contra = input("\nIngrse la contrasena ACTUAL again: " )
    
    def SepararCrear(emailx):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',emailx.lower()):
            print('\n ****Correo correcto****')
            a = emailx.split("@") # lista a  = nombre / dominio.com
            b = a[1].split(".") # lista b = dominio / com
            __idCuenta = a[0] # a[0] = el nombre del correo
            __dominio = b[0] # b[0] = es el dominio
            __tipoDominio = b[1] # b[1] = es com / com.ar
            __contrasena = input("Ingrese Password")
            email2 = Email(__idCuenta, __dominio, __tipoDominio, __contrasena)
            print('\n ****Instancia Creada****')
            input("Press key to cont...")
        else:
            print('\n ****Correo incorrecto****')
