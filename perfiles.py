import os
import sys
from string import Template

#abrimos el archivo
filein = open('/var/www/html/index.html')
#leyendo archivo
src = Template(filein.read())
#datos del documento
nombre =  input("ingrese su nombre:  ")
apellido =  input("ingrese su apellido:  ")
tel =  input("ingrese su telefono:  ")
ced =  input("ingrese su cedula:  ")
email =  input("ingrese su email:  ")
direc =  input("ingrese su direccion:  ")
fec_nac =  input("ingrese su fecha de nacimiento:  ")
prof =  input("ingrese su profesion:  ")
idioma =  input("ingrese sus idiomas (separado por comas):  ")
sexo =  input("ingrese su sexo:  ")
est_civil =  input("ingrese su estado civil:  ")
color_fav =  input("ingrese su color favorito:  ")
#Diccionario de datos
d = {'nombre':nombre, 'apellido':apellido, 'tel':tel, 'ced':ced, 'email':email, 'direc':direc, 'fec_nac':fec_nac, 'prof':prof, 'idioma':idioma, 'sexo':sexo, 'est_civil':est_civil, 'color_fav':color_fav }
#sustituyendo los valores a las variables de la plantilla
result = src.substitute(d)
try:
    os.mkdir('Perfiles')
    filein2 = open('Perfiles/'+str(ced)+'.html', 'w')
    filein2.writelines(result)
    print ("creando carpeta")
    print ("guardando archivo")
except OSError:
    if os.path.exist("Perfiles"):
        filein2 = open('Perfiles/'+str(ced)+'.html', 'w')
        filein2.writelines(result)
        print ("guardando archivo")

while True:
    pregunta = input ("presione N si quiere continuar y S si quiere salir")
    if pregunta == "N":
        os.system(r"perfiles.py")
    elif pregunta == "S":
        sys.exit()
