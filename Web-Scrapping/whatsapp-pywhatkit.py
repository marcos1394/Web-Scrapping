import pywhatkit

numero_celular = input("Ingresa el numero de celular: ")

pywhatkit.sendwhatmsg(numero_celular,"Test", 8, 39)


id_grupo = input("ingresa el id del grupo: ")
pywhatkit.sendwhatmsg_to_group(id_grupo, 7, 22)