#  [USER-PY 1.1]
#     
#   El proyecto USER-PY se trata de un gestor de usuarios basado en python, se trata de un complemento
#   al proyecto MAGICPASS-JS. Su funcionamiento es simple, introduces un usuario y la contraseña gener
#   ada en MAGICPASS-JS y el sistema generará un archivo de texto que registrará todos los usuarios que
#   quieras guardar, De esta forma tendrás todos tus usuarios y contraseñas guardados de forma segura 
#   (almacenándolos en un pen-drive cifrado, por ejemplo)
#   
#   Al igual que su complemento, es un proyecto completamente opensource abierto a cualquiera que quiera explorar
#   o hacer su propia versión de este proyecto ;)
#
#   [XTLABS© 2026 - OPENSOURCE]
#
#   [DOCUMENTACIÓN DEL PROYECTO]
#   
#   Licencia: https://www.mozilla.org/en-US/MPL/2.0/
#   Web XT LABS: https://xtlabsteam.infinityfreeapp.com/
#

# [LIBRERÍAS DEL SISTEMA]

import os # Importamos la librería OS para poder utilizar los comandos de limpiar pantalla
import time # Importamos la librería time para poder utilizar los delay/temporizadores

# [--- FUNCIONES DE REGISTRO/BORRADO DE ARCHIVOS ---]

# Función de registro de nuevos archivos (Borra el archivo de texto y lo reinicia desde cero)

def usrpy_new_file():

    print("-----------") # Mostramos un mensaje indicando que introduzcamos el usuario a registrar
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_username = input("Introduzca usuario:") # Almacenamos el usuario a registrar en la variable "usrpy_username"

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando el usuario registrado
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Usuario registrado:" + usrpy_username)

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que introduzcamos la contraseña a registrar
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_password = input("Introduzca contraseña:")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando la contraseña registrada
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Contraseña registrada:" + usrpy_password)

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que estamos registrando los datos recibidos
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Registrando datos...")

    with open("usrpy_data.txt", "w") as usrpy_file: # Abrimos el archivo en modo "write" para añadir datos sobreescribiendo los anteriores

        usrpy_file.write(usrpy_username + ":" + usrpy_password + "\n") # Escribimos el usuario y la contraseña en el archivo

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que hemos registrado los datos correctamente
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Datos registrados correctamente")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# Función de borrado de archivos

def usrpy_delete_file():

    print("-----------") # Mostramos un mensaje indicando que estamos eliminando los datos recibidos
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Eliminando datos...")

    if not os.path.exists("usrpy_data.txt"): #Si no se detecta el archivo, mostraremos un mensaje de error

        print("ERROR, NO EXISTE BASE DE DATOS DE USUARIOS DISPONIBLE") # Mostramos un mensaje de error indicando que no hay base de datos de usuarios disponible

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    else:

        os.remove("usrpy_data.txt") # Eliminamos el archivo indicado utilizando la función "os.path.remove" de python

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        print("-----------") # Mostramos un mensaje indicando que hemos eliminado los datos correctamente
        print("USER-PY 1.0")
        print("-----------")
        print("")
        print("Datos eliminados correctamente")

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# [--------------------------------------------------]

# [--- FUNCIONES DE BÚSQUEDA/MOSTRADO DE USUARIOS ---]

# Función de búsqueda de usuarios

def usrpy_search_user():

    print("-----------") # Mostramos un mensaje indicando que introduzcamos el usuario a buscar en el buscador del sistema
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_user = input("Introduzca usuario a buscar:")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que estamos buscando el usuario en el sistema
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Buscando usuario...")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    if not os.path.exists("usrpy_data.txt"): # Si no se detecta el archivo, mostraremos un mensaje de error

            print("ERROR, NO EXISTE BASE DE DATOS DE USUARIOS DISPONIBLE") # Mostramos un mensaje de error indicando que no hay base de datos de usuarios disponible

            time.sleep(2) # Esperamos dos segundos
            os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

            return # Ejecutamos función return, para evitar que Python genere excepcion y se bloquee
    
    usrpy_located = False # Variable auxiliar que utilizaremos para localizar el usuario y mostrar el mensaje correspondiente
    
    with open("usrpy_data.txt", "r") as usrpy_file: # Abrimos el archivo en modo "r" para leer los datos del archivo

        for line in usrpy_file: # Ejecutamos un bucle for para poder leer linea por linea
    
            line = line.strip() # Eliminamos los saltos de línea

            if usrpy_user in line: #Si encontramos el usuario en el archivo

                print(line) # Imprimimos el usuario:contraseña en la pantalla
                
                usrpy_located = True # Cambiamos al estado True la variable "usrpy_located"

                time.sleep(2) # Esperamos dos segundos
                os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

                break; # Finalizamos la ejecución de la búsqueda de usuarios, finalizando el bucle for
        
        if not usrpy_located: # Si no lo encontramos

            print("ERROR, USUARIO NO LOCALIZADO") # Mostramos un mensaje de error indicando que no hemos localizado al usuario

            time.sleep(2) # Esperamos dos segundos
            os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

            return # Ejecutamos función return, para evitar que Python genere excepcion y se bloquee
            
