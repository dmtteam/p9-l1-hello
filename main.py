print("Enter the loan amount:")
loanamount = int(input())

print("Enter the loan interest rate: ")
interest = float(input())

print("Enter the monthly rate: ")
rate = float(input())

# inflation def

m1r1=1.592824484
m2r1=-0.453509101
m3r1=2.324671717
m4r1=1.261254407
m5r1=1.782526286
m6r1=2.329384541
m7r1=1.502229842
m8r1=1.782526286
m9r1=2.328848994
m10r1=0.616921348
m11r1=2.352295886
m12r1=0.337779545
m1r2=1.577035247
m2r2=-0.292781443
m3r2=2.48619659
m4r2=0.267110318
m5r2=1.417952672
m6r2=1.054243267
m7r2=1.480520104
m8r2=1.577035247
m9r2=-0.07742069
m10r2=1.165733399
m11r2=-0.404186718
m12r2=1.499708521

left = "The remaining loan amount is:"
less = "less than the previous month"

sty1=round((1 + ((m1r1+interest)/1200)) * loanamount - rate, 2)
print((left), str(sty1), ",wchich is:", round((loanamount - sty1), 2), (less))

lut1=round((1 + ((m2r1+interest)/1200)) * sty1 - rate, 2)
print((left), str(lut1), ",wchich is:", round((sty1 -lut1), 2), (less))

mar1=round((1 + ((m3r1+interest)/1200)) * lut1 - rate, 2)
print((left), str(mar1), ",wchich is:", round((lut1 -mar1), 2), (less))

kwi1=round((1 + ((m4r1+interest)/1200)) * mar1 - rate, 2)
print((left), str(kwi1), ",wchich is:", round((mar1 -kwi1), 2), (less))

maj1=round((1 + ((m5r1+interest)/1200)) * kwi1 - rate, 2)
print((left), str(maj1), ",wchich is:", round((kwi1 -maj1), 2), (less))

cze1=round((1 + ((m6r1+interest)/1200)) * maj1 - rate, 2)
print((left), str(cze1), ",wchich is:", round((maj1 -cze1), 2), (less))

lip1=round((1 + ((m7r1+interest)/1200)) * cze1 - rate, 2)
print((left), str(lip1), ",wchich is:", round((cze1 -lip1), 2), (less))

sie1=round((1 + ((m8r1+interest)/1200)) * lip1 - rate, 2)
print((left), str(sie1), ",wchich is:", round((lip1 -sie1), 2), (less))

wrz1=round((1 + ((m9r1+interest)/1200)) * sie1 - rate, 2)
print((left), str(wrz1), ",wchich is:", round((sie1 -wrz1), 2), (less))

paz1=round((1 + ((m10r1+interest)/1200)) * wrz1 - rate, 2)
print((left), str(paz1), ",wchich is:", round((wrz1 -paz1), 2), (less))

lis1=round((1 + ((m11r1+interest)/1200)) * paz1 - rate, 2)
print((left), str(lis1), ",wchich is:", round((paz1 -lis1), 2), (less))

gru1=round((1 + ((m12r1+interest)/1200)) * lis1 - rate, 2)
print((left), str(gru1), ",wchich is:", round((lis1 -gru1), 2), (less))

# second year

sty2=round((1 + ((m1r2+interest)/1200)) * gru1 - rate, 2)
print((left), str(sty2), ",wchich is:", round((gru1 - sty2), 2), (less))

lut2=round((1 + ((m2r2+interest)/1200)) * sty2 - rate, 2)
print((left), str(lut2), ",wchich is:", round((sty2 -lut2), 2), (less))

mar2=round((1 + ((m3r2+interest)/1200)) * lut2 - rate, 2)
print((left), str(mar2), ",wchich is:", round((lut2 -mar2), 2), (less))

kwi2=round((1 + ((m4r2+interest)/1200)) * mar2 - rate, 2)
print((left), str(kwi2), ",wchich is:", round((mar2 -kwi2), 2), (less))

maj2=round((1 + ((m5r2+interest)/1200)) * kwi2 - rate, 2)
print((left), str(maj2), ",wchich is:", round((kwi2 -maj2), 2), (less))

cze2=round((1 + ((m6r2+interest)/1200)) * maj2 - rate, 2)
print((left), str(cze2), ",wchich is:", round((maj2 -cze2), 2), (less))

lip2=round((1 + ((m7r2+interest)/1200)) * cze2 - rate, 2)
print((left), str(lip2), ",wchich is:", round((cze2 -lip2), 2), (less))

sie2=round((1 + ((m8r2+interest)/1200)) * lip2 - rate, 2)
print((left), str(sie2), ",wchich is:", round((lip2 -sie2), 2), (less))

wrz2=round((1 + ((m9r2+interest)/1200)) * sie2 - rate, 2)
print((left), str(wrz2), ",wchich is:", round((sie2 -wrz2), 2), (less))

paz2=round((1 + ((m10r2+interest)/1200)) * wrz2 - rate, 2)
print((left), str(paz2), ",wchich is:", round((wrz2 -paz2), 2), (less))

lis2=round((1 + ((m11r2+interest)/1200)) * paz2 - rate, 2)
print((left), str(lis2), ",wchich is:", round((paz2 -lis2), 2), (less))

gru2=round((1 + ((m12r2+interest)/1200)) * lis2 - rate, 2)
print((left), str(gru2), ",wchich is:", round((lis2 -gru2), 2), (less))


