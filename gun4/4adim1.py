# ==============================================================================
# GÜN 4 - ADIM 1: Parmak Açık mı Kapalı mı Mantığı (Y Ekseni Karşılaştırması)
# SÜRE: ~25 Dakika
# ==============================================================================

# Gerekli 2 kütüphaneyi içe aktarıyoruz:
# OpenCV kamera görüntüsü için, MediaPipe ise el eklemlerini bulmak için kullanılır.
import cv2
import mediapipe as mp

# MediaPipe el takip modelini başlatıyoruz:
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    # Kullanıcıyla ayna gibi eşleşmesi için görüntüyü yatayda çeviriyoruz:
    frame = cv2.flip(frame, 1)

    # OpenCV (BGR) formatını MediaPipe'ın anladığı RGB formatına çeviriyoruz:
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Ekranda el tespit edildiyse:
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # 8 NUMARA: İşaret parmağının EN UÇ noktası
            # 6 NUMARA: İşaret parmağının İKİNCİ BOĞUMU (orta eklemi)
            #
            # EKRAN KOORDİNAT SİSTEMİ MANTIĞI:
            # Bilgisayar ekranında en üst kenar Y = 0 noktasıdır; aşağı indikçe Y değeri BÜYÜR.
            # Dolayısıyla parmağımızı yukarı kaldırdığımızda ucu (8), ekleminden (6) daha yukarıda durur.
            # Ekranda daha yukarıda olmak demek, Y değerinin daha KÜÇÜK olması demektir!
            isaret_parmagi_acik_mi = lm[8].y < lm[6].y

            # Koşula göre ekranda durumu gösterelim:
            if isaret_parmagi_acik_mi:
                durum = "ISARET PARMAGI: ACIK"
                renk = (0, 255, 0)  # Yeşil (BGR)
            else:
                durum = "ISARET PARMAGI: KAPALI"
                renk = (0, 0, 255)  # Kırmızı (BGR)

            cv2.putText(frame, durum, (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, renk, 2)

            # El eklemlerini ekranda göster:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 4 - Adim 1: Tek Parmak Kontrolu", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()