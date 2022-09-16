from datetime import date, datetime
from mailbox import NoSuchMailboxError
from pydoc import doc
#import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=Warning)

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

    def DFdata(self):
        """
        esta función cumple con el proposito de dar una descripción detallada de la información 
        medica del paciente proporcionada por el mismo, todo esto compliado en un dataframe para su 
        mayor comprensión. 
            
        """

        self.atributos = [self.tipo_doc, self.documento, self.historia, self.edad, self.sexo, self.RH,
        self.sanguineo, self.peso, self.estatura, self.reanimacion, self.alergias, self.comorbilidades,
        self.embarazos, self.FUM, self.observaciones, self.remision, self.especialista, self.medicacion,
        self.actualizacion]
        self.indices =  ["tipo_doc", "documento", "historia", "edad", "sexo", "RH", "sanguineo", 
        "peso", "estatura", "reanimacion", "alergias", "comorbilidades", "embarazos", "FUM", "observaciones",
        "remision", "especialista", "medicacion", "actualizacion"]
        self.Serie = pd.Series(self.atributos, index = self.indices)
        return self.Serie

 