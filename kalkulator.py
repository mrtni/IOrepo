def dodawanie():
		return a + b
def get_info():
	return "To jest program kalkulator stworzony przeze mnie"
try:
	a = int(input('Podaj pierwsza liczbe: '))
	b = int(input('Podaj druga liczbe: '))
	print(dodawanie(a,b))
except ValueError as ve: 
	print('Wprowadzono bledne dane, koncze dzialanie...')

print(get_info())
input()