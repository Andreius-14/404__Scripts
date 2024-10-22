import os
import shutil

# Obtener la ruta de la carpeta actual
ruta_actual = os.getcwd()

# Lista de extensiones de archivo de imágenes (puedes agregar más según tus necesidades)
extensiones_imagenes = ['.jpg', '.jpeg', '.png', '.gif']

# Recorrer todas las carpetas y subcarpetas
for directorio_raiz, directorios, archivos in os.walk(ruta_actual):
    for archivo in archivos:
        # Verificar si el archivo tiene una extensión de imagen
        if any(archivo.lower().endswith(ext) for ext in extensiones_imagenes):
            # Ruta completa del archivo encontrado
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            # Mover el archivo a la carpeta actual
            shutil.move(ruta_archivo, os.path.join(ruta_actual, archivo))

print("Imágenes movidas exitosamente a la carpeta actual.")

