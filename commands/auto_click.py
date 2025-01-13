import threading
import time
import pyautogui
from pynput import keyboard

clicking = False
running = True

def click_mouse():
    global clicking, running
    while running:
        if clicking:
            pyautogui.click()
            time.sleep(0.01)
        else:
            time.sleep(0.1)

def on_press(key):
    """Manejador de eventos para las teclas."""
    global clicking, running
    try:
        if key.char == 'q':
            print("Saliendo del programa...")
            running = False
            return False
        elif key.char == 'w':
            clicking = not clicking
            if clicking:
                print("Autoclicker iniciado.")
            else:
                print("Autoclicker detenido.")
    except AttributeError:
        pass

def run():
    """Función principal para iniciar el autoclicker."""
    print("Presiona 'w' para iniciar/detener el autoclicker. Presiona 'q' para salir.")

    threading.Thread(target=click_mouse, daemon=True).start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
