import os
import importlib
import sys

COMMANDS_FOLDER = "commands"

def load_commands(folder):
    """Carga los módulos de Python desde la carpeta especificada."""
    commands = {}
    if not os.path.exists(folder):
        print(f"La carpeta '{folder}' no existe. Creándola...")
        os.makedirs(folder)
        return commands

    sys.path.insert(0, folder)
    
    for filename in os.listdir(folder):
        if filename.endswith(".py") and not filename.startswith("_"):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "run"):
                    commands[module_name] = module.run
                else:
                    print(f"El módulo '{module_name}' no tiene una función 'run'.")
            except Exception as e:
                print(f"Error al cargar el módulo '{module_name}': {e}")
    
    sys.path.pop(0)
    return commands

def show_menu(commands):
    """Muestra el menú con las opciones disponibles."""
    print("\n=== MENÚ ===")
    for i, command in enumerate(commands.keys(), start=1):
        print(f"{i}. {command}")
    print("0. Salir")

def main():
    commands = load_commands(COMMANDS_FOLDER)

    if not commands:
        print("No hay comandos disponibles. Añade archivos .py en la carpeta 'commands' con una función 'run'.")
        return

    while True:
        show_menu(commands)
        choice = input("Selecciona una opción: ")

        if choice == "0":
            print("Saliendo del programa...")
            break

        try:
            choice = int(choice)
            if 1 <= choice <= len(commands):
                command_name = list(commands.keys())[choice - 1]
                print(f"Ejecutando '{command_name}'...", end="\n\n")
                commands[command_name]()
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
