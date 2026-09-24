# ==============================================================================
# BÖLÜM 3: Karar Mekanizmaları (if/else) ve Döngüler (for)
# SÜRE: ~25 Dakika
# ==============================================================================

# "Bilgisayarı akıllı yapan şey karar verebilmesidir.
# 'Eğer (if) kullanıcı butona bastıysa kamerayı aç, basmadıysa (else) bekle.'
# Koşulun sonuna İKİ NOKTA ÜST ÜSTE (:) koyarız. Bu, 'şartım bitti, şimdi bu şart sağlanırsa ne yapacağımı söylüyorum' demektir."

x_koordinati = 450
ekran_ortasi = 320

# [ÖĞRENCİYE GİRİNTİ (INDENTATION) UYARISI]:
# "Python'da süslü parantez blokları yoktur. Bir kodun if'in İÇİNDE olduğunu anlatmak için
# klavyedeki TAB tuşuna basarak içeri girinti (4 boşluk) bırakırız. İçerideki kodlar sadece şart tutarsa çalışır!"

if x_koordinati > ekran_ortasi:
    print("Parmak ekranın SAĞ tarafında!")
elif x_koordinati == ekran_ortasi:   # Dikkat: İki tane == karşılaştırma ('eşit midir?') demektir.
    print("Parmak tam ORTADA!")
else:
    print("Parmak ekranın SOL tarafında!")


# "Döngüler: Bilgisayara amelelik yaptırma sanatıdır.
# Elimizde 1000 tane koordinat varsa 1000 satır print() yazmayız.
# 'for' döngüsü listenin başına geçer, her turda sıradaki elemanı 'x' isimli geçici bir kutuya koyar ve içeri girer.
# Liste bitene kadar döngü kendi kendine döner."

x_noktalari = [120, 350, 50, 480, 210]

for x in x_noktalari:
    print("Sıradaki piksel taranıyor:", x)

# ------------------------------------------------------------------------------
# [DUR & ÇALIŞTIR]
# 1. Kodu çalıştır, terminalde döngünün sayıları nasıl alt alta döktüğünü göster.
# 2. [OLASI HATA]: 'IndentationError: expected an indented block'.
#    Öğrenci if veya for'un altındaki satırı içeri kaydırmayı unutmuştur. Hemen TAB tuşunu göster.
# ------------------------------------------------------------------------------