from datetime import date,datetime
from pydoc import doc

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
        self.ultima_actulizacion= (ultima_actualizacion)
    def __str__(self):
        return(f"Paciente {self.nombre} {self.apellido}, identificado con {self.tipo_doc} {self.documento} con número de contacto {self.numero_contacto}, reside en {self.ciudad_residencia}")
        

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
    def __str__(self) -> str:
        pass


class infoadministrativa:
    def __init__(self, ticket, historia, documento, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta):
        self.ticket=ticket
        self.historia=historia
        self.documento=documento
        self.profesional=profesional
        self.eps=eps
        self.entrada=entrada
        self.salida=salida
        self.hospitalizacion=hospitalizacion
        self.ubicacion=ubicacion
        self.alta=alta
    
    def __str__(self) -> str:
        pass

class infoprofesional:
    def __init__(self, nombre, tipo_doc, documento, tarjetaprof, especialidad, consultorio):
        self.nombre=nombre
        self.tipo_doc=tipo_doc
        self.documento=documento
        self.tarjetaprof=tarjetaprof
        self.especialidad=especialidad
        self.conslutorio=consultorio
    
    def __str__(self) -> str:
        pass



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
        pass



def agregarinfo_p():
    while True:
        tipo_doc = str(input("Ingrese tipo de documento (cc, ti, rc, ce, pp): "))
        if tipo_doc == ("cc" or "ti" or "rc" or "ce" or "pp"):
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
        nombre = str(input("Ingrese el nombre del paciente: "))
        if any(chr.isdigit() for chr in nombre):
            print("Revise el nombre :(")
        else:
            break

    while True:
        apellido = str(input("Ingrese el apellido del paciente: "))
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
        ciudad_residencia = str(input("Ingrese la ciudad de residencia: "))
        if any(chr.isdigit() for chr in ciudad_residencia):
            print("Revise la ciudad de residencia :(")
        else:
            break

    while True:
        estado_civil = str(input("Ingrese el estado civil: "))
        if any(chr.isdigit() for chr in estado_civil):
            print("Revise el estado civil :(")
        else:
            break

    while True:
        nacionalidad = str(input("Ingrese la nacionalidad:  ")))
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

    ultima_actualizacion =input("Ingrese la fecha de la ultima visita (año,mes,dia): ")

    Paciente= infopersonalpaciente(tipo_doc, documento, nombre, apellido, numero_contacto, ciudad_residencia, estado_civil, nacionalidad, numero_emergencia, ultima_actualizacion)
    listapacientes.append(Paciente)
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




def agregarinfo_a():
    ticket = input("Ingrese el ticket de atención: ")
    historia= input("Ingrese el número de la historia clínica del paciente: ")
    documento = input("Ingrese el número de documento del medico que atiende: ")
    profesional = input("Ingrese la identificación profesional del médico que atiende: ")
    eps =input("Ingrese la EPS del paciente: ") 
    entrada =input("Ingrese la fecha/hora de entrada: ")
    salida =input("Ingrese la fecha/hora de salida: ")
    hospitalizacion =input("Ingrese hospitalización o consulta: ")
    ubicacion =input("Ingrese la ubicación en la que fue internado el paciente: ")
    alta =input("Ingrese el tipo de alta que se dio al paciente: ")

    info_administrativa_paciente= infoadministrativa(ticket, historia, documento, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta)
    listainfoadministrativa.append(info_administrativa_paciente)



def agregarinfo_s():
    nombre = input("Ingrese el nombre del profesional que atendio al paciente: ")
    tipo_doc = input("Ingrese tipo de documento (cc,ti,rc,ce,pp): ")
    documento = input("Numero de documento: ")
    tarjetaprof = input("Numero de la tarjeta profesional: ")
    especialidad = input("Ingrese la especializacion (en caso de no tener coloque no): ")
    consultorio  = input("Numero de consultorio donde se ubica al profesional: ")

    info_profesional_salud= infoprofesional(nombre, tipo_doc, documento, tarjetaprof, especialidad, consultorio)
    listaprofesionales.append(info_profesional_salud)




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








def lista():
    print("--Listado de pacientes--")
    for infopersonalpaciente in listapacientes:
        print(infopersonalpaciente)

listafamaceutica=[]

listaprofesionales=[]

listainfoadministrativa= []

listainfomedica= []

listapacientes = []

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
        print("Cerrando cesión del sistema: ")
    elif( informacion == "p"):
        agregarinfo_p()
        lista()
        #print("A - Agregar informacion personal de un paciente: ")
        #print("M - modificar informacion de un paciente")
        #print("L - lista de pacientes")
        #opcion=print("Seleccione la opcion que necesita: ")
        #if(opcion == "a"):
            #agregarinfo_p()
        #elif(opcion == "m"):
            #pass
        #elif(opcion == "l"):
            #lista()
    elif( informacion == "m"):
        agregarinfo_m()

    elif(informacion == "a"):
        agregarinfo_a()
    
    elif(informacion == "s"):
        agregarinfo_s()

    elif(informacion == "f"):
        agregarinfo_f()    
