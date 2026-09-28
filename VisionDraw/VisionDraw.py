# ==============================================================================
# PROJE: VisionDraw - Havada Çizim Uygulaması
# DOSYA: vision_draw.py
# ==============================================================================

# Gerekli 3 temel kütüphaneyi içe aktarıyoruz:
# 1. cv2: Kamera görüntüsü, çizimler ve pencere yönetimi için (OpenCV)
# 2. mediapipe: El tespiti ve parmak ucu koordinatları için (koordinatları bizim yerimize hesaplar)
# 3. numpy: Üzerine çizim yapacağımız boş dijital tuvali bir matris olarak oluşturmak için
import cv2
import mediapipe as mp
import numpy as np

# ------------------------------------------------------------------------------
# ADIM 1: MediaPipe El Takibi Modelini Başlatma
# ------------------------------------------------------------------------------
# MediaPipe'ın el modülünü ve ekrandaki çizim yardımcısını tanımlıyoruz:
mp_hands = mp.solutions.hands           # MediaPipe'ın el araçları kutusunu tutan bir değişken.
mp_draw = mp.solutions.drawing_utils    # Ekrana çizim yapacak yardımcı aracı tutan değişken.

# max_num_hands=1: Ekranda sadece tek bir ele odaklansın
# min_detection_confidence=0.7: %70 emin olmadan 'el buldum' demesin
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)   # Çalışmaya hazır el takip modelimizi tutan değişken (nesne).


# ------------------------------------------------------------------------------
# ADIM 2: Kamerayı Açma ve Değişkenleri Hazırlama
# ------------------------------------------------------------------------------
# Bilgisayarın varsayılan kamerasını (0) başlatıyoruz:
cap = cv2.VideoCapture(0)       # cap, capture (yakalamak)'dan geliyor

# Çizim tuvali (başlangıçta boş; kameranın ilk karesi gelince boyutlandırılacak)
canvas = None

# Çizgiyi kesintisiz çekebilmek için bir önceki karenin (X, Y) koordinatları (previous / önceki)
prev_x, prev_y = 0, 0

# Çizim rengi: OpenCV renkleri BGR formatında tutar -> (Mavi, Yeşil, Kırmızı)
# (0, 0, 255) = Kırmızı
draw_color = (0, 0, 255) # İleride çeşitlendirilebilir


# ------------------------------------------------------------------------------
# ADIM 3: Sonsuz Video Döngüsü
# ------------------------------------------------------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    # Ayna etkisi: Kullanıcı elini sağa götürdüğünde ekranda da sağa gitsin
    frame = cv2.flip(frame, 1)

    # Ekranın yükseklik (h) ve genişlik (w) piksel değerlerini alıyoruz:
    h, w, c = frame.shape

    # İlk karede tam ekran boyutunda simsiyah boş bir dijital tuval açıyoruz:
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    # OpenCV (BGR) formatını MediaPipe'ın anladığı (RGB) formatına çeviriyoruz:
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)


    # --------------------------------------------------------------------------
    # ADIM 4: El Koordinatlarını (Landmarks) İnceleme
    # --------------------------------------------------------------------------
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # 8: İşaret parmağı ucu, 6: İşaret parmağı orta eklemi
            # 12: Orta parmak ucu,  10: Orta parmak orta eklemi
            # Oransal gelen değerleri (0.0 - 1.0) piksel koordinatına çeviriyoruz:
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            mx, my = int(lm[12].x * w), int(lm[12].y * h)

            # Bilgisayar ekranında Y koordinatı aşağıya doğru artar.
            # Uç noktanın Y değeri orta eklemden küçükse parmak havaya kalkmıştır:
            index_open = lm[8].y < lm[6].y
            middle_open = lm[12].y < lm[10].y


            # ------------------------------------------------------------------
            # ADIM 5: Çizim Modu / Gezinme Modu Kontrolü
            # ------------------------------------------------------------------
            # DURUM 1: Sadece işaret parmağı açıksa -> ÇİZİM YAP
            if index_open and not middle_open:
                # Parmağın ucunu belirtmek için küçük bir kılavuz nokta çiz:
                cv2.circle(frame, (ix, iy), 8, draw_color, cv2.FILLED)

                # Kalem ilk defa ekrana değiyorsa başlangıç noktasını sabitle:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = ix, iy

                # Önceki koordinat ile şimdiki koordinat arasına tuvalde çizgi çek:
                cv2.line(canvas, (prev_x, prev_y), (ix, iy), draw_color, 5)

                # Şimdiki noktayı bir sonraki kare için 'eski nokta' yap:
                prev_x, prev_y = ix, iy

            # DURUM 2: Hem işaret hem orta parmak açıksa -> GEZİNME (ÇİZİMİ DURDUR)
            elif index_open and middle_open:
                # Kalemi kâğıttan kaldır:
                prev_x, prev_y = 0, 0
                # Gezinme modunda olduğunu göstermek için parmağa mavi halka koy:
                cv2.circle(frame, (ix, iy), 12, (255, 0, 0), 2)

            else:
                prev_x, prev_y = 0, 0

            # Elin 21 eklem noktasını ve bağlantılarını kamera görüntüsüne çiz:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        # Ekranda hiç el yoksa kalemi sıfırla:
        prev_x, prev_y = 0, 0


    # --------------------------------------------------------------------------
    # ADIM 6: Tuval ile Kamerayı Birleştirme ve Ekrana Basma
    # --------------------------------------------------------------------------
    # %100 kamera karesi ile %70 tuvali üst üste yapıştır:
    combined_frame = cv2.addWeighted(frame, 1.0, canvas, 0.7, 0)

    # Kısayol bilgilendirme metni:
    cv2.putText(combined_frame, "Temizle: C | Cikis: Q", (15, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Nihai görüntüyü ekranda göster:
    cv2.imshow("VisionDraw", combined_frame)


    # --------------------------------------------------------------------------
    # ADIM 7: Tuş Kontrolleri
    # --------------------------------------------------------------------------
    key = cv2.waitKey(1) & 0xFF

    # 'q' tuşuna basılırsa döngüden çık:
    if key == ord('q'):
        break

    # 'c' tuşuna basılırsa tuvali yeniden siyah yaparak çizimleri sil:
    elif key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

# Kaynakları serbest bırak ve pencereleri kapat:
cap.release()
cv2.destroyAllWindows()