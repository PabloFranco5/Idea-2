from Hospital_system.Database_informacion.Pacientes import infopersonalpaciente
from Hospital_system.Database_informacion.Infomedica import infomedica
from Hospital_system.Database_informacion.Infoadministrativa import infoadministrativa
from Hospital_system.Database_informacion.Profesional import infoprofesional
from Hospital_system.Database_informacion.Farmaceutica import infofarmaceutica
from funciones import * 

from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)


print(f"""

 #     #                                                   
 #     #   ####    ####   #####   #  #####    ##    #      
 #     #  #    #  #       #    #  #    #     #  #   #      
 #######  #    #   ####   #    #  #    #    #    #  #      
 #     #  #    #       #  #####   #    #    ######  #      
 #     #  #    #  #    #  #       #    #    #    #  #      
 #     #   ####    ####   #       #    #    #    #  ######

 #     #                     #    
 #     #  #####   ######    # #   
 #     #  #    #  #        #   #  
 #     #  #    #  #####   #     # 
 #     #  #    #  #       ####### 
 #     #  #    #  #       #     # 
  #####   #####   ######  #     # 

""")

while( informacion.lower() != "x"):
    """
    Esta función tiene como objetivo redirigir al usuario a un portal donde tiene el acceso a la informacion 
    que necesita rellenar/modificar/eliminar dependiendo de su necesidad en el momento.

    En la pantalla principal tendremos las opciones del tipo de informacion del cual puede disponer, el usuario
    tiene las siguientes opciones: acceder a la informacion personal del paciente, a la informacion medica del paciente,
    a la informacion administrativa del paciente, informacion profesional de la salud, informacion farmaceutica o si 
    el usuario ya termino lo que estaba haciendo en la interfaz tambien se presenta la opcion de salir de la base de datos.

    """
    print("---- Base de Datos Hospital Universidad de Antioquia ----")
    print("p - informacion personal del paciente")
    print("m - informacion medica del paciente")
    print("a - informacion administrativa del paciente")
    print("s - informacion profesional de la salud") 
    print("f - informacion farmaceutica")
    print("x - salir de la base de datos")
    informacion = input("Ingrese el tipo de información a la que desea acceder: ")
    if( informacion.lower() == "x"):
        """
        Al momento de que el usuario culmine con lo que necesita de la base de datos, se redirige a esta opcion la cual 
        culmina su cesión.
        """
        print(f"""Cerrando sesión del sistema 
        
  #####                                             
 #     #  #####     ##     ####   #    ##     ####  
 #        #    #   #  #   #    #  #   #  #   #      
 #  ####  #    #  #    #  #       #  #    #   ####  
 #     #  #####   ######  #       #  ######       # 
 #     #  #   #   #    #  #    #  #  #    #  #    # 
  #####   #    #  #    #   ####   #  #    #   ####  
                                                           
        
        """)

    if( informacion.lower() == "p"):
        """
        Esta opcion redirige al usuario a la información personal del paciente recopilando la misma 
        en un dataframe donde cada columna hace referencia a una variable.
        """
        listapacientes = listapacientes.append(agregarinfo_p(), ignore_index=True)
        lista_p()

    elif( informacion.lower() == "m"):
        """
        Esta opcion redirige al usuario a la informacion medica del paciente recopilando la misma 
        en un dataframe donde cada columna hace referencia a una variable.
        """
        listainfomedica = listainfomedica.append(agregarinfo_m(), ignore_index=True)
        lista_m()

    elif(informacion.lower() == "a"):
        """
        Esta opcion redirige al usuario a la informacion administrativa del paciente recopilando la misma 
        en un dataframe donde cada columna hace referencia a una variable.
        """
        listainfoadministrativa = listainfoadministrativa.append(agregarinfo_a(), ignore_index=True)
        lista_a()
    
    elif(informacion.lower() == "s"):
        """
        Esta opcion redirige al usuario a la informacion profesional de la salud recopilando la misma 
        en un dataframe donde cada columna hace referencia a una variable.
        """
        listaprofesionales = listaprofesionales.append(agregarinfo_s(), ignore_index=True)
        lista_s()
    elif(informacion.lower() == "f"):
        """
        Esta opcion redirige al usuario a la informacion farmaceutica recopilando la misma 
        en un dataframe donde cada columna hace referencia a una variable.
        """
        listafamaceutica = listafamaceutica.append(agregarinfo_f(), ignore_index=True)   
        lista_f()

if not listapacientes.empty:
    listapacientes.to_csv('listapaciente.txt')

if not listainfomedica.empty:
    listainfomedica.to_csv('listainformacionmedica.txt')

if not listainfoadministrativa.empty:
    listainfoadministrativa.to_csv('listainformacionadministrativa.txt')

if not listaprofesionales.empty:
    listaprofesionales.to_csv('listadatosprofesionales.txt')

if not listafamaceutica.empty:
    listafamaceutica.to_csv('listarecetasfarmaceutica.txt')
