import threading
import time
from pynput import keyboard
from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent,
    CGEventPost,
    kCGEventLeftMouseDown,
    kCGEventLeftMouseUp,
    kCGHIDEventTap,
    CGEventCreate,
    CGEventGetLocation,
)

# Variables globales
clicking = False
running = True
click_count = 0  # Contador de clics


def get_mouse_position():
    """Obtiene la posición actual del mouse."""
    location = CGEventGetLocation(CGEventCreate(None))
    return location.x, location.y


def mouse_click(x, y):
    """Realiza un clic izquierdo en una posición específica."""
    event_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), 0)
    event_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), 0)
    CGEventPost(kCGHIDEventTap, event_down)
    CGEventPost(kCGHIDEventTap, event_up)


def click_mouse():
    """Función que realiza los clics cuando clicking está activo."""
    global clicking, running, click_count
    next_click_time = time.perf_counter()
    while running:
        if clicking:
            current_time = time.perf_counter()
            if current_time >= next_click_time:
                x, y = get_mouse_position()  # Obtener posición actual del mouse
                mouse_click(x, y)
                click_count += 1
                next_click_time = current_time + 0.01  # Ajuste para 100 clics/segundo
        else:
            time.sleep(0.1)


def print_clicks():
    """Función que imprime el número de clics realizados cada segundo."""
    global running, click_count
    while running:
        time.sleep(1)  # Espera 1 segundo
        print(f"Clics realizados en el último segundo: {click_count}")
        click_count = 0  # Reinicia el contador


def on_press(key):
    """Manejador de eventos para las teclas."""
    global clicking, running
    try:
        if key.char == "q":
            print("Saliendo del programa...")
            running = False
            return False
        elif key.char == "w":
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

    # Iniciar los hilos para los clics y el contador
    threading.Thread(target=click_mouse, daemon=True).start()
    threading.Thread(target=print_clicks, daemon=True).start()

    # Listener del teclado
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
