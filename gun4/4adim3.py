# ==============================================================================
# GÜN 4 - ADIM 3: Başparmak Dahil Tam Parmak Sayacı ve Kapanış Jesti
# SÜRE: ~30 Dakika
# ==============================================================================

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

kamera = cv2.VideoCapture(0)

# Dört parmağın uç indeksleri:
parmak_uclari = [8, 12, 16, 20]

while True:
    basarili, kare = kamera.read()
    if not basarili:
        print("Kamera görüntüsü alınamadı!")
        break

    kare = cv2.flip(kare, 1)
    rgb_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_kare)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark
            acik_parmak_sayisi = 0

            # 1. BAŞPARMAK KONTROLÜ (4 Numara):
            # Başparmak yukarı-aşağı değil, YATAYDA (X ekseninde) açılıp kapanır.
            # Uç noktası (4), boğum noktasından (3) daha dışarıdaysa açıktır:
            if lm[4].x > lm[3].x:
                acik_parmak_sayisi += 1

            # 2. DİĞER 4 PARMAK KONTROLÜ (Y Ekseni):
            for uc_id in parmak_uclari:
                if lm[uc_id].y < lm[uc_id - 2].y:
                    acik_parmak_sayisi += 1

            # Sol üst köşeye şık bir bilgi kutusu çiziyoruz (Piksel boyama):
            # cv2.rectangle(hedef, sol_ust_kose, sag_alt_kose, renk, kalinlik)
            cv2.rectangle(kare, (10, 10), (220, 110), (0, 0, 0), cv2.FILLED)

            # Ekrana büyük punto ile parmak sayısını basıyoruz:
            cv2.putText(kare, str(acik_parmak_sayisi), (85, 85),
                        cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 5)

            # Basit Jest Tanıma (Örnek Karar Mekanizması):
            if acik_parmak_sayisi == 0:
                cv2.putText(kare, "JEST: YUMRUK", (10, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            elif acik_parmak_sayisi == 5:
                cv2.putText(kare, "JEST: ACIK EL", (10, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            mp_draw.draw_landmarks(kare, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 4 - Adim 3: Akilli Parmak Sayaci", kare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()