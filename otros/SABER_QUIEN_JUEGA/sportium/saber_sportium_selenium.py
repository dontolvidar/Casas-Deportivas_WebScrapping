import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

    
# Configurar las opciones para Chrome
# Configurar las opciones para Chrome
class Saber_de_sportium():
    def saber_de_sportium(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-minimize")
        options.add_experimental_option('useAutomationExtension', True)

        # Inicializar el webdriver y abrir la página web
        driver = webdriver.Chrome(options=options)
        driver.get("https://sports.sportium.com.co/sports/tennis/matches/today")

        # 

        time.sleep(20)
        
        try:
            # Abrir cajas cerradas
            cajascerradas = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "ta-collapsed"))
            )
            
            for lista in cajascerradas:
                lista.click()
                time.sleep(2)
        except:
            print("Error de cajas")
            
        time.sleep(14)
        # Obtener todas las listas desplegables con la clase "ta-accordion"
        lista_de_regiones = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "EventListGroup"))
        )

        time.sleep(14)
        # Iterar sobre las listas desplegables y hacer clic solo en las que están cerradas
        def encontrar_partidos():
            partidos_finales=[]
            for lista_de_partidos in lista_de_regiones:
                
                cadena=lista_de_partidos.text
                delimitadores = "\nHoy, |\nMañana, " # esto es una presión regular que significa "o"
                desorden = re.split(delimitadores, cadena) # esto devuelveex una lista con las partes 
                
                if (len(desorden)>1):
                    del desorden[0]
                    for info_partido in desorden:
                        info_partido_ordenado=info_partido.split('\n')
                        equipo1=info_partido_ordenado[1]
                        equipo2=info_partido_ordenado[2]
                        cuota1=info_partido_ordenado[3]
                        cuota2=info_partido_ordenado[4]
                        hora=info_partido_ordenado[0]
                        partidos_finales.append({'equipo1':equipo1,'equipo2':equipo2,'cuota1':cuota1,'cuota2':cuota2,'hora':hora})
            return partidos_finales

    



        lista=encontrar_partidos()
        
        # En este ejemplo, esperamos a que un elemento específico aparezca en la página
        #elementos_esperados = WebDriverWait(driver, 10).until(
        #    EC.presence_of_all_elements_located((By.CLASS_NAME, "ta-participantName"))
        #)

        # Iterar sobre la lista de elementos y mostrar el texto de cada uno
        #for elemento in elementos_esperados:
        #    print(elemento.text)
        driver.quit()
        return lista