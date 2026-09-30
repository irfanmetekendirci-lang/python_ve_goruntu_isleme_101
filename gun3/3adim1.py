# ==============================================================================
# GÜN 3 - ADIM 1: Kamera Akışını Başlatma, Aynalama ve Pencere Yönetimi
# SÜRE: ~20 Dakika
# ==============================================================================

# OpenCV kütüphanesini içe aktarıyoruz:
# Kameradan görüntü okumak, pencere açmak ve tuş kontrolleri için kullanılır.
import cv2

# Bilgisayarın varsayılan dahili kamerasını (0 numaralı indeks) başlatıyoruz.
# Harici bir USB kamera bağlıysa bu indeks 1 veya 2 olabilir.
cap = cv2.VideoCapture(0)

# Sonsuz video döngüsü (Flipbook / Çevirmeli Defter Mantığı):
# Bilgisayar için 'video' diye bir veri tipi yoktur; saniyede 30 kare art arda akan fotoğraflar vardır.
while True:
    # cap.read() kameradan anlık tek bir fotoğraf çeker ve bize 2 değişken döndürür:
    # 1. ret (return): Fotoğraf başarıyla çekildi mi? (True / False döner).
    # 2. frame: Çekilen fotoğrafın kendisidir (piksel matrisi).
    ret, frame = cap.read()

    # Kamera kablosu çıkarsa veya görüntü alınamazsa program çökmesin diye döngüyü kırıyoruz:
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    # Ayna Etkisi (cv2.flip):
    # Standart web kameralarında elinizi sağa götürdüğünüzde ekrandaki görüntü sola gider.
    # Bu durum etkileşimli uygulamalarda kullanımı zorlaştırır.
    # cv2.flip(frame, 1) komutu ile görüntüyü yatay eksende (aynadaki gibi) ters çeviriyoruz.
    # 1: Yatay çevirme, 0: Dikey (baş aşağı) çevirme anlamına gelir.
    frame = cv2.flip(frame, 1)

    # cv2.imshow: Belirtilen isimde bir pencere açar ve anlık kareyi bu pencerede gösterir.
    cv2.imshow("Gun 3 - Adim 1: Kamera Testi", frame)

    # cv2.waitKey(1): İki temel görevi vardır:
    # 1. Ekrana basılan fotoğrafın görünür kalabilmesi için programı 1 milisaniye bekletir.
    # 2. O 1 milisaniye içinde klavyeden basılan tuşu dinler.
    # & 0xFF: İşletim sistemi farklılıklarından kaynaklanan tuş kodu uyumsuzluklarını önler (8-bit maskeleme).
    # ord('q'): 'q' harfinin klavyedeki sayısal ASCII kodunu verir.
    # 'q' tuşuna basıldığında döngüden çıkılır:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Döngü bittiğinde kamerayı işletim sistemine geri iade ediyoruz (kamera ışığı söner):
cap.release()

# OpenCV tarafından açılmış olan tüm pencereleri bellekten temizleyip kapatıyoruz:
cv2.destroyAllWindows()