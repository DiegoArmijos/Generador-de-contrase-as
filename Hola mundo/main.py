import random

caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Hola este es el gestor de contraseña de python: ¿Cuántos caracteres debe tener tu contraseña? "))

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña generada y segura es:", contraseña)
