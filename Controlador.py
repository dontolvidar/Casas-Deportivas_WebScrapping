import datetime
import requests
import threading
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from MODELO.conexion import Conexion
from MODELO.categoria import Categoria
from MODELO.apuesta import Apuesta
from MODELO.apuesta_tiempo import ApuestaTiempo
#SCRAPPING:

url = "https://na-offering-api.kambicdn.net/offering/v2018/rsico/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1694971544456"

headers = {
    "charset": "UTF-8",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
	"Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "http://www.rushbet.co",
}


def timer(timer_runs):
    while timer_runs.is_set():
        try:
            response = requests.get(url, headers=headers)
            lista_de_eventos=response.json().get('liveEvents')
    
            i=0
            for evento in lista_de_eventos:
                
                
                if (evento['event']['sport']=="TENNIS" or evento['event']['sport']=="BASKETBALL") and 'mainBetOffer' in evento:
                    event=evento['event']
                    mainbetofer=evento['mainBetOffer']
                    livedata=evento['liveData']
                    
                        
                    
                    #categoria
                    try:
                        
                        categoria=Categoria(event['sport'])
                    
                            
                    except KeyError:
                        categoria.set_nombre_categoria(event['sport'])
                        print ("error categoria")
                    
                    #apuesta
                    try:
                        idapuesta=livedata['eventId']
                        equipo1=mainbetofer['outcomes'][0]['label']
                        equipo2=mainbetofer['outcomes'][1]['label']
                        categoria_nombre_categoria=event['sport']
                        tiempo=datetime.datetime.now()
                        apuesta=[]
                        
                        apuesta=Apuesta(idapuesta,equipo1,equipo2,categoria_nombre_categoria,tiempo)
                        
                            
                    except KeyError:
                        apuesta.set_idapuesta(livedata['eventId'])
                        apuesta.set_equipo1(mainbetofer['outcomes'][0]['label'])
                        apuesta.set_equipo2(mainbetofer['outcomes'][1]['label'])
                        apuesta.set_categoria_nombre_categoria(event['sport'])
                        apuesta.set_tiempo(datetime.datetime.now())
                        print ("error apuesta")
                    
                    
                    #apuesta tiempo 
                    try:
                        
                        idapuesta=None
                        periodo=livedata['matchClock']['period'] if 'period' in livedata['matchClock'] else ""
                        tiempo_minutos=livedata['matchClock']['minute'] if 'minute' in livedata['matchClock'] else -1
                        tiempo_segundos=livedata['matchClock']['second'] if 'second' in livedata['matchClock'] else -1
                        cuota1=mainbetofer['outcomes'][0]['odds']/1000 if 'odds' in mainbetofer['outcomes'][0] else -1
                        cuota2=mainbetofer['outcomes'][1]['odds']/1000 if 'odds' in mainbetofer['outcomes'][1] else -1
                        
                        score_global_live1=livedata['score']['home'] if 'home' in livedata['score'] else -1
                        score_global_live2=livedata['score']['away'] if 'away' in livedata['score'] else -1    
                        
                        score1_set1=-1
                        score2_set1=-1
                        score1_set2=-1
                        score2_set2=-1
                        score1_set3=-1
                        score2_set3=-1
                        score1_set4=-1
                        score2_set4=-1
                        score1_set5=-1
                        score2_set5=-1
                        quien_sirve_tenis=""
                        if categoria.get_nombre_categoria()=="TENNIS":
                            if (len(livedata['statistics']['sets']['home'])<=3):
                                score1_set1=livedata['statistics']['sets']['away'][0]
                                score2_set1=livedata['statistics']['sets']['home'][0]
                                score1_set2=livedata['statistics']['sets']['home'][1]
                                score2_set2=livedata['statistics']['sets']['away'][1]
                                score1_set3=livedata['statistics']['sets']['home'][2]
                                score2_set3=livedata['statistics']['sets']['away'][2]
                                
                            elif(len(livedata['statistics']['sets']['home'])>3):
                                score1_set4=livedata['statistics']['sets']['away'][3]
                                score2_set4=livedata['statistics']['sets']['home'][3]
                                score1_set5=livedata['statistics']['sets']['away'][4]
                                score2_set5=livedata['statistics']['sets']['home'][4]
                            quien_sirve_tenis="equipo1" if livedata['statistics']['sets']['homeServe'] else "equipo2"
                        apuesta_idapuesta=livedata['eventId']
                        try:
                            apuestatiempo=ApuestaTiempo(idapuesta, periodo, tiempo_minutos, tiempo_segundos, cuota1, cuota2, score_global_live1, score_global_live2,
                            score1_set1, score2_set1, score1_set2, score2_set2, score1_set3, score2_set3, score1_set4, score2_set4, score1_set5, score2_set5,
                            quien_sirve_tenis, apuesta_idapuesta)
                        except:
                            apuesta.set_idapuesta_tiempo(idapuesta)
                            apuesta.set_periodo(periodo)
                            apuesta.set_tiempo_minutos(tiempo_minutos)
                            apuesta.set_tiempo_minutos(tiempo_segundos)
                            apuesta.set_cuota1(cuota1)
                            apuesta.set_cuota2(cuota2)
                            apuesta.set_score_global_live1(score_global_live1)
                            apuesta.set_score_global_live2(score_global_live2)
                            apuesta.set_score1_set1(score1_set1)
                            apuesta.set_score2_set1(score2_set1)
                            apuesta.set_score1_set2(score1_set2)
                            apuesta.set_score2_set2(score2_set2)
                            apuesta.set_score1_set3(score1_set3)
                            apuesta.set_score2_set3(score2_set3)
                            apuesta.set_score1_set4(score1_set4)
                            apuesta.set_score2_set4(score2_set4)
                            apuesta.set_score1_set5(score1_set5)
                            apuesta.set_score2_set5(score2_set5)
                            apuesta.set_quien_sirve_tenis(quien_sirve_tenis)
                            apuesta.set_apuesta_idapuesta(apuesta_idapuesta)
                            print("ERROR GARRAFAL")
                            
                    except:
                        MessageBox.showwarning("Alerta", "Hay algun error mirar recorrido.")
                    
                    
                    
                    
                    
                    #Pasar a base de datos
                    con = Conexion().conexionBD()
                    Conexion().insertar(con,"categoria",categoria.tolist())
                    Conexion().insertar(con,"apuesta",apuesta.tolist())
                    Conexion().insertar(con,"apuesta_tiempo",apuestatiempo.tolist())
                    i=i+1
                    print("TODO BIEN ",i)
        except:
            print("ERROR EN REQUEST")
        time.sleep(20)   
try:         
    timer_runs = threading.Event()
    timer_runs.set()
    t = threading.Thread(target=timer, args=(timer_runs,))
    t.start()
    # Esperar 10 segundos y luego detener el timer.
    #time.sleep(120)
    #timer_runs.clear()
    print("¡El timer ha sido detenido!")
except:
    MessageBox.showinfo("Alerta","El programa controlador ha sido cerrado")