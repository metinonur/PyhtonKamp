faiz = 1.59   #float
vade = "36"   #str
krediAdi = "İhtiyaç kredisi "  #str

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)

#vade = int(input("Lütfen istediğiniz vade sayısını giriniz "))     #type çevirme işlemini printe de yazabiliriz 
print(vade)
#vade = vade + 12 

#string interpolition
#seçtiğiniz vade sonucu ortaya çıkan vade
print("Seçtiğiniz vade sonucu ortaya çıkan vade :" + str(vade))      # type dönüştürme
print("Seçtiğiniz vade sonucu ortaya çıkan  vade :{vadeSayisi}" .format(vadeSayisi=vade))    #format kullanımı
print(f"Seçtiğniz vade sonucu ortaya çıkan vade : {vade}")    #f-string kullanım

isim = "Metin"
metin = "Merhaba {name}".format(name=isim)
print(metin)


# f-string kullanımı 
metin = f"Hoşgeldiniz{isim}" 

# listeler 
#döngüler

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler[0])
print(len(krediler))

krediler.append("Özel Kredi")
print(krediler)

krediler.append("Araç Kredisi")
krediler.pop(0)                      #pop girilen sıradaki elemanı siler
print(krediler)
krediler.remove("Taşıt Kredisi")    #remove  girilen elemanı siler
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])    #extend birden fazla veriyi tek seferde girmek için kullanılıyor
print(krediler)

#for döngüsü


for i in range(10):
     print(i)
print("**********************************")
for i in range(5,10):
     print(i)
print("**********************************")
for i in range(0,51,10):                        #ilk "başlangıç" ikinci "son" üçüncü "kaçar arttığı"
     print(i)

for kredi in krediler:
     print(kredi)
print("********************")
for i in range(len(krediler)):
     print(krediler[i])

print("**************************************")

i = 0
while i<10:
     print("x")
     i=i+1

# while döngüsünde "break" komutuyla sonsuz döngüleri kırabiliriz

i = 0
while i<len(krediler):
     i+=1
     print(krediler[i])
     if krediler[i] == "Y Kredisi":
          break
     #Y kredisinden sonra döngü break komutu yazdığımız için devam etmiyor ve Z kredisini çıktıda görmüyoruz

#fonksiyonlar       

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
calculate()
calculateWithParams(100,20)
calculateWithParams(100,50)


def sayHello(name):
     print(f"Merhaba {name}")

sayHello("Metin")



def calculateAndReturn(price,discount):
     return price-discount

yeniFiyat = calculateAndReturn(500,20)
print(yeniFiyat)

def calculatePrice(price,discount):
     print(price-discount)

def calculatePriceAndReturn(price,discount):
     return price-discount
print("*******************************")
fonk1 = calculatePrice(100,20)
fonk2 = calculatePriceAndReturn(300,20)
print(f"120.satır {fonk1}")
print(f"121.satır {fonk2}")
print("********************************")

#120.satırda  fonksiyondan bir geri dönüş olmadığı için çıktı alamımyoruz

