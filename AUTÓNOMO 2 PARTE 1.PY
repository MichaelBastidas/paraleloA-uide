import secrets 
import string

"""import secrets → permite generar números y elecciones aleatorias seguras 
(criptográficamente fuertes).

import string → da acceso a conjuntos de caracteres como letras, dígitos y símbolos."""

def generate_password(length=16):
    """
    Genera una contraseña segura.

    :param length: longitud de la contraseña (mínimo 8 recomendado)
    :return: contraseña generada (str)
    """

    if length < 8:
        raise ValueError("La longitud mínima recomendada es 8 caracteres.")

    # Conjuntos de caracteres
    lowercase = string.ascii_lowercase      # abc...
    uppercase = string.ascii_uppercase      # ABC...
    digits = string.digits                  # 0123456789
    symbols = "!@#$%^&*()-_=+[]{};:,.?/|"

    # Aseguramos al menos uno de cada tipo
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]