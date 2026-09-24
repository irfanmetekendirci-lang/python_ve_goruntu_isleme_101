# ==============================================================================
# BÖLÜM 4: Ders Sonu Pratiği - "Mini Koordinat Filtresi"
# SÜRE: ~15-20 Dakika
# ==============================================================================

# "Şimdi bugün öğrendiğimiz 3 büyük silahı birleştireceğiz:
# 1. Listeler (Veriyi tutmak için)
# 2. Döngüler (Listenin içini tek tek gezmek için)
# 3. Koşullar (İstediğimiz noktayı seçip ayıklamak için)
#
# SENARYO:
# Kameramız 640 piksel genişliğinde olsun. Ekranın tam ortası 320'dir.
# MediaPipe'tan kameraya gelen rastgele parmak noktaları aldığımızı hayal edelim.
# Görevimiz: Sadece ekranın sağ yarısına (320'den büyük) düşen noktaları bulup
# 'sagdaki_noktalar' adında yeni, temiz bir listeye toplamak!"

# 1. Adım: Ham verimiz (Temsili kamera koordinatları)
gelen_koordinatlar = [110, 450, 320, 580, 95, 410, 200]

# 2. Adım: Filtrelenenleri koyacağımız boş bir çekmece/kutu açıyoruz
sagdaki_noktalar = []

# 3. Adım: For döngüsüyle tüm noktaları tek tek geziyoruz
for nokta in gelen_koordinatlar:
    # 4. Adım: Şartımızı koşuyoruz (Nokta 320'den büyük mü?)
    if nokta > 320:
        # Şart tuttuysa, .append() yeteneğini kullanarak boş listemize atıyoruz!
        sagdaki_noktalar.append(nokta)

# "Döngünün DIŞINA çıkıyoruz (girintiyi siliyoruz) çünkü sonucu sadece 1 kere bastırmak istiyoruz."
print("--- FİLTRELEME SONUCU ---")
print("Kameradan gelen tüm noktalar :", gelen_koordinatlar)
print("Sadece SAĞ taraftaki noktalar:", sagdaki_noktalar)

# ------------------------------------------------------------------------------
# [DUR & KONTROL]
# 1. Kodu çalıştır ve terminal çıktısını sınıfa göster.
# 2. Sınıfa meydan okuma (Mini Challenge):
#    "Peki ekranın SOLUNDAKİ (320'den küçük) noktaları almak isteseydik kodda nereyi değiştirirdik?"
#    Cevap: if nokta < 320
# ------------------------------------------------------------------------------