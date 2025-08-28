
<div align="center">

# 🔐 Password Strength & Breach Checker

Herramienta en **Python** para evaluar la seguridad de contraseñas: calcula **complejidad y entropía**, estima **tiempo de crackeo** y verifica si la contraseña **aparece en filtraciones reales** (Have I Been Pwned).

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](#)

</div>

---

## ✨ Características
- ✅ **Análisis de complejidad** (minúsculas, mayúsculas, números y símbolos)
- ✅ **Entropía** aproximada (bits)
- ✅ **Estimación de tiempo** de crackeo a 1e9 intentos/seg
- ✅ **Chequeo de filtraciones** con k-anonymity en HIBP
- ✅ **Salida clara en consola**

---

## 🚀 Instalación, dependencias y uso

**1) Clonar el repositorio**
```bash
git clone https://github.com/nicosotomayor/password-checker.git
cd password-checker
2) Instalar dependencias

pip install -r requirements.txt


3) Ejecutar

python src/password_checker.py


4) Probar

Introduce una contraseña a evaluar: M1l@Clave!2025#

