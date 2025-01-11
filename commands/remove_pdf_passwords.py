import os
from PyPDF2 import PdfReader, PdfWriter

def ejecutar():
    """
    Elimina la contraseña de todos los archivos PDF en la carpeta especificada.
    """
    ruta_carpeta = input("Ingresa la ruta de la carpeta: ").strip()
    contraseña = input("Ingresa la contraseña del PDF: ").strip()

    for nombre_archivo in os.listdir(ruta_carpeta):
        if nombre_archivo.endswith(".pdf"):
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            try:
                lector = PdfReader(ruta_archivo)

                if lector.is_encrypted:
                    lector.decrypt(contraseña)

                escritor = PdfWriter()
                for pagina in lector.pages:
                    escritor.add_page(pagina)

                with open(ruta_archivo, "wb") as pdf_salida:
                    escritor.write(pdf_salida)

                print(f"Contraseña eliminada de: {nombre_archivo}")
            except Exception as e:
                print(f"No se pudo procesar {nombre_archivo}: {e}")
