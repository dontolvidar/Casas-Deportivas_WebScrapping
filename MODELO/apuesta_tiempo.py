class ApuestaTiempo():
    def __init__(self, idapuesta_tiempo, periodo, tiempo_minutos, tiempo_segundos, cuota1, cuota2, score_global_live1, score_global_live2,
                 score1_set1, score2_set1, score1_set2, score2_set2, score1_set3, score2_set3, score1_set4, score2_set4, score1_set5, score2_set5,
                 quien_sirve_tenis, apuesta_idapuesta):
        self.idapuesta_tiempo = idapuesta_tiempo
        self.periodo = periodo
        self.tiempo_minutos = tiempo_minutos
        self.tiempo_segundos = tiempo_segundos
        self.cuota1 = cuota1
        self.cuota2 = cuota2
        self.score_global_live1 = score_global_live1
        self.score_global_live2 = score_global_live2
        self.score1_set1 = score1_set1
        self.score2_set1 = score2_set1
        self.score1_set2 = score1_set2
        self.score2_set2 = score2_set2
        self.score1_set3 = score1_set3
        self.score2_set3 = score2_set3
        self.score1_set4 = score1_set4
        self.score2_set4 = score2_set4
        self.score1_set5 = score1_set5
        self.score2_set5 = score2_set5
        self.quien_sirve_tenis = quien_sirve_tenis
        self.apuesta_idapuesta = apuesta_idapuesta
    # Getters
    def get_idapuesta_tiempo(self):
        return self._idapuesta_tiempo

    def get_periodo(self):
        return self._periodo

    def get_tiempo_minutos(self):
        return self._tiempo_minutos

    def get_tiempo_segundos(self):
        return self._tiempo_segundos

    def get_cuota1(self):
        return self._cuota1

    def get_cuota2(self):
        return self._cuota2

    def get_score_global_live1(self):
        return self._score_global_live1

    def get_score_global_live2(self):
        return self._score_global_live2

    def get_score1_set1(self):
        return self._score1_set1

    def get_score2_set1(self):
        return self._score2_set1

    def get_score1_set2(self):
        return self._score1_set2

    def get_score2_set2(self):
        return self._score2_set2

    def get_score1_set3(self):
        return self._score1_set3

    def get_score2_set3(self):
        return self._score2_set3

    def get_score1_set4(self):
        return self._score1_set4

    def get_score2_set4(self):
        return self._score2_set4

    def get_score1_set5(self):
        return self._score1_set5

    def get_score2_set5(self):
        return self._score2_set5

    def get_quien_sirve_tenis(self):
        return self._quien_sirve_tenis

    def get_apuesta_idapuesta(self):
        return self._apuesta_idapuesta

    # Setters
    def set_idapuesta_tiempo(self, idapuesta_tiempo):
        self._idapuesta_tiempo = idapuesta_tiempo

    def set_periodo(self, periodo):
        self._periodo = periodo

    def set_tiempo_minutos(self, tiempo_minutos):
        self._tiempo_minutos = tiempo_minutos

    def set_tiempo_segundos(self, tiempo_segundos):
        self._tiempo_segundos = tiempo_segundos

    def set_cuota1(self, cuota1):
        self._cuota1 = cuota1

    def set_cuota2(self, cuota2):
        self._cuota2 = cuota2

    def set_score_global_live1(self, score_global_live1):
        self._score_global_live1 = score_global_live1

    def set_score_global_live2(self, score_global_live2):
        self._score_global_live2 = score_global_live2

    def set_score1_set1(self, score1_set1):
        self._score1_set1 = score1_set1

    def set_score2_set1(self, score2_set1):
        self._score2_set1 = score2_set1

    def set_score1_set2(self, score1_set2):
        self._score1_set2 = score1_set2

    def set_score2_set2(self, score2_set2):
        self._score2_set2 = score2_set2

    def set_score1_set3(self, score1_set3):
        self._score1_set3 = score1_set3

    def set_score2_set3(self, score2_set3):
        self._score2_set3 = score2_set3

    def set_score1_set4(self, score1_set4):
        self._score1_set4 = score1_set4

    def set_score2_set4(self, score2_set4):
        self._score2_set4 = score2_set4

    def set_score1_set5(self, score1_set5):
        self._score1_set5 = score1_set5

    def set_score2_set5(self, score2_set5):
        self._score2_set5 = score2_set5

    def set_quien_sirve_tenis(self, quien_sirve_tenis):
        self._quien_sirve_tenis = quien_sirve_tenis

    def set_apuesta_idapuesta(self, apuesta_idapuesta):
        self._apuesta_idapuesta = apuesta_idapuesta
        
    
    def tolist(self):
        return [
            self.idapuesta_tiempo,
            self.periodo,
            self.tiempo_minutos,
            self.tiempo_segundos,
            self.cuota1,
            self.cuota2,
            self.score_global_live1,
            self.score_global_live2,
            self.score1_set1,
            self.score2_set1,
            self.score1_set2,
            self.score2_set2,
            self.score1_set3,
            self.score2_set3,
            self.score1_set4,
            self.score2_set4,
            self.score1_set5,
            self.score2_set5,
            self.quien_sirve_tenis,
            self.apuesta_idapuesta
        ]
        
# Ejemplo de uso
"""apuesta = ApuestaTiempo(idapuesta_tiempo=1, periodo="Trimestral", tiempo_minutos=30.5, tiempo_segundos=15.2, cuota1=2.0, cuota2=3.0,
                        score_global_live1=3, score_global_live2=2, score1_set1=6, score2_set1=4, score1_set2=7, score2_set2=5,
                        score1_set3=None, score2_set3=None, score1_set4=None, score2_set4=None, score1_set5=None, score2_set5=None,
                        quien_sirve_tenis="Jugador A", apuesta_idapuesta=1001)"""