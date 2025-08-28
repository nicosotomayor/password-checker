# 🔐 Password Strength & Breach Checker
Herramienta en **Python** para evaluar la seguridad de contraseñas.  
Esta aplicación combina tres funciones principales:  
1. **Análisis de complejidad** → Evalúa longitud, uso de mayúsculas, minúsculas, números y símbolos.  
2. **Estimación de tiempo de crackeo** → Calcula cuánto tardaría en ser descubierta con fuerza bruta.  
3. **Verificación en filtraciones reales** → Consulta la API de [Have I Been Pwned](https://haveibeenpwned.com) para comprobar si ya fue expuesta en leaks.
4. 
## 🚀 Instalación
Clonar el repositorio y entrar en la carpeta:
```bash
git clone https://github.com/nicosotomayor/password-checker.git
cd password-checker

Instalar dependencias:

pip install -r requirements.txt

▶️ Uso

Ejecutar el script:

python src/password_checker.py


El programa pedirá que introduzcas una contraseña a evaluar:

Introduce una contraseña a evaluar: M1l@Clave!2025#


Ejemplo de salida:

🔍 Evaluando contraseña: M1l@Clave!2025#
- Longitud: 14
- Tipos de caracteres usados: 94
- Entropía: 91.86 bits
- Tiempo estimado crackeo: 🔐 Más de 1000 años (irrompible en la práctica)
- Estado filtraciones: ✅ No aparece en filtraciones conocidas.

📊 Resultados posibles

Muy débil → menos de 1 minuto en crackearse.

Débil → horas o días.

Aceptable → meses o algunos años.

Fuerte → siglos o miles de años.

Irrompible en la práctica → más de 1000 años.

⚠️ Filtrada → aparece en bases de datos de contraseñas robadas → no debe usarse nunca.
