

# 🔐 Password Strength & Breach Checker

Herramienta en **Python** para evaluar la seguridad de contraseñas.  

Esta aplicación combina tres funciones principales:  
1. **Análisis de complejidad** → Evalúa longitud, uso de mayúsculas, minúsculas, números y símbolos.  
2. **Estimación de tiempo de crackeo** → Calcula cuánto tardaría en ser descubierta con fuerza bruta.  
3. **Verificación en filtraciones reales** → Consulta la API de [Have I Been Pwned](https://haveibeenpwned.com) para comprobar si ya fue expuesta en leaks.  

---

## 🚀 Instalación, dependencias y uso

**1) Clonar el repositorio**  
ABRIR```bash
git clone https://github.com/nicosotomayor/password-checker.git
cd password-checker
CERRAR```

**2) Instalar dependencias**  
ABRIR```bash
pip install -r requirements.txt
CERRAR```

**3) Ejecutar**  
ABRIR```bash
python src/password_checker.py
CERRAR```

**4) Probar**  
ABRIR```bash
Introduce una contraseña a evaluar: M1l@Clave!2025#
CERRAR```

---

## 📋 Ejemplo de salida
ABRIR```bash
🔍 Evaluando contraseña: M1l@Clave!2025#
- Longitud: 14
- Tipos de caracteres usados: 94
- Entropía: 91.86 bits
- Tiempo estimado crackeo: 🔐 Más de 1000 años (irrompible en la práctica)
- Estado filtraciones: ✅ No aparece en filtraciones conocidas.
CERRAR```

---

## 📊 Resultados posibles
- **Muy débil** → menos de 1 minuto en crackearse.  
- **Débil** → horas o días.  
- **Aceptable** → meses o algunos años.  
- **Fuerte** → siglos o miles de años.  
- **Irrompible en la práctica** → más de 1000 años.  
- **⚠️ Filtrada** → aparece en bases de datos de contraseñas robadas → *no debe usarse nunca*.  

---

## 📜 Licencia
MIT License © 2025 [nicosotomayor](https://github.com/nicosotomayor)


