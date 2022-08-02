from datetime import datetime

"""
FUNCION PARA CREAR LOGS
"""

def crear_log(cantidad_res, query):
    
    marca_temporal = datetime.now().strftime('%H:%M')
    archi1=open("datos.txt","a+") 
    archi1.write("--------------------------------------------\n")
    archi1.write(f'Archivo creado: {marca_temporal}\n') 
    archi1.write(f'Se buscó el artículo: {query}\n') 
    archi1.write(f'Resultados encontrados: {cantidad_res}\n')
    archi1.write("--------------------------------------------\n")  
    archi1.close() 
