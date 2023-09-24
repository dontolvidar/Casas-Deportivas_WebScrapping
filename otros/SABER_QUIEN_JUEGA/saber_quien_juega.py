import requests
import threading
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from mandar_correo import Correo

mandarcorreo=Correo()
#eleccion=int(input("Santafe(1) o Real madrid(2)  escoja entre '1 ó 2' "))
nombres=["Karatancheva, Lia"
         #,"Faria, Jaime"#activenme miercoles
         ,"Blanch, Dali",
          "Adkar","Nagata"
         ,"Chopra, Keshav"
         ,"Douglas, Ellie"
         ,"Kestelboim, Mariano"
         ,"Sekulic, Philip"
         ,"Dolehide, Caroline"
         #,"Kiick, Allie"#activenme mañana
         #,"Limoges CSP"#hasta el 30 de abril
        
        ]#REVISAR ADKAR Y NAGATA
nombres_formateados = []
for string in nombres:
    string_modificado = string.replace(" ", "%20")
    nombres_formateados.append(string_modificado)
print(nombres_formateados)

def timer(timer_runs):
    while timer_runs.is_set():
        
        
        
        i=0
        print("")
        for nombre in nombres_formateados:
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
                MessageBox.showinfo("Alerta",  (str(i)+" "+nombres[i]+" Si esta"))
                
            i+=1
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