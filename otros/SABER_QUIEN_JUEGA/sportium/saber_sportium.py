import datetime
import json
import requests
import threading
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from mandar_correo import Correo
from saber_sportium_selenium import Saber_de_sportium
mandarcorreo=Correo()
sportium=Saber_de_sportium()
#eleccion=int(input("Santafe(1) o Real madrid(2)  escoja entre '1 ó 2' "))
nombres=["Karatancheva, Lia"
         ,"Faria, Jaime"#activenme miercoles
         ,"Blanch, Dali"
         ,"Adkar"
         ,"Nagata"
         ,"Chopra, Keshav"
         ,"Douglas, Ellie"
         ,"Kestelboim, Mariano"
         ,"Sekulic, Philip"
         ,"Dolehide, Caroline"
         ,"Kiick, Allie"#activenme mañana
         ,"Peyre, Lucia"
         ,"Kozyreva, Maria"
         ,"Tikhonova, Anastasia"
         ,"Alexandrova, Ekaterina"
         ,"Corley, Carmen"
         
         #,"Limoges CSP"#hasta el 30 de abril
        
        ]#REVISAR ADKAR Y NAGATA


backup_nombres=[]
for x in range(0,len(nombres)):
    backup_nombres.append(nombres[x])

def timer(timer_runs):
    while timer_runs.is_set():
        
        
        
        i=0
        print("")
        x=sportium.saber_de_sportium ()
        for nombre in nombres:
            
            try:
                for nombre_sportium in x:
                    if nombre==nombre_sportium["equipo1"]:
                        mandarcorreo.enviar_correo(json.dumps(nombre_sportium, indent=5))
                        print("Alerta "+json.dumps(nombre_sportium, indent=5))
                        del nombres[i]
                    elif nombre==nombre_sportium["equipo2"]:
                        mandarcorreo.enviar_correo(json.dumps(nombre_sportium, indent=5))
                        print("Alerta "+json.dumps(nombre_sportium, indent=5))
                        del nombres[i]
                    else:
                        pass
                    
                
                
                """
                hora_objetivo1 = datetime.time(23, 53, 0)
                hora_objetivo2 = datetime.time(23, 56, 0)
                hora_actual = datetime.datetime.now().time()
                if hora_actual >= hora_objetivo1 and hora_actual <= hora_objetivo2:
                    nombres.clear()
                    nombres_formateados.clear()
                    for x in range(0,len(backup_nombres)):
                        nombres.append(backup_nombres[x])
                        nombres_formateados.append(backup_nombres_formateados[x])"""
            except:
                print("Error en el server")
            i+=1
        time.sleep(30)
try:
    timer_runs = threading.Event()
    timer_runs.set()
    t = threading.Thread(target=timer, args=(timer_runs,))
    t.start()
    # Esperar 10 segundos y luego detener el timer.
    #time.sleep(7200)
    #timer_runs.clear()
    print("¡El timer ha sido detenido!")
except:
    MessageBox.showinfo("Alerta","Se cerro el programa de saber quien juega")