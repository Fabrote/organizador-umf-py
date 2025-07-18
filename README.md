# 🧠 Clasificador de Informes Médicos por DNI
---

Este proyecto automatiza el proceso de clasificación de informes médicos en formato PDF, extrayendo el DNI desde el contenido del archivo y moviéndolo automáticamente a la carpeta correspondiente del paciente.


## 🚀 Objetivo
---
Evitar errores humanos y ahorrar tiempo en la gestión de documentos médicos. El script toma los informes que llegan a una carpeta común, detecta el DNI desde el texto del PDF y lo mueve a la carpeta del paciente cuyo nombre termina en ese DNI.


## 🗂 Estructura esperada
---

- Los informes llegan a una carpeta general, definida en `ruta_informes`

Cada carpeta debe terminar con el número de DNI del paciente (7 u 8 dígitos).



## ⚙️ Requisitos
---
- Python 3.8+
- Librerías:

pip install pdfplumber

El texto del PDF debe contener el número de DNI como secuencia de 7 u 8 dígitos, aunque puede estar precedido por letras o símbolos (por ejemplo: D12345678, Nº12345678, etc.).

▶️ Cómo usarlo:
---
Colocá los informes PDF en la carpeta INFORMES.


Ejecutá el script:

"python mover_informes.py"


El script buscará el DNI en cada PDF y lo moverá a la carpeta del paciente correspondiente dentro de IMAGENES.


🛡 Manejo de errores:
---
Si no se encuentra un DNI en el PDF, se muestra un mensaje de error.

Si hay más de una carpeta que termina con el mismo DNI, se ignora y se notifica para que intervengas manualmente.

Si no hay ninguna carpeta coincidente, también se muestra un aviso.


📌 Posibles mejoras:
---
Interfaz gráfica para uso por personal no técnico.

Detección otros identificadores.


👨‍⚕️ Caso de uso real:
---
Diseñado para entornos médicos donde los informes deben archivarse automáticamente en carpetas de pacientes según su DNI, optimizando procesos administrativos y minimizando errores manuales.

🧠 Autor:
---
Fabrizio

Proyecto interno de automatización para flujos de trabajo.
