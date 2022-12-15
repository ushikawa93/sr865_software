# sr865_software
Funcionalidades para controlar un lockin sr865 de stanford en forma remota

## Ejemplos
Ejemplos escritos en Python que encontre por ahi. Tiene opciones para capturar datos una unica vez y otro para hacer streaming de datos (este ultimo por ahora no lo probe)

## Propio
Aca lo importante es el archivo sr865_functions.py, tiene una clase llamada sr865 que tiene varias funcionalidades del lockin
La conexión se realiza via Ethernet. Hay que configurar el IP en el dispositivo y en el programita. Por ahora usé '192.168.1.4'.
Hay métodos con las cosas que mas uso, y uno generico mas sendCommand que le metes un string y mandas el comando que quieras (mirar en el manual los comandos disponibles)

Despues el archivo scan_frecuencies_con_clase.py emplea esta clase, hace un scan de frecuencias en el lockin y lo guardaa en un archivo
Tambien puede graficar esta transferencia al final y compararla con una RC diferencial teórica (estaba usando una carga asi para probar la cuestion)

Carga RC diferencial (Vout y Vin son respecto al Lockin)

	#    Vout+ ------ R -----|----------- Vin+ 
    #                        |              
    #                                       
    #                        C              
    #                                      
    #                        |             
    #    Vout- ------ R -----|----------- Vin- 
