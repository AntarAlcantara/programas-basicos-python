from random import randint

if __name__ == '__main__':
	intentos = 10
	numeroM = randint(0,99)+1
	print("Adivina el numero (de 1 a 100):")
	ingresado = int(input())
	while numeroM != ingresado and intentos!=0:
		if numeroM > ingresado:
			print("Te falta papi")
		else:
			print("Te fuiste muy lejos baby")
		print("Todavia te quedan ",intentos," intentos:")
		ingresado = float(input())
		intentos = intentos-1
	if numeroM==ingresado:
		print("Ya le atinaste en ",10-intentos," intentos.")
	else:
		print("Numero correcto: ",numeroM)
