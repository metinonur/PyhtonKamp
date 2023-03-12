print("Reco benim yarramı yesin")
baslik = "Ya receeep"
print(baslik)
#string => metinsel ifade 
baslik = "Ya malii"
print(baslik)
#int intager => tam sayı 
vade = 36
ekVade = 12
vade2 = "36" 
vade + 2
#float, decimel, double
aylikOdeme = 200.50
#bool, boolean => true false
yukselisteMi = False

#matematiksel operatörler
print(5 + 5)
print(vade + 15)
print(vade + ekVade)
print(5 - 5)

# * çarpma operasyonu
print(5*5)
print(vade*ekVade)

# / bölme operasyonu
print(vade/ekVade)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20
print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10%2)


#mantıksal operatörler
print(1 == 1)
print(1 == 2)
print(1 < 5)
print(1 > 5)
print(1<=1)

# ctrl+k +c seçili satırları yorum satırı yapma kısayolu

# != eşit değildir demek
print(1 != 1)
print(1 != 2)

# or and

print(1 > 2 or 5 > 2)
print(1 < 2 and 5 > 2 )

print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapıları
# if else 


sayi = 20
sayi2 = 20
if  sayi>sayi2:
    print("sayi2 büyüktür sayi")
elif sayi==sayi2 :
    print("iki sayı eşittir") 
else :  
    print("sayı sayı2den küçüktür")
