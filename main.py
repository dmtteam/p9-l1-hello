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

sty2 = round((1 + ((m1r2+interest)/1200)) * dec1 - rate, 2)
print((left), str(sty2), ",which is:", round((dec1 - sty2), 2), (less))

lut2 = round((1 + ((m2r2+interest)/1200)) * sty2 - rate, 2)
print((left), str(lut2), ",which is:", round((sty2 -lut2), 2), (less))

mar2 = round((1 + ((m3r2+interest)/1200)) * lut2 - rate, 2)
print((left), str(mar2), ",which is:", round((lut2 -mar2), 2), (less))

kwi2 = round((1 + ((m4r2+interest)/1200)) * mar2 - rate, 2)
print((left), str(kwi2), ",which is:", round((mar2 -kwi2), 2), (less))

maj2 = round((1 + ((m5r2+interest)/1200)) * kwi2 - rate, 2)
print((left), str(maj2), ",which is:", round((kwi2 -maj2), 2), (less))

cze2 = round((1 + ((m6r2+interest)/1200)) * maj2 - rate, 2)
print((left), str(cze2), ",which is:", round((maj2 -cze2), 2), (less))

lip2 = round((1 + ((m7r2+interest)/1200)) * cze2 - rate, 2)
print((left), str(lip2), ",which is:", round((cze2 -lip2), 2), (less))

sie2 = round((1 + ((m8r2+interest)/1200)) * lip2 - rate, 2)
print((left), str(sie2), ",which is:", round((lip2 -sie2), 2), (less))

wrz2 = round((1 + ((m9r2+interest)/1200)) * sie2 - rate, 2)
print((left), str(wrz2), ",which is:", round((sie2 -wrz2), 2), (less))

paz2 = round((1 + ((m10r2+interest)/1200)) * wrz2 - rate, 2)
print((left), str(paz2), ",which is:", round((wrz2 -paz2), 2), (less))

nov2 = round((1 + ((m11r2+interest)/1200)) * paz2 - rate, 2)
print((left), str(nov2), ",which is:", round((paz2 -nov2), 2), (less))

dec2 = round((1 + ((m12r2+interest)/1200)) * nov2 - rate, 2)
print((left), str(dec2), ",which is:", round((nov2 -dec2), 2), (less))