# Función de mostrar  usuarios totales

def usrpy_show_user():
    
    print("-----------") # Mostramos un mensaje indicando que estamos mostrando los usuarios del sistema
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Mostrando usuarios del sistema...")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    if not os.path.exists("usrpy_data.txt"): #Si no se detecta el archivo, mostraremos un mensaje de error

            print("ERROR, NO EXISTE BASE DE DATOS DE USUARIOS DISPONIBLE") # Mostramos un mensaje indicando que no hay base de datos de usuarios disponible

            time.sleep(2) # Esperamos dos segundos
            os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

            return # Ejecutamos función return, para evitar que Python genere excepcion y se bloquee

    with open("usrpy_data.txt", "r") as usrpy_file: # Abrimos el archivo en modo "r" para leer los datos del archivo

        for line in usrpy_file: # Ejecutamos un bucle for para poder leer linea por linea
            
            line = line.strip() # Eliminamos los saltos de línea
            print(line) # Imprimimos los datos del archivo

            time.sleep(2) # Esperamos dos segundos
            os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# [-------------------------------------------------]

# [--- FUNCIONES DE REGISTRO/BORRADO DE USUARIOS ---]

# Función de registro de usuarios (Añade nuevos usuarios al archivo sin borrar los anteriores)

def usrpy_add_user():

    print("-----------") # Mostramos un mensaje indicando que introduzcamos el usuario a añadir
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_username = input("Introduzca usuario:") # Almacenamos el usuario a añadir en la variable "usrpy_username"

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("--------------") # Mostramos un mensaje indicando el usuario registrado
    print("USER-PY-PY 1.0")
    print("--------------")
    print("")
    print("Usuario registrado:" + usrpy_username)

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que introduzcamos la contraseña a registrar
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_password = input("Introduzca contraseña:")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando la contraseña registrada
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Contraseña registrada:" + usrpy_password)

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que estamos registrando los datos recibidos
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Registrando datos...")

    with open("usrpy_data.txt", "a") as usrpy_file: # Abrimos el archivo en modo "append" para añadir datos sin sobreescribir los anteriores

        usrpy_file.write(usrpy_username + ":" + usrpy_password + "\n") # Escribimos el usuario y la contraseña en el archivo

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que hemos registrado los datos correctamente
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Datos registrados correctamente")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# Función de borrado de usuarios 

def usrpy_delete_user():

    print("-----------") # Mostramos un mensaje indicando que introduzcamos el usuario a borrar
    print("USER-PY 1.0")
    print("-----------")
    print("")
    usrpy_username = input("Introduzca usuario:") # Almacenamos el usuario a borrar en la variable "usrpy_username"

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que estamos borrando el usuario introducido
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Borrando usuario...")

    if not os.path.exists("usrpy_data.txt"): #Si no se detecta el archivo, mostraremos un mensaje de error

        print("ERROR, NO EXISTE BASE DE DATOS DE USUARIOS DISPONIBLE") # Mostramos un mensaje indicando que no hay base de datos de usuarios disponible

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        return # Ejecutamos función return, para evitar que Python genere excepcion y se bloquee

    with open("usrpy_data.txt", "r") as usrpy_file: # Abrimos el archivo en modo "r" para leer los datos del archivo

        lines = usrpy_file.readlines() # Almacenamos las líneas del archivo en la variable "lines":

    with open("usrpy_data.txt", "w") as usrpy_file: # Abrimos el archivo en modo "write" para añadir datos sobreescribiendo los anteriores

        for line in lines: # Ejecutamos un bucle for para poder leer linea por linea

            if usrpy_username not in line: # Si el usuario introducido no está en la linea

                usrpy_file.write(line) # Reescribimos el archivo, esquivando las líneas que tengan el usuario introducido

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    print("-----------") # Mostramos un mensaje indicando que hemos borrado el usuario correctamente
    print("USER-PY 1.0")
    print("-----------")
    print("")
    print("Usuario borrado correctamente")

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS
    
# [-------------------------------------------------]

# [-------FUNCIONES DEL SISTEMA--------]

# Función de bienvenida del sistema

def system_welcome_screen():
    
    print("----------------------") #Mostramos un mensaje indicando el mensaje de bienvenida del sistema
    print("USER-PY 1.0 BY XT LABS")
    print("----------------------")
    print("")
    print("Bienvenido a USER-PY, un proyecto de XT LABS")
    print("Liberado bajo licencia MPL 2.0")

# Función de versión del sistema

def system_version_screen():

    print("-----------") # Mostramos un mensaje indicando que versión del sistema tenemos instalada
    print("USER-PY 1.0")
    print("-----------")
    print ("")
    print ("Versión del sistema instalada -> v1.1") # Mostramos un mensaje indicando la versión específica del programa

    time.sleep(2) # Esperamos dos segundos
    os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# Función lectora de comandos

