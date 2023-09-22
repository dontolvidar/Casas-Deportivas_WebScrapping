import sqlite3
from sqlite3 import Error
class Conexion():
      def conexionBD(self):
            try:
                  con = sqlite3.connect('apuestas.db')
                  return con
            except sqlite3.Error as e:
                  print("Error en la clase conexion en conextar")
                  print(e)
                  return None

      
      def insertar(self,con,tabla,registros):
            try:
                  cursorOBJ= con.cursor()
                  consulta = f"INSERT INTO {tabla} VALUES ({', '.join(['?'] * len(registros))})"
                  cursorOBJ.execute(consulta, registros)
                  con.commit()
            except sqlite3.Error as e:
                  print(f"Error en la clase conexion en insertar en {tabla}") if tabla=='apuesta_tiempo' else print(f"Error normalito en {tabla}")
                  #print(e)
#EJEMPLO DE USO
#con = Conexion().conexionBD()
#Conexion().insertar(con,"apuesta_tiempo",None,"1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1")
#Conexion().insertar(con,"apuesta",2,"1",2,1)
#Conexion().insertar(con,"categoria","TENNIS")