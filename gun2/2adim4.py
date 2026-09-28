# ==============================================================================
# BÖLÜM 4: Kütüphane Kurulumları ve Sürpriz Kamera Testi!
# SÜRE: ~25 Dakika
# ==============================================================================

# "Geldik günün en önemli yerine! Haftaya kamerayı açacağız ve el takibi yapacağız.
# Bunun için iki kütüphaneye ihtiyacımız var:
# 1) opencv-python: Kameraya erişmemizi, görüntüleri işlememizi sağlayan gözümüz.
# 2) mediapipe: Google'ın geliştirdiği hazır yapay zeka modeli. Başka projelerde kendimiz de model eğitebiliriz
#    ancak MediaPipe hazır eğitilmiş olduğu için bizi saatlerce model eğitmekten kurtarır.
#
# ŞİMDİ HERKES VS CODE ALTINDAKİ TERMİNALİ AÇSIN (Kısayol: Ctrl + ` veya Terminal -> New Terminal):
# Şu komutu yazıp Enter'a basıyoruz:
# pip install opencv-python mediapipe numpy
# "

# [KURULUM KONTROLÜ]:
import cv2
import mediapipe as mp
import numpy as np

print("\nTEBRİKLER!")
print("OpenCV Versiyonu :", cv2.__version__)
print("MediaPipe Başarıyla Yüklendi!")
print("NumPy Versiyonu  :", np.__version__)

# ------------------------------------------------------------------------------
# [SÜRPRİZ KOD - İLK KAMERA TESTİ]:
# "Madem her şeyi kurduk, haftaya bırakmayalım.
# Şimdi kameramıza kodla ilk 'merhaba'mızı diyelim!"
# ------------------------------------------------------------------------------

# Bilgisayarın varsayılan kamerasını (0 numaralı index) başlatıyoruz
kamera = cv2.VideoCapture(0)

print("\nKamera açılıyor... Kapatmak için kamera penceresi üzerindeyken 'q' tuşuna basın.")

while True:
    # Kameradan anlık kareyi okuyoruz
    # basarili: Görüntü geldi mi? (True/False)
    # kare: Gelen görüntünün NumPy matrisi
    basarili, kare = kamera.read()
    
    if not basarili:
        print("Kamera görüntüsü alınamadı!")
        break

    # Ekrana canlı pencereyi açıyoruz
    cv2.imshow("YAZGIT - Ilk Kamera Testi", kare)

    # 1 milisaniye klavyeyi dinle; eğer 'q' tuşuna basıldıysa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
kamera.release()
cv2.destroyAllWindows()
print("Kamera başarıyla kapatıldı. Haftaya el takibine %100 hazırsınız!")

# ------------------------------------------------------------------------------
# [OLASI HATALAR VE EĞİTMEN ÇÖZÜMLERİ]
# 1. HATA: "'pip' is not recognized / pip komutu bulunamadı":
#    ÇÖZÜM: Windows'ta Python kurulurken PATH işaretlenmemiştir.
#    Hemen terminalde şunu yazdır: "python -m pip install opencv-python mediapipe numpy"
# 2. HATA: Kamera penceresi açılmıyor veya siyah ekran veriyor:
#    ÇÖZÜM: Harici kamera takılıysa veya sanal kamera varsa cv2.VideoCapture(0) yerine cv2.VideoCapture(1) denet.
# 3. HATA: Kurulum çok yavaş / internet zayıf:
#    ÇÖZÜM: Yanındaki arkadaşıyla eşleşmesini (pair programming) söyle, dersi kilitleme.
# ------------------------------------------------------------------------------