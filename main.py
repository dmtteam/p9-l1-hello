# Stwórz program, który na podstawie
# tabeli inflacji
# wartości oprocentowania kredytu,
# kwoty początkowej kredytu
# i stałej wartości raty wyliczy
# wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

# Niech program wydrukuje dla każdego miesiąca następującą linię:
# Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

# Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację),
# i kwota raty były pobierane ze standardowego wejścia (terminal).

# Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej.
# Skopiuj z niego wartości inflacji dla każdego miesiąca.

# Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium powinno zawierać więcej, niż jeden commit.


txt1linia="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
txt2linia="Dzień Dobry! Witamy w instytucji: PYTHONbank!"
txt3linia="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
print (txt1linia)
print (txt2linia)
print (txt3linia)
print("Ile USD dzis potrzebujesz? Smialo - mamy duzo kasy dla Ciebie:")
kwotakredytu=int(input())
print("Wprowadz za nas % kredytu /ponad inflacje/: ")
oprocentowanie=int(input())
print("Jaka miesieczna rate jestes w stanie splacac? Oragnow nie przyjmujemy ")
ratadeklarowana=int(input())
komunikat1="OK. Mozemy Ci udzielic kredytu na 24 miesciace. Parametry:"
komunikat2="Kwota:"
komunikat3="Oprocentowanie:"
komunikat4="Rata:"
# do zrobienia: print parametrow w jednej linii - takie podsumowanie - jak?
# print(komunikat1 + kwotakredytu + komunikat2 + oprocentowanie + komunikat3 + ratadeklarowana)
# ponizej definiowanie inflacji ze wsadu .xls - int - zaookraglenie zrobic
m1r1=int(1.592824484)
#m2r1=int(0.453509101)
##m4r1=int(1.261254407)
#m5r1=int(1.782526286)
#m6r1=int(2.329384541)
#m7r1=int(1.502229842)
#m8r1=int(1.782526286)
#m9r1=int(2.328848994)
#m10r1=int(0.616921348)
#m11r1=int(2.352295886)
#m12r1=int(0.337779545)
#m1r2=int(1.577035247)
#m2r2=int(-0.292781443)
#m3r2=int(2.48619659)
#m4r2=int(0.267110318)
#m5r2=int(1.417952672)
#m6r2=int(1.054243267)
#m7r2=int(1.480520104)
#m8r2=int(1.577035247)
#m9r2=int(-0.07742069)
#m10r2=int(1.165733399)
#m11r2=int(-0.404186718)
#m12r2=int(1.499708521)
# Niech program wydrukuje dla każdego miesiąca następującą linię:
# Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
# formula z xls to(1 + ((inflacjadanymiesiac+opocentowanie)/kwotakreydtu)) * kwotakredytu - ratamiesieczna
#print("Pozostala kwota kredytu to:") + ((kwotakredytu) - (m1r1) + oprocentowanie)/ (kwotakredytu) - ratadeklarowana
zostalo='Pozostala kwota kredytu'
mniej="Mniej niz w poprzednim miesiacu"
# tu problem z wyslistowaniem zdefiniowanego int'a
print((zostalo) + int(m1r1) + (mniej))
