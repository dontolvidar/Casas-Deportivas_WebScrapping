import smtplib
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText
#!pip install smtplib
class Correo():
    
    
    def enviar_correo(self, texto):
        # Crea la conexión SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        correo = 'jadiazf@unal.edu.co'
        pas ='Fonseca4455'
        # Inicia sesión en tu cuenta de Gmail
        server.starttls()
        server.login(correo, pas)
        
        # Definir el remitente y destinatario del correo electrónico
        remitente = "jadiazf@unal.edu.co"
        destinatario = "jadiazf@unal.edu.co"
        # Crear el mensaje del correo electrónico
        mensaje = email.mime.multipart.MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = "Correo electrónico con archivo adjunto"

        # Añadir el cuerpo del mensaje
        cuerpo = "Hola, tienes que apostar por: \n\n"+texto+"\n\nSaludos,\n Apuestas,\n"
        mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

        # Añadir el archivo Excel como adjunto
        """ruta_archivo = '/content/Owner_2022123084834.csv'
        archivo = open(ruta_archivo, 'rb')
        adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
        adjunto.set_payload((archivo).read())
        email.encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
        mensaje.attach(adjunto)
        """
        # Convertir el mensaje a texto plano
        texto = mensaje.as_string()

        # Enviar el correo electrónico
        server.sendmail(remitente, destinatario, texto)

        # Cerrar la conexión SMTP
        server.quit()