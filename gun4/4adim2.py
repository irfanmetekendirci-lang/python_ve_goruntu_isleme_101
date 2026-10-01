# ==============================================================================
# GÜN 4 - ADIM 2: Çoklu Parmak Sayma (Döngü ve Liste Kullanımı)
# SÜRE: ~35 Dakika
# ==============================================================================

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# MediaPipe'ta 4 ana parmağın uç noktaları (Landmark ID):
# 8: İşaret Parmağı Ucu
# 12: Orta Parmak Ucu
# 16: Yüzük Parmağı Ucu
# 20: Serçe Parmak Ucu
parmak_uclari = [8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Her karede açık parmakları saymak için sayacımızı sıfırlıyoruz:
            acik_parmak_sayisi = 0

            # 1. Gün öğrendiğimiz FOR DÖNGÜSÜ ile parmak uçlarını tek tek geziyoruz:
            for uc_id in parmak_uclari:
                # Uç noktanın 2 altındaki eklem o parmağın orta boğumudur (Örn: 8 için 6, 12 için 10)
                alt_eklem_id = uc_id - 2

                # Parmak ucu alt eklemden yukarıdaysa (Y değeri daha küçükse) parmak açıktır:
                if lm[uc_id].y < lm[alt_eklem_id].y:
                    acik_parmak_sayisi += 1

            # 4 parmağın toplam sonucunu ekrana yazdırıyoruz:
            cv2.putText(frame, f"Acik Parmak: {acik_parmak_sayisi}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 4 - Adim 2: Parmak Sayar", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()