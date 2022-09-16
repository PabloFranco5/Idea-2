from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)


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

    def DFdata(self):
        """
        Esta función tiene la caracteristica de compliar la información administrativa acerca 
        del paciente mediante un dataframe. 
        """

        self.atributos = [self.tipo_doc, self.documento, self.nombre, self.apellido, self.ticket,
        self.historia, self.documento_prof, self.profesional, self.eps, self.entrada, self.salida,
        self.hospitalizacion, self.ubicacion, self.alta]
        self.indices =  ["tipo_doc", "documento", "nombre", "apellido", "ticket", "historia",
        "documento_prof", "profesional", "eps", "entrada", "salida", "hospitalizacion", "ubicacion", "alta"]
        self.Serie = pd.Series(self.atributos, index = self.indices)
        return self.Serie
    
 