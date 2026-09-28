# ==============================================================================
# BÖLÜM 1: Fonksiyonlar (def ve return Mantığı)
# SÜRE: ~25 Dakika
# ==============================================================================

# "Geçen ders değişkenleri, listeleri ve döngüleri gördük.
# Şimdi düşünün: Elimizdeki bir işlemi (örneğin kameradan gelen koordinatı piksele çevirmeyi)
# kodun içinde 50 farklı yerde yapmamız gerekiyor.
# Her seferinde aynı 5 satırı kopyala-yapıştır mı yapacağız? Kesinlikle hayır!
# Yazılımın 1 numaralı kuralı: DRY (Don't Repeat Yourself - Kendini Tekrar Etme).
# Belirli bir işi yapan kod bloklarını paketleyip isim verdiğimiz yapılara 'fonksiyon' deriz.
# Python'da fonksiyon tanımlarken 'def' (define - tanımla) anahtar kelimesini kullanırız."

# 1. En Basit Fonksiyon (Girdisiz, Çıktısız)
def karsilama_yap():
    print("---------------------------------")
    print("Kamera Takip Sistemi Başlatılıyor")
    print("---------------------------------")

# "Fonksiyonu sadece tanımlamak yetmez; çalışması için onu 'çağırmamız' (call) gerekir."
karsilama_yap()


# 2. Parametre (Girdi) Alan Fonksiyon
# "Fonksiyonları bir meyve sıkacağı gibi düşünebilirsiniz. İçine meyve atarsınız, size meyve suyu verir.
# Parantez içine yazdığımız değişkenlere 'parametre' denir. Fonksiyona dışarıdan bilgi yollarız."

def koordinat_yazdir(nokta_adi, x, y):
    print(f"[{nokta_adi}] -> X: {x}, Y: {y}")

koordinat_yazdir("İşaret Parmağı", 320, 240)
koordinat_yazdir("Başparmak", 180, 210)


# 3. Geriye Değer Döndüren Fonksiyon (return) vs Sadece Print
# "İşte programlamada en çok karıştırılan yer: 'print' ile 'return' farkı!
# Şöyle hayal edin:
# - Sadece print yapan fonksiyon: Masaya yemek getirmeyen, sadece duvardaki panoya 'Yemek hazır!' yazan bir restorandır.
#   Gözünüzle görürsünüz ama elinize bir yemek (veri) geçmez.
# - Return yapan fonksiyon ise yemeği tabağa koyup doğrudan masanıza, ELİNİZE TESLİM EDEN garsondur.
#   Yemeği aldıktan sonra ister yer, ister paket yapar eve götürürsünüz (başka değişkene atayabilir, işlem yapabilirsiniz)."

# Yanlış kullanım örneği (Sadece print):
def topla_ve_yazdir(a, b):
    print("Toplam (Sadece Ekrana Basıldı):", a + b)

sonuc1 = topla_ve_yazdir(10, 20)
print("sonuc1 kutusunun içi:", sonuc1)  # Ekrana 'None' yazar, çünkü hafızaya bir şey dönmedi!

# Doğru kullanım örneği (Return ile veriyi koda teslim etme):
def topla_ve_dondur(a, b):
    return a + b

sonuc2 = topla_ve_dondur(10, 20)
print("sonuc2 kutusunun içi:", sonuc2)  # Ekrana 30 yazar!
print("Sonucun 5 fazlası:", sonuc2 + 5) # Veri elimizde olduğu için matematik yapabiliriz.


# 4. Görüntü İşleme İçin Pratik Fonksiyon: Piksele Çevirme
# "NEDEN int() KULLANDIK?
# MediaPipe koordinatları 0.0 ile 1.0 arasında ondalıklı (float) oran olarak verir (Örn: 0.4578).
# Bunu 640 ile çarparsak 292.992 çıkar.
# Arkadaşlar, ekranda 292. piksel vardır, 293. piksel vardır; ama ASLA 292.992'nci piksel diye yarım bir piksel/lamba olamaz!
# OpenCV'ye bu sayıyı verirsek hata verir.
# Bu yüzden başına 'int()' koyarak ondalık kısmı atıp net bir tam sayı elde ederiz."

def piksele_cevir(oran, ekran_boyutu):
    piksel_degeri = int(oran * ekran_boyutu)
    return piksel_degeri

hesaplanan_x = piksele_cevir(0.5, 640)
print("0.5 oranının 640 pikseldeki tam karşılığı:", hesaplanan_x)

# ------------------------------------------------------------------------------
# [DUR & ÇALIŞTIR]
# 1. Kodu çalıştır, terminalde çıktıları göster.
# 2. Sınıfa sor: "Return neden veriyi koda teslim eder dedik, anlaşıldı mı?"
# ------------------------------------------------------------------------------