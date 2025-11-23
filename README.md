
Traductor LSC a Voz y Texto (Prototipo TRL5)

Este repositorio contiene un prototipo funcional de un traductor de Lengua de Señas Colombiana (LSC) a texto y voz en tiempo real.
Fue desarrollado como parte de la Fase 4 del proyecto ingenieril en la UNAD.

Nivel de madurez tecnológica (TRL): TRL 5 – Prototipo validado en entorno relevante.

Traductor LSC a Voz y Texto (Prototipo TRL5)
Este repositorio contiene un prototipo funcional de un traductor de Lengua de Señas Colombiana (LSC) a texto y voz en tiempo real.
Fue desarrollado como parte de la Fase 4 del proyecto ingenieril en la UNAD.
Nivel de madurez tecnológica (TRL): TRL 5 – Prototipo validado en entorno relevante.

Descripción del funcionamiento
El sistema utiliza la cámara para detectar la mano del usuario, identifica la seña correspondiente a la mano abierta (cuatro dedos extendidos), muestra el texto "HOLA" en pantalla y reproduce en voz la palabra "Hola".
El prototipo es demostrativo y académico, no representa una aplicación final ni un sistema de reconocimiento completo de señas.

Instalación y ejecución
1. Clonar el repositorio
   
git clone https://github.com/kymba95/traductor_lsc.git

2, Navegar a la carpeta

cd traductor_lsc

3. Crear un entorno virtual
   
Windows

python -m venv venv
.\venv\Scripts\activate

macOS o Linux

python3 -m venv venv
source venv/bin/activate

4. Instalar dependencias
   
pip install -r requirements.txt

5. Ejecutar el prototipo
   
python prototipo_lsc.py

Modo de uso

Coloque la mano frente a la cámara con cuatro dedos extendidos (no es obligatorio incluir el pulgar).
Si la seña es reconocida, en pantalla aparecerá el texto "HOLA" y se reproducirá la palabra "Hola" mediante síntesis de voz.
Presione la tecla Q para cerrar el programa.
