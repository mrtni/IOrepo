def dodawanie():
		return a + b

try:
	a = int(input('Podaj pierwsza liczbe: '))
	b = int(input('Podaj druga liczbe: '))
	print(dodawanie(a,b))
except ValueError as ve: 
	print('Wprowadzono bledne dane, koncze dzialanie...')
input()