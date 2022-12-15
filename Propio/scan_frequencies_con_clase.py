# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:16:10 2022

@author: MatiOliva
"""

from sr865_functions import sr865 
from sr865_functions import OpcionesCaptura
from funciones_transferencias import TransferenciaTeorica_RC_ideal
import time
import pylab as pl
import math
import numpy as np

# Adquisicion

ip_addr = '192.168.1.4'
variables_a_capturar = OpcionesCaptura.XYRT
cantidad_datos_x_frecuencia = 1
tension=200
graficar = True

frec_inicial = 1000
frec_final = 20000
delta = 500

f = range(frec_inicial,frec_final+1,delta)

sr865_inst = sr865(ip_addr)
sr865_inst.set_tension_referencia(tension)
sr865_inst.set_frecuencia_referencia(f[0])
time.sleep(2)

resultados = []

for frec in f:
    sr865_inst.set_frecuencia_referencia(frec)
    time.sleep(1)
    dato = sr865_inst.configurar_buffer_y_capturar(cantidad_datos_x_frecuencia, variables_a_capturar)    
    dato[0].insert(0, frec)
    resultados.append(dato[0])
    
# Guardado de datos en CSV
sr865_inst.write_data_to_file('Datos.txt',variables_a_capturar,resultados)


# Si quiero graficar y estoy obteniendo todos los datos XYRT entonces le mando
if((variables_a_capturar == OpcionesCaptura.XYRT) and graficar) :
    frecuencias=[]
    tensiones=[]
    fases=[]

    for r in resultados:
        frecuencias.append(r[0])
        tensiones.append(r[3]/(tension/1000 * 2))
        fases.append(r[4])

    # Resultados Teoricos:
    # Valores de los componentes
    R=1e3
    C=15e-9
    fc=1/(2*math.pi*R*2*C)

    [f_teoricas,H_teorica] =  TransferenciaTeorica_RC_ideal(R,C,frec_inicial,frec_final, len(f))
        
    figure, axes = pl.subplots(nrows=2, ncols=1)       

    # Graficos
    pl.suptitle("Transferencia obtenida")
        
    pl.subplot(2,1,1)
    pl.semilogx(frecuencias,tensiones)
    pl.semilogx(f_teoricas, np.abs(H_teorica))
    pl.xlabel("Frecuencia del Lock In")
    pl.ylabel("Amplitud")
    pl.grid()
        
    pl.subplot(2,1,2)
    pl.semilogx(frecuencias,fases)
    pl.semilogx(f_teoricas, np.angle(H_teorica)*180/math.pi)
    pl.xlabel("Frecuencia del Lock In")
    pl.ylabel("Fase")
    pl.grid()





    
