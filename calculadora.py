#Soliciatar que ingresen Datos de usuario

miCadena="CALCULADORA DE MASA CORPORAL (IMC)"
#En esta parte me base en realizar un pequeño titulo de nuestra calculadora de masa corpolar con print miCadena.title que lo estuve
#observando en unos videos de youtube que me sirvieron de inspiracion y ayudandome con un pequeño libro de programacion basica nivel bachillerato

print(miCadena.title())
nombre = input("Ingresa tu nombre:") 
apellido_paterno = input("Ingresa tu apellido paterno:") 
apellido_materno = input("Ingresa tu apellido materno:")
edad = int(input("Ingresa tu edad:")) 
peso = float(input("Peso (kilogramos): "))
estatura = float(input("Estatura (centimetros):" )) /100

#En la linea 8 comenzamos a ingresar y escribir el codigo para pedirle a nuestros usuarios su informacion personal para obtener un mejor
#Resultado sobre su IMC basandonos en la formula. De igual forma aprendi a utilizar las dobles comillas de una mejor manera al igual que los
#parentesis son muy importantes para poder programar de una buena manera y que nuestro codigo corra de una de las mejores formas
#Uno de los obstaculos que tuve al estar realizando esta calculadora, fuel el evitar espacios vacios, o que colocaran caracteres que no eran
#Aun sigo aprendiendo y realmente recomendare el curso con amigos, familiares y conocidos porque me ha hecho aprender otras maneras de programar al 
#igual que como utilizar python de una manera correcta
#Cualquier duda o ajuste que sea necesario que realice estoy en la disposicion

#Calcularemos el indice de Masa Corporal (IMC) con la formula imc = peso / (estatura**2)

#Ahora mostraremos los datos ingresados y el IMC

print("\n--- Datos Personales ---")
print("Nombre Completo:", nombre, apellido_paterno, apellido_materno)
print("Edad:", edad, "años") 
print("Peso:", peso,"kg")
print("Estatura:", estatura, "cm")
imc = round(peso / (estatura * estatura), 1)
print("Su IMC es: {}" .format(imc))

#Para finalizar aqui nos mostrara el resultado de nuestra masa corporal y verificamos si en verdad es veredicta
