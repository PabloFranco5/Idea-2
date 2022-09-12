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
    print("---- Base de Datos Hospital Universidad de Antioquia ----")
    print("p - informacion personal del paciente")
    print("m - informacion medica del paciente")
    print("a - informacion administrativa del paciente")
    print("s - informacion profesional de la salud") 
    print("f - informacion farmaceutica")
    print("x - salir de la base de datos")
    informacion = input("Ingrese el tipo de información a la que desea acceder: ")
    if( informacion.lower() == "x"):
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
        listapacientes = listapacientes.append(agregarinfo_p(), ignore_index=True)
        lista_p()

    elif( informacion.lower() == "m"):
        listainfomedica = listainfomedica.append(agregarinfo_m(), ignore_index=True)
        lista_m()

    elif(informacion.lower() == "a"):
        listainfoadministrativa = listainfoadministrativa.append(agregarinfo_a(), ignore_index=True)
        lista_a()
    
    elif(informacion.lower() == "s"):
        listaprofesionales = listaprofesionales.append(agregarinfo_s(), ignore_index=True)
        lista_s()
    elif(informacion.lower() == "f"):
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
