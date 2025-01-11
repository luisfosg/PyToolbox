import os
import rarfile

def run():
    def descomprimir_rar():
        # Solicita el path donde buscar los archivos .rar
        path = input("Ingresa el path donde buscar los archivos .rar: ").strip()
        
        # Verifica si el path ingresado es válido
        if not os.path.exists(path):
            print("El path ingresado no existe. Inténtalo de nuevo.")
            return

        # Busca archivos .rar en el directorio
        rar_files = [f for f in os.listdir(path) if f.endswith('.rar')]

        if not rar_files:
            print("No se encontraron archivos .rar en el directorio proporcionado.")
            return

        # Itera sobre los archivos encontrados y los descomprime
        for rar_file in rar_files:
            rar_path = os.path.join(path, rar_file)
            output_dir = os.path.join(path, rar_file.replace('.rar', ''))
            
            try:
                # Abre el archivo .rar y extrae su contenido
                with rarfile.RarFile(rar_path) as rf:
                    print(f"Descomprimiendo '{rar_file}' en '{output_dir}'...")
                    rf.extractall(output_dir)
                    print(f"Archivo '{rar_file}' descomprimido con éxito.")
            except rarfile.Error as e:
                print(f"Error al descomprimir '{rar_file}': {e}")
    
    descomprimir_rar()
