# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:49:37 2022

@author: MatiOliva
"""

import numpy as np
import math

# Otras funciones utiles
def TransferenciaTeorica_RC_ideal(RL,C,f_inicio = 1000,f_final = 2000000, num = 1000):
    """    
    Funcion para obtener la funcion de transferencia de un filtro RC diferencial ideal
    
    Uso:
    ----------
        f,H = TransferenciaTeorica_RC_ideal(RL,C,f_inicio,f_final,num)
        
        f: Frecuencias a las que esta calculada la transferencia
        H: Transferencia (compleja) del sistema


    Parametros
    ----------
    RL :                Parametro requerido
        Descripción:    Resistencia del circuito
        
    C :                 Parametro requerido
        Descripción:    Capacidad del circuito
        
    f_inicio :          Parametro opcional
        Descripción:    Frecuencia de inicio de la transferencia
                        Por default es: 1000 Hz
                        
    f_final :           Parametro opcional
        Descripción:    Frecuencia final de la transferencia
                        Por default es: 2000000 Hz
    
    num :               Parametro opcional
        Descripción:    Cantidad de puntos para calcular la transferencia
                        Por default es: 1000
                            
    """
    
    f=np.linspace(f_inicio,f_final,num)
    w=np.multiply(2*math.pi,f)
    s=1j*w
    
    H = 1 / (1 + np.multiply(s , 2*C*RL))
    return f,H

