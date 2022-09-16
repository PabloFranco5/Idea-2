from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)

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
    
    def DFdata(self):
        """
        Esta función tiene el oficio de resumir el proceso donde un farmaceutico le entrega a un 
        paciente el medicamento que le preescribio el medico anteriormente recetado donde se especifica 
        el medicamento, la dosis y la aplicación del mismo, todo es devuelto en forma de un dataframe.

           
        """
        self.atributos = [self.ticket, self.documento, self.historia, self.farmaceutica, self.profesional,
        self.medicamento, self.laboratorio, self.codigo, self.administracion, self.cantidad, self.entrega]

        self.indices =  ["ticket", "documento", "historia", "farmaceutica", "profesional",
        "medicamento", "laboratorio", "codigo", "administracion", "cantidad", "entrega"]
        self.Serie = pd.Series(self.atributos, index = self.indices)
        return self.Serie


