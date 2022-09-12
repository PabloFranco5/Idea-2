from Hospital_system.Database_informacion.Pacientes import infopersonalpaciente
from Hospital_system.Database_informacion.Infomedica import infomedica
from Hospital_system.Database_informacion.Infoadministrativa import infoadministrativa
from Hospital_system.Database_informacion.Profesional import infoprofesional
from Hospital_system.Database_informacion.Farmaceutica import infofarmaceutica

from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)

#las funciones en general llamadas agregarinfo_ tienen la intencion de que dependiendo del tipo de informacion que se desee
#llenar preguntarla con especificaciones delimitadas para mayor facilidad tanto al lector como para la base de datos
#arrojando en un listado los datos que se pidieron 


def agregarinfo_p():

    while True:
        tipo_doc = input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ").lower()
        if tipo_doc == "cc" or tipo_doc =="ti" or tipo_doc =="rc" or tipo_doc =="ce" or tipo_doc =="pp":
            break
        print("Ingrese un valor válido")

    while True:
        try:
            documento = int(input("Ingrese el documento del paciente: "))
            if documento > 10**6:
                break
            print("Confirme documento de identificación")
        except ValueError: 
            print("No es un número válido")
            
    
    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if any(chr.isdigit() for chr in nombre):
            print("Revise el nombre :(")
        else:
            break

    while True:
        apellido = input("Ingrese el apellido del paciente: ")
        if any(chr.isdigit() for chr in apellido):
            print("Revise el apellido :(")
        else:
            break

    while True:
        try:
            numero_contacto = int(input("Ingrese el numero de contacto: "))
            if numero_contacto > 10**6:
                break
            print("Confirme número de contacto")
        except ValueError: 
            print("No es un número válido")


    while True:
        ciudad_residencia = input("Ingrese la ciudad de residencia: ")
        if any(chr.isdigit() for chr in ciudad_residencia):
            print("Revise la ciudad de residencia :(")
        else:
            break

    while True:
        estado_civil = input("Ingrese el estado civil: ")
        if any(chr.isdigit() for chr in estado_civil):
            print("Revise el estado civil :(")
        else:
            break

    while True:
        nacionalidad = input("Ingrese la nacionalidad:  ")
        if any(chr.isdigit() for chr in nacionalidad):
            print("Revise la nacionalidad :(")
        else:
            break

    while True:
        try:
            numero_emergencia = int(input("Ingrese un número contacto de emergencia: "))
            if numero_emergencia > 10**6:
                break
            print("Confirme número de contacto")
        except ValueError: 
            print("No es un número válido")

    ultima_actualizacion =input("Ingrese la fecha de la ultima visita (YYYY,MM,DD): ")


    Paciente = infopersonalpaciente(tipo_doc, documento, nombre, apellido, numero_contacto, ciudad_residencia, estado_civil, nacionalidad, numero_emergencia, ultima_actualizacion)
    return Paciente.DFdata()


def agregarinfo_m():

    while True:
        tipo_doc = input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ").lower()
        if tipo_doc == "cc" or tipo_doc =="ti" or tipo_doc =="rc" or tipo_doc =="ce" or tipo_doc =="pp":
            break
        print("Ingrese un valor válido")

    while True:
        try:
            documento = int(input("Ingrese el número de documento: "))
            if documento > 10**6:
                break
            print("Confirme documento de identificación")
        except ValueError: 
            print("No es un número válido")

    while True:
        try:
            historia = int(input("Ingrese el número de historia: "))
            break
        except ValueError: 
            print("Valor inválido para una historia")


    while True:
        try:
            edad = int(input("Ingrese la edad del paciente: "))
            break
        except ValueError: 
            print("Ingrese edad valida")

    while True:
        sexo = input("Ingrese el sexo del paciente(F/M): ").upper()
        if sexo == "F" or sexo =="M" :
            break
        print("Ingrese un valor válido, solo M o F")

    while True:
        RH = input("Ingrese el RH al que pertenece el paciente (+,-): ")
        if RH == "+" or RH =="-" :
            break
        print("Ingrese un valor válido, solo + o -")
    
    while True:
        sanguineo = input("Ingrese el grupo sanguineo del paciente (A, B, O, AB): ").upper()
        if sanguineo == "A" or sanguineo =="B" or sanguineo =="O" or sanguineo =="AB" :
            break
        print("Ingrese grupo sanguineo válido")

    while True:
        try:
            peso = float(input("Ingrese el peso del paciente (kg): "))
            break
        except ValueError: 
            print("Peso inválido")

    while True:
        try:
            estatura = int(input("Ingrese el estatura del paciente (cms): "))
            break
        except ValueError: 
            print("estatura inválido")

    while True:
        reanimacion = input("En caso de que se complique su salud, el paciente esta deacuerdo con ser reanimado (si, no): ").lower()
        if reanimacion == "sí" or reanimacion =="si" or reanimacion =="no":
            break
        print("Ingrese respuesta válida")

    
    alergias = input("A que es alergico el paciente: ")
    comorbilidades = input("ingrese las comorbilidades del paciente: ")

    while True:
        try:
            embarazos = int(input("Cantidad de embarazos hasta la fecha: "))
            if embarazos < 30:
                break
            print("Confirme número de contacto")
        except ValueError: 
            print("No es un número válido")

    FUM = input("Fecha de la ultima mestruación (YYYY-MM-DD): ")
    observaciones = input("Observaciones medicas: ")
    remision = input("El paciente requirio remision a un especialista (si,no): ")
    especialista = input("Tipo de especialista al que fue remitido el paciente: ")
    medicacion = input("Medicación resetada por el doctor que vio al paciente: ") 
    actualizacion = input("Ingrese la fecha de la ultima actualizacion de datos (YYYY-MM-DD):") 

    info_medica_paciente=infomedica(tipo_doc,documento, historia, edad, sexo, RH, sanguineo, peso, estatura, reanimacion, alergias, comorbilidades, embarazos, FUM, observaciones, remision, especialista, medicacion, actualizacion)
    return info_medica_paciente.DFdata()


