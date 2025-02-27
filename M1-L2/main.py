import random

caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud= int(input("Indique en números, ¿de cuántos dígitos desea su contraseña?"))

contrasena= ""
for i in range(longitud):
    contrasena += random.choice(caracteres)
print ("Su contraseña es:", contrasena)