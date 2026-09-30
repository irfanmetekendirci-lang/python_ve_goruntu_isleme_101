# ==============================================================================
# GÜN 3 - ADIM 3: Koordinatları Piksele Çevirme ve İşaret Parmağı Takibi
# SÜRE: ~20 Dakika
# ==============================================================================

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    frame = cv2.flip(frame, 1)

    # frame.shape komutu görüntünün boyutlarını verir: [Yükseklik, Genişlik, Renk Kanalı Sayısı]
    # h (Height): Kameranın yükseklik pikseli (Örn: 480)
    # w (Width): Kameranın genişlik pikseli (Örn: 640)
    h, w, c = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # MediaPipe ele 0'dan 20'ye kadar tam 21 raptiye (landmark) batırır.
            # lm: Bu 21 noktanın tamamını içeren listedir:
            lm = hand_landmarks.landmark

            # 8 NUMARALI NOKTA: İşaret parmağının en uç noktasıdır.
            # MediaPipe koordinatları piksel olarak değil, 0.0 ile 1.0 arasında oran olarak verir (Normalize değer).
            # Örneğin ekranın ortasındaysa lm[8].x = 0.5 gelir.
            # Bu oranı gerçek ekrandaki piksel konumuna çevirmek için ekran genişliği (w) ve yüksekliği (h) ile çarparız.
            # Ekranda buçuklu piksel (örn: 320.45) olamayacağı için int() ile tam sayıya yuvarlarız:
            ix = int(lm[8].x * w)
            iy = int(lm[8].y * h)

            # cv2.circle ile işaret parmağının tam ucuna kırmızı bir takip noktası çiziyoruz:
            # Parametreler: (Hedef Görüntü, (X, Y) Merkezi, Yarıçap, Renk (BGR), Kalınlık)
            # (0, 0, 255): BGR formatında Kırmızı renktir.
            # cv2.FILLED: Dairenin içinin tamamen boyanmasını sağlar.
            # (DİKKAT: Henüz kalıcı çizgi çekmiyoruz; sadece parmağın ucunu ekranda canlı işaretliyoruz)
            cv2.circle(frame, (ix, iy), 10, (0, 0, 255), cv2.FILLED)

            # Koordinatları ekranda anlık metin olarak gösterme:
            # cv2.putText(Hedef Görüntü, Metin, Sol Alt Köşe (X, Y), Yazı Tipi, Ölçek, Renk, Kalınlık)
            cv2.putText(frame, f"Isaret Parmagi: X={ix} Y={iy}", (15, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # El iskeletini ve diğer tüm eklem bağlantılarını da göstermeye devam ediyoruz:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 3 - Adim 3: Parmak Takibi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()