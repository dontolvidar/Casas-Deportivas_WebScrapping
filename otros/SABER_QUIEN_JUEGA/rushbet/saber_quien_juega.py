import datetime
import requests
import threading
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from mandar_correo import Correo

mandarcorreo=Correo()
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

nombres_formateados = []
for string in nombres:
    string_modificado = string.replace(" ", "%20")
    nombres_formateados.append(string_modificado)
print(nombres_formateados)

backup_nombres=[]
backup_nombres_formateados = []
for x in range(0,len(nombres)):
    backup_nombres.append(nombres[x])
    backup_nombres_formateados.append(nombres_formateados[x])
    
    
    
def timer(timer_runs):
    while timer_runs.is_set():
        
        
        
        i=0
        print("")
        for nombre in nombres_formateados:
            try:
                url = f"https://www.rushbet.co/api/service/sportsbook/misc/search?queryString="+nombre+"&cageCode=57"
                headers = {
                    "charset": "UTF-8",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip,deflate,br",
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Referer": "http://www.rushbet.co",
                }
                response = requests.get(url, headers=headers)
                
                if response.text=='[]':
                    print (str(i)+" "+nombres[i]+" NO esta")
                else:
                    mandarcorreo.enviar_correo(nombres[i])
                    print("Alerta "+ (str(i)+" "+nombres[i]+" SI ESTA !"))
                    del nombres[i]
                    del nombres_formateados[i]
                    
                    
                hora_objetivo1 = datetime.time(23, 53, 0)
                hora_objetivo2 = datetime.time(23, 56, 0)
                hora_actual = datetime.datetime.now().time()
                if hora_actual >= hora_objetivo1 and hora_actual <= hora_objetivo2:
                    nombres.clear()
                    nombres_formateados.clear()
                    for x in range(0,len(backup_nombres)):
                        nombres.append(backup_nombres[x])
                        nombres_formateados.append(backup_nombres_formateados[x])
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