# ==============================================================================
# BÖLÜM 1: Ekrana Yazdırma ve Değişkenler
# SÜRE: ~20 Dakika
# ==============================================================================

# "Python'da bilgisayarla konuşmanın en doğrudan yolu 'print()' fonksiyonudur.
# Parantez içi, bilgisayara 'bunu al ve terminale fırlat' demektir.
# Metin yazıyorsak Python bunun bir yazı olduğunu anlasın diye çift tırnak ("...")
# veya tek tırnak ('...') içine alırız. Tırnak koymazsak bunu bir komut sanır ve hata verir."

print("YAZGİT Python Eğitimine Hoş Geldiniz!")


# Her şeyi anında ekrana basmak yetmez; verileri bilgisayarın hafızasında tutmalıyız.
# Değişken dediğimiz şey, üzerine etiket yapıştırdığımız bir ayakkabı kutusu gibidir.
# Sol tarafa kutunun adını (etiketi), sağ tarafa içine koyacağımız değeri yazarız.
# Aradaki tek eşittir (=) 'eşittir' demek değildir; 'sağdakini al, soldaki kutunun içine koy (atama yap)' demektir.
# C veya Java gibi dillerin aksine Python çok zekidir; 'bu bir tam sayıdır' diye belirtmenize gerek kalmaz, içine bakıp kendisi anlar."

ogrenci_sayisi = 25       # int (Integer - Tam sayı): Sayma işlemleri, piksel koordinatları.
kamera_fps = 29.97         # float (Kayan noktalı sayı): Ondalıklı hassas değerler.
topluluk_adi = "YAZGİT"    # str (String - Metin): Yazılar, dosya yolları.
kamera_acik_mi = True      # bool (Boolean): Sadece True (Doğru/1) veya False (Yanlış/0) olabilir.

# "Print fonksiyonunun içine kutuların adını virgülle yan yana yazarak bastırabiliriz."
print("Topluluk:", topluluk_adi)
print("Katılımcı Sayısı:", ogrenci_sayisi)
print("Kamera çalışıyor mu?:", kamera_acik_mi)

# ------------------------------------------------------------------------------
# [DUR & ÇALIŞTIR]
# 1. VS Code sağ üstteki 'Run' üçgenine bas veya terminale 'python bolum1_degiskenler.py' yaz.
# 2. Terminal çıktısını göster.
# 3. Sınıfı kontrol et yazan var mı.
# 4. [OLASI HATA]: Tırnağı kapatmayı unutanlar 'SyntaxError: unterminated string literal' alır.
# ------------------------------------------------------------------------------