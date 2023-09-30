import datetime
import json
import requests
import threading
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from mandar_correo import Correo
from saber_sportium_selenium import Saber_de_sportium
import re
mandarcorreo=Correo()

#eleccion=int(input("Santafe(1) o Real madrid(2)  escoja entre '1 ó 2' "))
try:
    def coincidencia(str_peque,str_grande):
        lista_grande=str_grande.split(' ')
        lista_peque=str_peque.split(', ')
        lista_booleanos=[]
        for p in lista_peque:
            boleano=False
            for g in lista_grande:
                boleano=g==p
                if boleano:break
            lista_booleanos.append(boleano)        
        return all(lista_booleanos)
except:
    print("Error en las coincidencias")

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
         ,"Elan Chalon"
         ,"Vismane, Daniela"
         ,"Pavlou, Dimitra"
         ,"Norrkoping Dolphins"
         ,"Radisic, Nika"
         ,"De Vivo, Nicholas"
         ,"Kay, Simone"
         ,"Shnaider, Diana"
         ,"Kolyachev, Nikola"
         #,"Limoges CSP"#hasta el 30 de abril
        
        ]#REVISAR ADKAR Y NAGATA


backup_nombres=[]
for x in range(0,len(nombres)):
    backup_nombres.append(nombres[x])

def timer(timer_runs):
    while timer_runs.is_set():
        
        
        
        print("")
       
        try:
            hora_objetivo1 = datetime.time(0, 7, 0)
            hora_objetivo2 = datetime.time(0, 13, 0)
            hora_actual = datetime.datetime.now().time()
    
            if hora_actual >= hora_objetivo1 and hora_actual <= hora_objetivo2:
                sportium=Saber_de_sportium()
                x=sportium.saber_de_sportium ()
                for nombre in nombres:
                    

                    if nombre=="Claire, Liu": 
                        print(nombre)
                    for nombre_sportium in x:
                        if  coincidencia(nombre,nombre_sportium["equipo1"]):
                            mandarcorreo.enviar_correo("apostar por "+nombre+"\n"+json.dumps(nombre_sportium, indent=5))
                            print("Alerta "+json.dumps(nombre_sportium, indent=5))
                        elif coincidencia(nombre,nombre_sportium["equipo2"]):
                            mandarcorreo.enviar_correo("apostar por "+nombre+"\n"+json.dumps(nombre_sportium, indent=5))
                            print("Alerta "+json.dumps(nombre_sportium, indent=5))
                        else:
                            pass
            else:
                print("El programa se salio de la hora")
                
        except:
            print("Error en el server")
        
        time.sleep(120)
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