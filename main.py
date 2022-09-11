from datetime import date,datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
import numpy as np
import pandas as pd

class infopersonalpaciente:
    def __init__(self, tipo_doc,documento, nombre, apellido, numero_contacto, ciudad_residencia, estado_civil, nacionalidad, numero_emergencia, ultima_actualizacion):
        self.tipo_doc=tipo_doc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.numero_contacto=numero_contacto
        self.ciudad_residencia=ciudad_residencia
        self.estado_civil=estado_civil
        self.nacionalidad= nacionalidad
        self.numero_emergencia=numero_emergencia
        self.ultima_actulizacion= ultima_actualizacion
    
    def paiente(self):
        """
        Esta funcion tinene el proposito de dar un resumen informativo acerca de los datos proporcionados por el paciente en cuestion al que 
        pertenecen los datos mediante un return 

        """
        #dict={"tipo_doc":self.tipo_doc, "documento": self.documento,"nombre" :self.nombre, "apellido":self.apellido,"numero_contacto": self.numero_contacto,"ciudad_residencia": self.ciudad_residencia, "estado_civil":self.estado_civil, "nacionalidad":self.nacionalidad, "numero_emergencia": self.numero_emergencia,"ultima_actualizacion":self.ultima_actulizacion}
        #df=pd.DataFrame(dict)
        #return(df)
        
        return(f"El paciente {self.nombre} {self.apellido}, identificado con {self.tipo_doc} {self.documento} con nacionalidad {self.nacionalidad} reside en {self.ciudad_residencia}, se encuentra {self.estado_civil} y cuenta con un el numero {self.numero_contacto} para contactarlo y para cualquier emergencia se cuenta con el numero {self.numero_emergencia}")

class infopaciente:
    def __init__(self,tipo_doc,documento,apellido,nombre):
        infopersonalpaciente.__init__(tipo_doc,documento, nombre, apellido)
    def paciente(self):
        pass
        #return(f"El paciente {self.nombre} {self.apellido}, identificado con {self.tipo_doc} {self.documento}")

class infomedica:

    def __init__(self, tipo_doc,documento, historia, edad, sexo, RH, sanguineo, peso, estatura, reanimacion, alergias, comorbilidades, embarazos, FUM, observaciones, remision, especialista, medicacion, actualizacion):
        self.tipo_doc=tipo_doc
        self.documento=documento
        self.historia=historia
        self.edad=edad
        self.sexo=sexo
        self.RH=RH
        self.sanguineo=sanguineo
        self.peso=peso
        self.estatura=estatura
        self.reanimacion=reanimacion
        self.alergias=alergias
        self.comorbilidades=comorbilidades
        self.embarazos=embarazos
        self.FUM=FUM
        self.observaciones=observaciones
        self.remision=remision
        self.especialista=especialista
        self.medicacion=medicacion
        self.actualizacion=actualizacion
    def medica(self) -> str:
        """
        esta funcion cumple con el proposito de dar un descripcion detallada de la informacion 
        medica del paciente proporcionada por el mismo con la ayuda de un return 
            
        """
        
        return(f"El paciente de sexo {self.sexo} identificado con {self.tipo_doc} el {self.documento} posee una edad de {self.edad} años, un peso de {self.peso} y una estatura de {self.estatura}, cuenta con un tipo de sangre {self.RH}{self.sanguineo}, es alegrico a: {self.alergias}, posee las siguientes comorbilidades: {self.comorbilidades},  el paciente respecto con ser reanimado en caso de que se complique su salud dijo que {self.reanimacion}, ha tenido hasta la fecha {self.embarazos} embarazos y la fecha de su ultima mestruacion fue {self.FUM}, ante su visita al doctor se le hicieron las siguientes observaciones: {self.observaciones} , ademas, requirio una remision {self.remision} ante el especialista de {self.especialista}, el doctor le receto {self.medicacion}. Todo esto a la fecha de {self.actualizacion} ")



class infoadministrativa:
    def __init__(self, tipo_doc, documento, nombre, apellido, ticket, historia, documento_prof, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta):
        self.tipo_doc=tipo_doc
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.ticket=ticket
        self.historia=historia
        self.documento_prof=documento_prof
        self.profesional=profesional
        self.eps=eps
        self.entrada=entrada
        self.salida=salida
        self.hospitalizacion=hospitalizacion
        self.ubicacion=ubicacion
        self.alta=alta
    
    def __str__(self) -> str:
        """
        Esta funcion tiene la caracteristica de relatar la informacion administrativa acerca del paciente. 
        """
        
        pass
        #return(El paciente super().paciente())
        #el paciente (pepito) (perez) identificado con la (cedula) (numero) fue con un ticket de atencion el dia (entrada) a una (hospitalizacion) a cargo del (profesional) identificado con (numero profesional)
        #gracias a la entidad de seguros (eps) que cubrio todo.

