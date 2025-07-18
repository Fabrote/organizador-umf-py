import os
import pdfplumber
import shutil
import re

# Rutas personalizadas
ruta_informes = r"ruta\a\informes"  
ruta_pacientes = r"ruta\a\pacientes"  

def extraer_dni_desde_pdf(ruta_pdf):
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            texto = pdf.pages[0].extract_text()
            for palabra in texto.split():
                numeros = re.findall(r'\d{7,8}', palabra)
                if numeros:
                    return numeros[0]  # Devuelve el primer DNI que encuentra     
    except Exception as e:
        print(f"Error al leer {ruta_pdf}: {e}")
    return None

def mover_informes():
    for archivo in os.listdir(ruta_informes):
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(ruta_informes, archivo)
            dni = extraer_dni_desde_pdf(ruta_pdf)
            if dni:
                # Buscar carpeta en red que termine en el DNI
                carpetas = [c for c in os.listdir(ruta_pacientes) if c.endswith(dni)]
                if len(carpetas) == 1:
                    carpeta_destino = os.path.join(ruta_pacientes, carpetas[0])
                    destino = os.path.join(carpeta_destino, archivo)
                    try:
                        shutil.move(ruta_pdf, destino)
                        print(f"✅ Movido: {archivo} → {carpeta_destino}")
                    except Exception as e:
                        print(f"❌ Error al mover {archivo}: {e}")
                elif len(carpetas) == 0:
                    print(f"❌ No se encontró carpeta para DNI {dni}")
                else:
                    print(f"⚠️ Múltiples carpetas para DNI {dni}: {carpetas}")
            else:
                print(f"❌ No se pudo extraer DNI de: {archivo}")

if __name__ == "__main__":
    mover_informes()
