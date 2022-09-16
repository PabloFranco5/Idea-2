from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)

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

    def DFdata(self):
        """
        Esta función tinene el proposito de dar un resumen informativo acerca de los datos basicos y de contacto 
        proporcionados por el paciente en cuestión mediante un dataframe.

        """
        
        self.atributos = [self.tipo_doc, self.documento, self.nombre, self.apellido, self.numero_contacto,
        self.ciudad_residencia, self.estado_civil, self.nacionalidad, self.numero_emergencia, self.ultima_actulizacion]
        self.indices =  ["tipo_doc", "documento", "nombre", "apellido", "numero_contacto", "ciudad_residencia",
        "estado_civil", "nacionalidad", "numero_emergencia", "ultima_actulizacion"]
        self.Serie = pd.Series(self.atributos, index = self.indices)
        return self.Serie
    

