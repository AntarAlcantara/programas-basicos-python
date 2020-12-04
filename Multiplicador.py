if __name__ == '__main__':
	x = int()
	ran = int()
	multi = int()
	resultado = int()
	print("Escribe un numero a multiplicar")
	x = int(input())
	print("rango de multiplicacion")
	ran = int(input())
	for z in range(ran):
		print("multiplicador")
		multi = int(input())
		resultado = multi*x
		print("tu resultado es: ")
		print(resultado)
	print("¿volver a usar? (si o no): ")
	sionoraza = input()
	if sionoraza=="si":
		while True:
			print("Escribe un numero a multiplicar")
			x = int(input())
			print("rango de multiplicacion")
			ran = int(input())
			for z in range(ran):
				print("multiplicador")
				multi = int(input())
				resultado = multi*x
				print("tu resultado es: ")
				print(resultado)
			print("¿volver a usar? (si o no): ")
			sionoraza = input()
			if sionoraza=="no": break
