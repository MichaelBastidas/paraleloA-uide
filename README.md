# paraleloA-uide
El presente código es un programa "Generador de contraseñas seguro", a continuación, explicaré lo nuevo que aprendí:
- El programa utiliza los módulos o librerías "import secrets", e "import string", estas librerías son usados en software de seguridad real. "import secrets" permite generar números y elecciones aleatorias seguras  (criptográficamente fuertes), import string, da acceso a conjuntos de caracteres como letras, dígitos y símbolos
- def generate_password(length=16): Esta línea define una función llamada generate_password que recibe como parámetro la longitud de la contraseña. Si no se especifica un valor, la contraseña se genera con 16 caracteres por defecto.
- raise ValueError("La longitud mínima recomendada es 8 caracteres.") en esta línea el programa se detiene completamente si "length" es menor a 8
- En estas líneas a continuación, se selecciona una minúscula, una mayúscula, un número y un símbolo y se guarda cada una en una variable, los símbolos están definidos por los caracteres a continuación del "=":
    lowercase = string.ascii_lowercase      # abc...
    uppercase = string.ascii_uppercase      # ABC...
    digits = string.digits                  # 0123456789
    symbols = "!@#$%^&*()-_=+[]{};:,.?/|"
  - en estas líneas a continuación, se crea una lista llamada "password_chars" y se asigna por lo menos una minúscula, una mayúscula, un número y un símbolo:
  password_chars = [
    secrets.choice(lowercase),
    secrets.choice(uppercase),
    secrets.choice(digits),
    secrets.choice(symbols),

]

- En las siguientes líneas  rellenamos el resto de la contraseña con una mezcla de todo, concatenamos varios conjuntos de caracteres en una sola cadena de texto,
    all_chars = lowercase + uppercase + digits + symbols 
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_chars))

    # Mezclamos el orden para que no siempre empiece en el mismo patrón
    secrets.SystemRandom().shuffle(password_chars)

    # Unimos la lista en un string
    return "".join(password_chars)

  - Este bloque de código se ejecuta cuando el programa se inicia. Le pide al usuario la longitud de la contraseña, usa 16 caracteres por defecto si no se ingresa un valor, genera una contraseña segura llamando a la función correspondiente y muestra el resultado. Además, maneja errores para evitar que el programa falle si el usuario ingresa datos incorrectos:
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