class infoprofesional:
    def __init__(self, nombre_prof, apellido_prof, tipo_doc, documento_prof, tarjetaprof, especialidad, consultorio):
        self.nombre_prof=nombre_prof
        self.apellido_prof=apellido_prof
        self.tipo_doc=tipo_doc
        self.documento_prof=documento_prof
        self.tarjetaprof=tarjetaprof
        self.especialidad=especialidad
        self.conslutorio=consultorio
    
    def __str__(self) -> str:
        """
        Esta funcion nos genera un resumen de la informacion del profesional que en cuestion atiende al paciente mediante un return convierte el 
        resumen de los datos en una variable type string 
        """

        pass
        #El profesional nombre apellido identificado con la tipo_doc documento se identifica con la tarjeta profesional (tarjetaprof) especializado en, ubicado en el consultorio 



class infofarmaceutica:
    def __init__(self, ticket, documento, historia, farmaceutica, profesional, medicamento, laboratorio, codigo, administracion, cantidad, entrega):
        self.ticket=ticket
        self.documento=documento
        self.historia=historia
        self.farmaceutica=farmaceutica
        self.profesional=profesional
        self.medicamento=medicamento
        self.laboratorio=laboratorio
        self.codigo=codigo
        self.administracion=administracion
        self.cantidad=cantidad
        self.entrega=entrega
    
    
    def __str__(self) -> str:
        """
        Esta funcion tiene el oficio de resumir el proceso donde un farmaceutico le entrega a un 
        paciente el medicamento que le preescribio el medico anteriormente recetado donde se especifica el medicamento, la dosis 
        y la aplicacion del mismo 

           
        """
        pass
        #return(f"el farmaceutica identificado con (tarjeta profesional)  del laboratorio, le suministro al paciente identificado con el (numero) el medicamento () con codigo (), el medicamento se debe administrar () con una dosis de () ")



listafamaceutica=[]

listaprofesionales=[]

listainfoadministrativa= []

listainfomedica= []

listapacientes = []







