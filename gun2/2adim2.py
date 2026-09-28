# ==============================================================================
# BÖLÜM 2: NumPy Nedir ve Görüntü İşlemede Ne İşe Yarar?
# SÜRE: ~20 Dakika
# ==============================================================================

# "Şimdi kritik soru: Python'ın kendi listeleri varken veri bilimciler ve görüntü işlemeciler
# neden sürekli 'NumPy' kütüphanesini kullanır?
# Matematik formülleriyle kafanızı şişirmeyeceğim. Bilmeniz gereken TEK ŞEY şudur:
# 1) Dijital dünyada her görüntü, aslında sayılardan oluşan devasa bir tablodur (matristir).
# 2) Python'ın normal listeleri bu milyonlarca sayıyı işlerken yavaş kalır.
# 3) NumPy (Numerical Python), C diliyle yazılmış arka planı sayesinde bu devasa sayı tablolarını
#    ışık hızında çarpar, böler ve filtreler.
# Harici kütüphaneleri kodumuza 'import' anahtar kelimesiyle çağırırız.
# 'as np' demek ise: 'Koda her seferinde uzun uzun numpy yazmayayım, ona kısaca np diyeyim' demektir."

import numpy as np

# Normal bir Python listesi:
python_listesi = [10, 20, 30]

# NumPy Dizisi (Array):
numpy_dizisi = np.array([10, 20, 30])

print("NumPy Dizisi:", numpy_dizisi)

# "Görüntü İşleme Ön İncelemesi:
# Bir web kamerasından gelen tek bir kare düşünün: 640 piksel genişlik, 480 piksel yükseklik.
# NumPy ile tamamen siyah bir ekran (tüm pikselleri 0 olan bir matris) oluşturalım:"

siyah_tuval = np.zeros((480, 640)) # 480 satır, 640 sütunluk sıfırlar tablosu

print("Tuvalin Boyutu (shape):", siyah_tuval.shape)
# "shape komutu bize görüntünün (Yükseklik, Genişlik) ölçüsünü söyler.
# Haftaya OpenCV kamerayı açtığında arkada tam olarak bu matris dönecek!"

# ------------------------------------------------------------------------------
# [DUR & ÇALIŞTIR]
# 1. Kodu çalıştır. 
# 2. [OLASI HATA]: 'ModuleNotFoundError: No module named numpy' alan olursa:
#    kütüphaneler yüklenecek...
# ------------------------------------------------------------------------------