def agregarinfo_a():
    while True:
        tipo_doc = input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ").lower()
        if tipo_doc == "cc" or tipo_doc =="ti" or tipo_doc =="rc" or tipo_doc =="ce" or tipo_doc =="pp":
            break
        print("Ingrese un valor válido")

    while True:
        try:
            documento = int(input("Ingrese el número de documento: "))
            if documento > 10**6:
                break
            print("Confirme documento de identificación")
        except ValueError: 
            print("No es un número válido")

    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if any(chr.isdigit() for chr in nombre):
            print("Revise el nombre :(")
        else:
            break

    while True:
        apellido = input("Ingrese el apellido del paciente: ")
        if any(chr.isdigit() for chr in apellido):
            print("Revise el apellido :(")
        else:
            break
   
    while True:
        try:
            ticket = int(input("Ingrese número de ticket: "))
            break
        except ValueError: 
            print("Valor inválido")


    while True:
        try:
            historia = int(input("Ingrese el número de historia: "))
            break
        except ValueError: 
            print("Valor inválido para una historia")

    while True:
        try:
            documento_prof = int(input("Ingrese el número de documento del medico que atiende: "))
            if documento_prof > 10**6:
                break
            print("Confirme documento del profesional")
        except ValueError: 
            print("No es un número válido")

    while True:
        try:
            profesional = int(input("Ingrese la identificación profesional del médico que atiende: "))
            if documento_prof > 10**6:
                break
            print("Confirme documento, por favor")
        except ValueError: 
            print("No es una identificación válida")

    eps = input("Ingrese la EPS del paciente: ") 
    entrada =input("Ingrese la fecha/hora de entrada: ")
    salida =input("Ingrese la fecha/hora de salida: ")
    hospitalizacion =input("Ingrese hospitalización o consulta: ")
    ubicacion =input("Ingrese la ubicación en la que fue internado el paciente: ")
    alta =input("Ingrese el tipo de alta que se dio al paciente: ")

    info_administrativa_paciente= infoadministrativa(tipo_doc, documento, nombre, apellido, ticket, historia, documento_prof, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta)
    return info_administrativa_paciente.DFdata()



def agregarinfo_s():

    while True:
        nombre_prof = input("Ingrese el nombre del profesional: ")
        if any(chr.isdigit() for chr in nombre_prof):
            print("Revise el nombre :(")
        else:
            break

    while True:
        apellido_prof = input("Ingrese el apellido del profesional: ")
        if any(chr.isdigit() for chr in apellido_prof):
            print("Revise el apellido :(")
        else:
            break

    while True:
        tipo_doc = input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ").lower()
        if tipo_doc == "cc" or tipo_doc =="ti" or tipo_doc =="rc" or tipo_doc =="ce" or tipo_doc =="pp":
            break
        print("Ingrese un valor válido")

    while True:
        try:
            documento_prof = int(input("Ingrese el número de documento del profesional: "))
            if documento_prof > 10**6:
                break
            print("Confirme documento de identificación")
        except ValueError: 
            print("No es un número válido")

    while True:
        try:
            tarjetaprof = int(input("Ingrese la identificación profesional del médico que atiende: "))
            if tarjetaprof > 10**6:
                break
            print("Confirme documento, por favor")
        except ValueError: 
            print("No es una identificación válida")

    especialidad = input("Ingrese la especializacion (en caso de no tener coloque no): ")
    consultorio  = input("Numero de consultorio donde se ubica al profesional: ")

    info_profesional_salud= infoprofesional(nombre_prof,apellido_prof, tipo_doc, documento_prof, tarjetaprof, especialidad, consultorio)
    return info_profesional_salud.DFdata()