def system_command_screen():

    print("-----------") # Mostramos un mensaje indicando que introduzcamos un comando
    print("USER-PY 1.0")
    print("-----------")
    print ("")
    usrpy_command = input ("Introduzca comando:") # Almacenamos el comando en la variable "usrpy_command"

    # Comando de nuevo registro de archivos

    if usrpy_command == "usrpy/new_file": 

        print("Iniciando registro de nuevo archivo") # Mostramos un mensaje indicando que estamos iniciando el registro de un nuevo archivo
        
        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_new_file() # Llamamos a la función "usrpy_new_file"

    # Comando de borrado de archivos

    elif usrpy_command == "usrpy/delete_file": 

        print("Iniciando borrado de archivos") # Mostramos un mensaje indicando que estamos iniciando el borrado de un archivo
        
        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_delete_file() # Llamamos a la función "usrpy_delete_file"

    # Comando de búsqueda de usuarios

    elif usrpy_command == "usrpy/search_user":

        print("Iniciando búsqueda de usuarios") # Mostramos un mensaje indicando que estamos iniciando la búsqueda de usuarios

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_search_user() #Llamamos a la función "usrpy_search_user"

    # Comando de lectura de usuarios totales

    elif usrpy_command == "usrpy/show_user":

        print("Iniciando lectura de usuarios") # Mostramos un mensaje indicando que estamos iniciando la lectura de usuarios

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_show_user() #Llamamos a la función "usrpy_show_user"

    # Comando de añadido de usuarios
    
    elif usrpy_command == "usrpy/add_user": 

        print("Iniciando añadido de usuarios") # Mostramos un mensaje indicando que estamos iniciando el añadido de un nuevo usuario
        
        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_add_user() # Llamamos a la función "usrpy_add_user"

    # Comando de borrado de usuarios
    
    elif usrpy_command == "usrpy/delete_user": 

        print("Iniciando borrado de usuarios") # Mostramos un mensaje indicando que estamos iniciando el borrado de usuarios
        
        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        usrpy_delete_user() # Llamamos a la función "usrpy_add_user"

    # Comando de ayuda del sistema

    elif usrpy_command == "usrpy/system_help":

        print("Mostrando ayuda del sistema") # Mostramos un mensaje indicandoque estamos mostrando la ayuda del sistema

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        help_screen() # Llamamos a la función "help_screen"

    # Comando de versión del sistema

    elif usrpy_command == "usrpy/system_version":

        print("Mostrando versión del sistema") # Mostramos un mensaje indicando que estamos mostrando la versión del sistema

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

        system_version_screen() # Llamamos a la función "version_screen"

    # Comando de limpieza de pantalla

    elif usrpy_command == "usrpy/system_clear":

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

    # Comando de salida del programa

    elif usrpy_command == "usrpy/system_exit" : 

        time.sleep(2) # Esperamos dos segundos
        quit() # Salimos del intérprete de python

    # Cualquier comando no registrado en el sistema

    else:

        print("ERROR, COMANDO NO RECONOCIDO") # Mostramos un mensaje indicando que no hemos reconocido el comando introducido

        time.sleep(2) # Esperamos dos segundos
        os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

# Función de ayuda del sistema

def help_screen():

    print("-----------") # Mostramos un mensaje indicando que hemos iniciado la función de ayuda de USER-PY, y mostramos los comandos del sistema
    print("USER-PY 1.0")
    print("-----------")
    print ("")

    print("USER-PY HELP v1.0")

    print("")

    print("Comandos de control de archivos:") # Comandos de control de archivos

    print("")

    print("usrpy/new_file -> Crear nuevo archivo, sobreescribiendo el anterior")
    print("usrpy/delete_file -> Borrar archivo")

    print("")

    print("Comandos de búsqueda y localización de usuarios:") # Comandos de búsqueda y localización de usuarios

    print("")

    print("usrpy/search_user -> Buscar usuario")
    print("usrpy/show_user -> Mostrar los usuarios totales del sistema")

    print("")

    print("Comandos de control de usuarios:") # Comandos de control de usuarios

    print("")

    print("usrpy/add_user -> Añadir nuevo usuario")
    print("usrpy/delete_user -> Borrar usuario")

    print("")

    print("Comandos del sistema:") # Comandos del sistema

    print("")

    print("usrpy/system_help -> Ayuda del sistema") 
    print("usrpy/system_clear -> Limpiar pantalla")
    print("usrpy/system_version -> Versión de la aplicación")
    print("usrpy/system_exit -> Salir de la aplicación")

    print("")

# [------------------------------------]

system_welcome_screen() # Llamamos a la función de bienvenida, que se ejecutará cada vez que iniciemos el programa

time.sleep(2) # Esperamos dos segundos
os.system("cls" if os.name == "nt" else "clear") # Limpiamos pantalla con el comando que corresponda, según el OS

while True:

    system_command_screen() # Ejecutamos la función lectora de comandos del dispositivo
