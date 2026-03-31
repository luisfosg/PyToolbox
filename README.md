# Python Toolbox

Colección de herramientas de línea de comandos en Python.

## Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

## Instalación

```bash
pip install -r requirements.txt
```

## Uso (local)

```bash
python main.py
```

Sigue las instrucciones en pantalla para seleccionar una herramienta.

## Uso con Docker

```bash
# Build
docker build -t pytoolbox .

# Run
docker run -it --rm -v "$(pwd)/commands:/app/commands" pytoolbox
```

O usar docker-compose:

```bash
docker-compose up --build
```

## Estructura

```
├── main.py                   # Punto de entrada
├── commands/                 # Comandos disponibles
│   ├── extract_rar.py
│   ├── auto_click.py
│   └── remove_pdf_passwords.py
├── requirements.txt          # Dependencias local
├── docker-requirements.txt   # Dependencias Docker
├── Dockerfile                # Configuración Docker
├── docker-compose.yml        # Orquestación Docker
└── README.md                 # Este archivo
```

## Comandos disponibles

### 1. Remove Pdf Passwords
Elimina la contraseña de archivos PDF protegidos.
- **Input**: Ruta de carpeta con PDFs y contraseña
- **Output**: PDFs sin protección

### 2. Extract Rar
Descomprime archivos RAR en una carpeta.
- **Input**: Ruta donde buscar archivos .rar
- **Output**: Archivos extraídos en carpetas con el nombre del archivo

### 3. Auto Click (solo macOS)
Autoclicker que hace clic en la posición actual del mouse.
- **Controles**:
  - `w`: Iniciar/detener clic automático
  - `q`: Salir
- **Nota**: Solo funciona en macOS y requiere instalación local (no disponible en Docker)

## Añadir nuevos comandos

1. Crea un archivo en `commands/`
2. Define una función `run()` sin argumentos
3. El comando aparecerá automáticamente en el menú