def agregarinfo_p():
    tipo_doc= input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ")
    documento= input("Ingrese el documento del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    numero_contacto =input("Ingrese el numero de contacto: ") 
    ciudad_residencia =input("Ingrese la ciudad de residencia: ")
    estado_civil =input("Ingrese el estado civil: ")
    nacionalidad =input("Ingrese la nacionalidad:  ")
    numero_emergencia =input("Ingrese un numero contacto de emergencia: ")
    ultima_actualizacion =input("Ingrese la fecha de la ultima visita (año,mes,dia): ")

    Paciente= infopersonalpaciente(tipo_doc, documento, nombre, apellido, numero_contacto, ciudad_residencia, estado_civil, nacionalidad, numero_emergencia, ultima_actualizacion)
    listapacientes.append(Paciente)
    df= pd.DataFrame(listapacientes)
    #df.set_index(documento)
    df.to_csv(r'C:\Users\DELL\OneDrive\Desktop\Idea#2\listapaciente.txt')


    #print(Paciente)


def agregarinfo_m():
    tipo_doc = input("Ingrese tipo de documento (cc,ti,rc,ce,pp): ")
    documento = input("Ingrese el numero de documento: ")
    historia = input("Ingrese el numero de la historia clinica: ") #?
    edad = input("Ingrese la edad del paciente: ")
    sexo = input("Ingrese el sexo del paciente: ")
    RH = input("Ingrese el RH al que pertenece el paciente (+,-): ")
    sanguineo = input("Ingrese el grupo sanguineo del paciente (A, B, O, AB): ")
    peso = input("Ingrese el peso del paciente: ")
    estatura = input("Estatura del paciente: ")
    reanimacion =  input("En caso de que se complique su salud, el paciente esta deacuerdo con ser reanimado (si, no): ")
    alergias = input("A que es alergico el paciente: ")
    comorbilidades = input("ingrese las comorbilidades del paciente: ")
    embarazos = input("Cantidad de embarazos hasta la fecha: ")
    FUM = input("Fecha de la ultima mestruación: ")
    observaciones = input("Observaciones medicas: ")
    remision = input("El paciente requirio remision a un especialista (si,no): ")
    especialista = input("Tipo de especialista al que fue remitido el paciente: ")
    medicacion = input("Medicación resetada por el doctor que vio al paciente: ") 
    actualizacion = input("Ingrese la fecha de la ultima actualizacion de datos (año,mes,dia):") 

    info_medica_paciente=infomedica(tipo_doc,documento, historia, edad, sexo, RH, sanguineo, peso, estatura, reanimacion, alergias, comorbilidades, embarazos, FUM, observaciones, remision, especialista, medicacion, actualizacion)
    listainfomedica.append(info_medica_paciente)
    df1= pd.DataFrame(listainfomedica)
    #df.set_index(documento)
    df1.to_csv(r'C:\Users\DELL\OneDrive\Desktop\Idea#2\listainformacionmedica.txt')




def agregarinfo_a():
    tipo_doc= input("Ingrese tipo de documento (cc, ti, rc, ce, pp): ")
    documento= input("Ingrese el documento del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    ticket = input("Ingrese el ticket de atención: ")
    historia= input("Ingrese el número de la historia clínica del paciente: ")
    documento_prof = input("Ingrese el número de documento del medico que atiende: ")
    profesional = input("Ingrese la identificación profesional del médico que atiende: ")
    eps =input("Ingrese la EPS del paciente: ") 
    entrada =input("Ingrese la fecha/hora de entrada: ")
    salida =input("Ingrese la fecha/hora de salida: ")
    hospitalizacion =input("Ingrese hospitalización o consulta: ")
    ubicacion =input("Ingrese la ubicación en la que fue internado el paciente: ")
    alta =input("Ingrese el tipo de alta que se dio al paciente: ")

    info_administrativa_paciente= infoadministrativa(tipo_doc, documento, nombre, apellido, ticket, historia, documento_prof, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta)
    listainfoadministrativa.append(info_administrativa_paciente)
    df2= pd.DataFrame(listainfoadministrativa)
    #df.set_index(documento)
    df2.to_csv(r'C:\Users\DELL\OneDrive\Desktop\Idea#2\listainformacionadministrativa.txt')



def agregarinfo_s():
    nombre_prof = input("Ingrese el nombre del profesional que atendio al paciente: ")
    apellido_prof = input("Ingrese el apellido del profesional que atendio al paciente: ")
    tipo_doc = input("Ingrese tipo de documento (cc,ti,rc,ce,pp): ")
    documento_prof = input("Numero de documento: ")
    tarjetaprof = input("Numero de la tarjeta profesional: ")
    especialidad = input("Ingrese la especializacion (en caso de no tener coloque no): ")
    consultorio  = input("Numero de consultorio donde se ubica al profesional: ")

    info_profesional_salud= infoprofesional(nombre_prof,apellido_prof, tipo_doc, documento_prof, tarjetaprof, especialidad, consultorio)
    listaprofesionales.append(info_profesional_salud)
    df3= pd.DataFrame(listaprofesionales)
    #df.set_index(documento)
    df3.to_csv(r'C:\Users\DELL\OneDrive\Desktop\Idea#2\listadatosprofesionales.txt')




def agregarinfo_f():
    ticket= str(input("Ingrese el ticket de atención: ")),
    documento = int(input("Ingrese número de documento: ")),
    historia= int(input("ingrese el número de historia: ")),
    farmaceutica = str(input("Ingrese el nombre del farmacéutico que atiende: ")), 
    profesional= int(input("Ingrese el numero de tarjeta profesional del farmacéutico: ")), 
    medicamento = str(input("Ingrese medicamento: " )),
    laboratorio = str(input("Ingrese el laboratorio: ")), 
    codigo = str(input("Ingrese el código del medicamento: ")), 
    administracion= str(input("Ingrese vía de administración del medicamento: ")),
    cantidad = int(input("Ingrese dosis de medicamento: ")),
    entrega = str(input("ingrese fecha de entrega de medicamento: "))

    info_farmaceutica= infofarmaceutica(ticket, documento, historia, farmaceutica, profesional, medicamento, laboratorio, codigo, administracion, cantidad, entrega)
    listafamaceutica.append(info_farmaceutica)
    df4= pd.DataFrame(listafamaceutica)
    #df.set_index(documento)
    df4.to_csv(r'C:\Users\DELL\OneDrive\Desktop\Idea#2\listarecetasfarmaceutica.txt')



def lista_p():
    print("--Listado de pacientes--")
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
    print("--listado de profesionales--")
    for infoprofesional in listaprofesionales:
        print(infoprofesional)


def lista_f():
    print("--listado recetas medicamentos--")
    for infofarmaceutica in listafamaceutica:
        print(infofarmaceutica)





informacion = " "
while( informacion != "x"):
    print("---- Base de Datos Hospital Universidad de Antioquia ----")
    print("p - informacion personal del paciente")
    print("m - informacion medica del paciente")
    print("a - informacion administrativa del paciente")
    print("s - informacion profesional de la salud") 
    print("f - informacion farmaceutica")
    print("x - salir de la base de datos")
    informacion = input("Ingrese el tipo de información a la que desea acceder: ")
    if( informacion == "x"):
        print("Cerrando cesión del sistema ")
    if( informacion == "p"):
        #print("a - agregar informacion nueva")
        #print("m - modificar informacion existente")
        #opcion = print("selecciona la opcion que necesitas: ")
        agregarinfo_p ()
        lista_p()
        
        #if(opcion == "a"):
            #agregarinfo_p()
            #lista_p()
        #elif(opcion == "m"):
            #pass 


    elif( informacion == "m"):
        agregarinfo_m()
        lista_m()

    elif(informacion == "a"):
        agregarinfo_a()
        lista_a()
    
    elif(informacion == "s"):
        agregarinfo_s()
        lista_s()
    elif(informacion == "f"):
        agregarinfo_f()    
        lista_f()