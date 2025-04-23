5. **README del Proyecto:**  
   Incluye un archivo `README.md` con la siguiente estructura:

   - **Introducción:** Breve descripción del reto y su propósito.
   - **Instrucciones de Ejecución:** Cómo instalar dependencias y ejecutar la aplicación.
   - **Enfoque y Solución:** Lógica implementada y decisiones de diseño.
   - **Estructura del Proyecto:** Archivos y carpetas principales.

6. **Documentación y Calidad del Código:**
   - Código bien documentado y fácil de leer.
   - Comentarios explicando pasos clave y lógica del programa.

-------------------------
# Procesamiento de Transacciones Bancarias (CLI)

## 💡 Introducción
Este proyecto es una aplicación CLI en Python para procesar un archivo CSV con transacciones bancarias y generar un reporte con balance final, transacción de mayor monto y conteo total de transacciones por tipo.

## 🚀 Instrucciones de Ejecución
1. Clona el repositorio desde la base: https://github.com/codeableorg/interbank-academy-25
Ejemplo desde Anaconda Tool:
cd ruta/donde/quieres/guardar/el/proyecto
git clone https://github.com/codeableorg/interbank-academy-25.git
cd interbank-academy-25

2. Activa el entorno virtual.
conda create -n transacciones-env python=3.10 -y
conda activate transacciones-env
* Si hay dependencias puedes instalarlas
pip install pandas

3. Ejecuta `main.py` con un archivo `ejercicioTransacciones.csv` en el mismo directorio.

## 🧠 Enfoque y Solución
Se utiliza `pandas` para leer el CSV y realizar cálculos según el tipo de transacción. 

## 📁 Estructura del Proyecto
- `transacciones.py`: Código principal
- `ejercicioTransacciones.csv`: Archivo de entrada de ejemplo
- `README.md`: Esta documentación

## 🧼 Calidad del Código
El código está comentado y estructurado para facilitar su lectura.