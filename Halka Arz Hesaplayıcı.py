#Şirketlerin halka arzlarına katılımda ne kadar kar edileceğinin belirlenmesi için yazılan bir hesaplayıcıdır.
print("Halka arz hesaplayıcıya hoşgeldiniz.")
a = float(input("Hissenin Halka Arz Fiyatı Kaç Lira ? "))
b = int(a)
kactavan = int(input("Kaç Defa Tavan Yapması Öngörülüyor ?"))
kaclot = int(input("Kaç lot düştü ?"))

sonuc = 0

for i in range(1,kactavan+1):
    sonuc = a + a/10
    a = sonuc
    floatsonuc= "{:.2f}".format(sonuc)

    print(i,". Tavanda fiyatı", float(floatsonuc),"TL'dir","Açılış fiyatıyla Arasındaki Fark",int(sonuc) - b ,"TL'dir","Toplam edilecek kar =",int(sonuc * kaclot))







