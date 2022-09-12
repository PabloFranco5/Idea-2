from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)

class infoprofesional:
    def __init__(self, nombre_prof, apellido_prof, tipo_doc, documento_prof, tarjetaprof, especialidad, consultorio):
        self.nombre_prof=nombre_prof
        self.apellido_prof=apellido_prof
        self.tipo_doc=tipo_doc
        self.documento_prof=documento_prof
        self.tarjetaprof=tarjetaprof
        self.especialidad=especialidad
        self.consultorio=consultorio


    def DFdata(self):
        """
        Esta función nos genera un resumen de la información del profesional que en cuestión 
        atiende al paciente mediante un return convierte el 
        resumen de los datos en dataframe.
        """

        self.atributos = [self.nombre_prof, self.apellido_prof, self.tipo_doc, self.documento_prof,
        self.tarjetaprof, self.especialidad, self.consultorio]
        self.indices =  ["nombre_prof", "apellido_prof", "tipo_doc", "documento_prof","tarjetaprof",
        "especialidad", "consultorio"]
        self.Serie = pd.Series(self.atributos, index = self.indices)
        return self.Serie
    
 

