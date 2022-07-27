print("Enter the loan amount:")
loan_amount = int(input())

print("Enter the loan interest rate: ")
interest = float(input())

print("Enter the monthly rate: ")
rate = float(input())

# inflation def

m1r1 = 1.592824484
m2r1 = -0.453509101
m3r1 = 2.324671717
m4r1 = 1.261254407
m5r1 = 1.782526286
m6r1 = 2.329384541
m7r1 = 1.502229842
m8r1 = 1.782526286
m9r1 = 2.328848994
m10r1 = 0.616921348
m11r1 = 2.352295886
m12r1 = 0.337779545
m1r2 = 1.577035247
m2r2 = -0.292781443
m3r2 = 2.48619659
m4r2 = 0.267110318
m5r2 = 1.417952672
m6r2 = 1.054243267
m7r2 = 1.480520104
m8r2 = 1.577035247
m9r2 = -0.07742069
m10r2 = 1.165733399
m11r2 = -0.404186718
m12r2 = 1.499708521

left = "The remaining loan amount is:"
less = "less than the previous month"

jan1 = round((1 + ((m1r1+interest)/1200)) * loan_amount - rate, 2)
print((left), str(jan1), ",which is:", round((loan_amount - jan1), 2), (less))

feb1 = round((1 + ((m2r1+interest)/1200)) * jan1 - rate, 2)
print((left), str(feb1), ",which is:", round((jan1 -feb1), 2), (less))

mar1 = round((1 + ((m3r1+interest)/1200)) * feb1 - rate, 2)
print((left), str(mar1), ",which is:", round((feb1 -mar1), 2), (less))

apr1 = round((1 + ((m4r1+interest)/1200)) * mar1 - rate, 2)
print((left), str(apr1), ",which is:", round((mar1 -apr1), 2), (less))

may1 = round((1 + ((m5r1+interest)/1200)) * apr1 - rate, 2)
print((left), str(may1), ",which is:", round((apr1 -may1), 2), (less))

jun1 = round((1 + ((m6r1+interest)/1200)) * may1 - rate, 2)
print((left), str(jun1), ",which is:", round((may1 -jun1), 2), (less))

jul1 = round((1 + ((m7r1+interest)/1200)) * jun1 - rate, 2)
print((left), str(jul1), ",which is:", round((jun1 -jul1), 2), (less))

aug1 = round((1 + ((m8r1+interest)/1200)) * jul1 - rate, 2)
print((left), str(aug1), ",which is:", round((jul1 -aug1), 2), (less))

sep1 = round((1 + ((m9r1+interest)/1200)) * aug1 - rate, 2)
print((left), str(sep1), ",which is:", round((aug1 -sep1), 2), (less))

oct1 = round((1 + ((m10r1+interest)/1200)) * sep1 - rate, 2)
print((left), str(oct1), ",which is:", round((sep1 -oct1), 2), (less))

nov1 = round((1 + ((m11r1+interest)/1200)) * sep1 - rate, 2)
print((left), str(nov1), ",which is:", round((sep1 -nov1), 2), (less))

dec1 = round((1 + ((m12r1+interest)/1200)) * nov1 - rate, 2)
print((left), str(dec1), ",which is:", round((nov1 -dec1), 2), (less))

# second year

jan2 = round((1 + ((m1r2+interest)/1200)) * dec1 - rate, 2)
print((left), str(jan2), ",which is:", round((dec1 - jan2), 2), (less))

feb2 = round((1 + ((m2r2+interest)/1200)) * jan2 - rate, 2)
print((left), str(feb2), ",which is:", round((jan2 -feb2), 2), (less))

mar2 = round((1 + ((m3r2+interest)/1200)) * feb2 - rate, 2)
print((left), str(mar2), ",which is:", round((feb2 -mar2), 2), (less))

apr2 = round((1 + ((m4r2+interest)/1200)) * mar2 - rate, 2)
print((left), str(apr2), ",which is:", round((mar2 -apr2), 2), (less))

may2 = round((1 + ((m5r2+interest)/1200)) * apr2 - rate, 2)
print((left), str(may2), ",which is:", round((apr2 -may2), 2), (less))

jun2 = round((1 + ((m6r2+interest)/1200)) * may2 - rate, 2)
print((left), str(jun2), ",which is:", round((may2 -jun2), 2), (less))

jul2 = round((1 + ((m7r2+interest)/1200)) * jun2 - rate, 2)
print((left), str(jul2), ",which is:", round((jun2 -jul2), 2), (less))

aug2 = round((1 + ((m8r2+interest)/1200)) * jul2 - rate, 2)
print((left), str(aug2), ",which is:", round((jul2 -aug2), 2), (less))

sep2 = round((1 + ((m9r2+interest)/1200)) * aug2 - rate, 2)
print((left), str(sep2), ",which is:", round((aug2 -sep2), 2), (less))

oct2 = round((1 + ((m10r2+interest)/1200)) * sep2 - rate, 2)
print((left), str(oct2), ",which is:", round((sep2 -oct2), 2), (less))

nov2 = round((1 + ((m11r2+interest)/1200)) * oct2 - rate, 2)
print((left), str(nov2), ",which is:", round((oct2 -nov2), 2), (less))

dec2 = round((1 + ((m12r2+interest)/1200)) * nov2 - rate, 2)
print((left), str(dec2), ",which is:", round((nov2 -dec2), 2), (less))


