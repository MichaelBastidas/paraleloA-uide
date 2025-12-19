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

    # Rellenamos el resto de la contraseña con una mezcla de todo
    all_chars = lowercase + uppercase + digits + symbols #concatenamos varios conjuntos de caracteres en una sola cadena de texto.
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_chars))

    # Mezclamos el orden para que no siempre empiece en el mismo patrón
    secrets.SystemRandom().shuffle(password_chars)

    # Unimos la lista en un string
    return "".join(password_chars)


if __name__ == "__main__":
    try:
        user_input = input("Longitud de la contraseña (por seguridad, debe ser mayor a 8 caracteres; ENTER para 16): ").strip()
        if user_input == "":
            length = 16
        else:
            length = int(user_input)

        pwd = generate_password(length)
        print("\nTu contraseña segura es:\n", pwd)
    except ValueError as e:
        print("Error:", e)