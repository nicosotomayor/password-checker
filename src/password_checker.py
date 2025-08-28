import re
import math
import string
import hashlib
import requests
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def calcular_complejidad(password):
    """Evalúa longitud, tipos de caracteres y entropía"""
    longitud = len(password)
    charsets = 0
    if re.search(r'[a-z]', password):  
        charsets += len(string.ascii_lowercase)
    if re.search(r'[A-Z]', password):  
        charsets += len(string.ascii_uppercase)
    if re.search(r'[0-9]', password):  
        charsets += len(string.digits)
    if re.search(r'[^a-zA-Z0-9]', password):  
        charsets += len(string.punctuation)
    
    entropia = longitud * math.log2(charsets) if charsets else 0
    return longitud, charsets, entropia

def tiempo_crack(entropia):
    """Calcula tiempo estimado de crackeo con fuerza bruta (1e9 intentos/segundo)"""
    intentos = 2 ** entropia
    segundos = intentos / 1e9
    minutos, horas = segundos / 60, segundos / 3600
    dias, años = horas / 24, horas / 8760
    
    if años > 1000:
        return "🔐 Más de 1000 años (irrompible en la práctica)"
    elif años >= 1:
        return f"⏳ ~{años:.2f} años"
    elif dias >= 1:
        return f"⏳ ~{dias:.2f} días"
    elif horas >= 1:
        return f"⚠️ ~{horas:.2f} horas"
    elif minutos >= 1:
        return f"⚠️ ~{minutos:.2f} minutos"
    else:
        return "❌ Menos de 1 minuto (muy débil)"

def check_pwned(password):
    """Verifica si la contraseña está en filtraciones (HaveIBeenPwned API)"""
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    if res.status_code != 200:
        return f"⚠️ Error al consultar la API ({res.status_code})"
    
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"⚠️ Esta contraseña apareció en {count} filtraciones. ¡No la uses!"
    return "✅ No aparece en filtraciones conocidas."

def evaluar_password(password):
    longitud, charsets, entropia = calcular_complejidad(password)
    print(Fore.CYAN + f"\n🔍 Evaluando contraseña: {password}")
    print(Fore.YELLOW + f"- Longitud: {longitud}")
    print(Fore.YELLOW + f"- Tipos de caracteres usados: {charsets}")
    print(Fore.YELLOW + f"- Entropía: {entropia:.2f} bits")
    print(Fore.GREEN + f"- Tiempo estimado crackeo: {tiempo_crack(entropia)}")
    print(Fore.RED + f"- Estado filtraciones: {check_pwned(password)}")

if __name__ == "__main__":
    password = input("Introduce una contraseña a evaluar: ")
    evaluar_password(password)
