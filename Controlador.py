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
                
                
                if (evento['event']['sport']=="BASKETBALL") and 'mainBetOffer' in evento:
                    event=evento['event']
                    mainbetofer=evento['mainBetOffer']
                    livedata=evento['liveData']
                    
                        
                    
                    #categoria
                    try:
                        
                        categoria=Categoria(event['sport'])
                    
                            
                    except KeyError:
                        categoria.set_nombre_categoria(event['sport'])
                        print ("error categoria")
                    
                    #partido
                    try:
                        idapuesta=livedata['eventId']
                        equipo1=evento['homeName']
                        equipo2=evento['awayName']
                        categoria_nombre_categoria=event['sport']
                        tiempo_registro=datetime.datetime.now()
                        nombre_partido_completo = evento['name']
                        fecha_inicio_partido = evento['start']
                        nombre_torneo = evento['group']
                        en_curso= evento['state']
                        apuesta=[]
                        apuesta = Apuesta(idapuesta, equipo1, equipo2, categoria_nombre_categoria, tiempo_registro, nombre_partido_completo, fecha_inicio_partido, nombre_torneo, en_curso)
                        
                            
                    except KeyError:
                        print ("error apuesta")
                    
                    
                    #datos en vivo del partido
                    idapuesta_tiempo = 0
                    periodo = ""
                    tiempo_minutos = 0.0
                    tiempo_segundos = 0.0
                    cuota1 = 0.0
                    cuota2 = 0.0
                    score_global_live1 = 0
                    score_global_live2 = 0
                    apuesta_idapuesta = 0
                    tiempo_minutos_faltante = -1 # O datetime.datetime.now() si prefieres la fecha y hora actual
                    tiempo_segundos_faltante = -1 # O datetime.datetime.now()
                    puntajecuarto_actual_equipo_1 = ""
                    puntajecuarto_actual_equipo_2 = ""
                    ultima_accion = ""
                    nonLiveBoCount = ""
                    liveBoCount = ""
                    criterion1 = ""
                    criterion2 = ""
                    cuota1_american = ""
                    cuota2_american = ""
                    nombre_equipo_1 = ""
                    nombre_equipo_2 = ""
                    apuesta_abierta_equipo_1 = ""
                    apuesta_abierta_equipo_2 = ""
                    
                    
                    
                    try:
                        # verifica que este activo el equipo 1
                        if 0 in evento['mainBetOffer'] or 1 in evento['mainBetOffer']:
                            periodo=livedata['matchClock']['period'] if 'period' in livedata['matchClock'] else ""
                            tiempo_minutos=livedata['matchClock']['minute'] if 'minute' in livedata['matchClock'] else -1
                            tiempo_segundos=livedata['matchClock']['second'] if 'second' in livedata['matchClock'] else -1
                            
                            
                            score_global_live1=livedata['score']['home'] if 'home' in livedata['score'] else -1
                            score_global_live2=livedata['score']['away'] if 'away' in livedata['score'] else -1    
                            
                            tiempo_minutos_faltante = livedata['matchClock']['minutesLeftInPeriod'] 
                            tiempo_segundos_faltante = livedata['matchClock']['secondsLeftInMinute']

                            puntajecuarto_actual_equipo_1 = evento['liveData']['info'] #arreglar
                            puntajecuarto_actual_equipo_2 = evento['liveData']['info'] #arreglar
                            
                            
                            ultima_accion = evento['liveData']['who']
                            nonLiveBoCount = evento['nonLiveBoCount']
                            liveBoCount = evento['liveBoCount']
                            
                            
                        if 0 in evento['mainBetOffer']:
                            nombre_equipo_1=mainbetofer['outcomes'][0]['label']
                            cuota1=mainbetofer['outcomes'][0]['odds']/1000 if 'odds' in mainbetofer['outcomes'][0] else -1
                            criterion1 = evento['mainBetOffer']['outcomes'][0]['criterion']['label']
                            cuota1_american=evento['mainBetOffer']['outcomes'][0]['oddsAmerican']
                            apuesta_abierta_equipo_1=evento['mainBetOffer']['outcomes'][0]['status']
                        else:
                            cuota1=-1
                                
                        if 1 in evento['mainBetOffer']:
                            nombre_equipo_2=mainbetofer['outcomes'][1]['label']
                            cuota2=mainbetofer['outcomes'][1]['odds']/1000 if 'odds' in mainbetofer['outcomes'][1] else -1
                            criterion2 = evento['mainBetOffer']['outcomes'][1]['criterion']['label']
                            cuota2_american=evento['mainBetOffer']['outcomes'][1]['oddsAmerican']
                            apuesta_abierta_equipo_2=evento['mainBetOffer']['outcomes'][1]['status']
                        else:
                            cuota2=-1
                        
                        
                        # escribir el objeto
                        try:
                            apuestatiempo = ApuestaTiempo(idapuesta_tiempo, periodo, tiempo_minutos, tiempo_segundos, cuota1, cuota2,
                              score_global_live1, score_global_live2, apuesta_idapuesta,
                              tiempo_minutos_faltante, tiempo_segundos_faltante,
                              puntajecuarto_actual_equipo_1, puntajecuarto_actual_equipo_2,
                              ultima_accion, nonLiveBoCount, liveBoCount, criterion1, criterion2,
                              cuota1_american, cuota2_american, nombre_equipo_1, nombre_equipo_2,
                              apuesta_abierta_equipo_1, apuesta_abierta_equipo_2)
                        except:
                            print("no se pudo declarar el objeto de PARTIDO EN VIVO")
                        
                       
                            
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