def agregarinfo_f():
    while True:
        try:
            ticket = int(input("Ingrese el ticket de atención: "))
            break
        except ValueError: 
            print("Valor inválido")

    while True:
        try:
            documento = int(input("Ingrese el número de documento: "))
            if documento > 10**6:
                break
            print("Confirme documento de identificación")
        except ValueError: 
            print("No es un número válido")

    while True:
        try:
            historia = int(input("Ingrese el número de historia: "))
            break
        except ValueError: 
            print("Valor inválido para una historia")

    farmaceutica = input("Ingrese el nombre del farmacéutico que atiende: ")

    while True:
        try:
            profesional = int(input("Ingrese el numero de tarjeta profesional del farmacéutico: "))
            if profesional > 10**6:
                break
            print("Confirme tarjeta profesional del farmacéutico")
        except ValueError: 
            print("No es un número válido")    

 
    medicamento = input("Ingrese medicamento en ml: " )
    laboratorio = input("Ingrese el laboratorio: ")

    while True:
        try:
            codigo = int(input("Ingrese el código del medicamento: "))
            if codigo > 10**6:
                break
            print("Confirme el código del medicamento")
        except ValueError: 
            print("No es un código válido") 
 
    administracion= input("Ingrese vía de administración del medicamento: ")

    while True:
        try:
            cantidad = int(input("Ingrese dosis de medicamento: "))
            if cantidad < 1000:
                break
            print("Confirme número de dosis")
        except ValueError: 
            print("No es un número válido")    

    entrega = str(input("ingrese fecha de entrega de medicamento (YYYY-MM-DD): "))

    info_farmaceutica= infofarmaceutica(ticket, documento, historia, farmaceutica, profesional, medicamento, laboratorio, codigo, administracion, cantidad, entrega)
    return info_farmaceutica.DFdata()

# las funciones lista_ en general tienen la intencion de compilar en una "lista" la informacion que se va compilando
# de los diferentes pacientes dichas "listas" son vistas en forma de dataframe donde cada componente tiene su nombre respectivo 
# al dato que pertenece 

def lista_p():
    print("--Listado de informacion basica de pacientes--")
    for infopersonalpaciente in listapacientes:
        print(infopersonalpaciente)


def lista_m():
    print("--listado sobre la informacion medica del paciente--")
    for infomedica in listainfomedica:
        print(infomedica)


def lista_a():
    print("--informacion administrativa--")
    for infoadministrativa in listainfoadministrativa:
        print(infoadministrativa)


def lista_s():
    print("--Información de los profesionales--")
    for infoprofesional in listaprofesionales:
        print(infoprofesional)


def lista_f():
    print("--Informacion para las recetas de medicamentos--")
    for infofarmaceutica in listafamaceutica:
        print(infofarmaceutica)


informacion = " "
listapacientes = pd.DataFrame(columns=["tipo_doc", "documento", "nombre", "apellido", "numero_contacto",
 "ciudad_residencia","estado_civil", "nacionalidad", "numero_emergencia", "ultima_actulizacion"])

listainfomedica= pd.DataFrame(columns=["tipo_doc", "documento", "historia", "edad", "sexo", "RH", "sanguineo", 
        "peso", "estatura", "reanimacion", "alergias", "comorbilidades", "embarazos", "FUM", "observaciones",
        "remision", "especialista", "medicacion", "actualizacion"])

listainfoadministrativa= pd.DataFrame(columns=["tipo_doc", "documento", "nombre", "apellido", "ticket", "historia",
        "documento_prof", "profesional", "eps", "entrada", "salida", "hospitalizacion", "ubicacion", "alta"])

listaprofesionales = pd.DataFrame(columns=["nombre_prof", "apellido_prof", "tipo_doc", "documento_prof","tarjetaprof",
        "especialidad", "consultorio"])

listafamaceutica=pd.DataFrame(columns = ["ticket", "documento", "historia", "farmaceutica", "profesional",
        "medicamento", "laboratorio", "codigo", "administracion", "cantidad", "entrega"])
        