# ==============================================================================
# GÜN 4 - ADIM 3: Taş-Kağıt-Makas Jest Tanıma
# SÜRE: ~30 Dakika
# ==============================================================================

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

kamera = cv2.VideoCapture(0)

# Sadece dikey eksende (Y) sorunsuz çalışan 4 parmağın uç indeksleri:
# 8: İşaret, 12: Orta, 16: Yüzük, 20: Serçe
# NOT: Başparmak yatayda açılıp kapandığı ve sağ/sol elde yönü değiştiği için
# hesaba katmıyoruz. Taş-Kağıt-Makas için 4 parmak yeterli!
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

            # 1. PARMAK KONTROLÜ (Y Ekseni):
            # Uç noktası, iki alttaki eklemden daha yukarıdaysa parmak açıktır.
            for uc_id in parmak_uclari:
                alt_eklem = uc_id - 2
                if lm[uc_id].y < lm[alt_eklem].y:
                    acik_parmak_sayisi += 1

            # 2. JEST KARAR MEKANİZMASI:
            jest = "TANIMSIZ"
            renk = (200, 200, 200)  # Gri

            if acik_parmak_sayisi == 0:
                jest = "TAS (Yumruk)"
                renk = (0, 0, 255)  # Kırmızı
            elif acik_parmak_sayisi == 2 and lm[8].y < lm[6].y and lm[12].y < lm[10].y:
                # Sadece işaret ve orta parmak açıksa
                jest = "MAKAS"
                renk = (255, 165, 0)  # Turuncu
            elif acik_parmak_sayisi == 4:
                jest = "KAGIT"
                renk = (0, 255, 0)  # Yeşil

            # Sol üst köşeye bilgi kutusu çiziyoruz (Piksel boyama):
            # cv2.rectangle(hedef, sol_ust_kose, sag_alt_kose, renk, kalinlik)
            cv2.rectangle(kare, (10, 10), (320, 100), (0, 0, 0), cv2.FILLED)

            cv2.putText(kare, f"Acik: {acik_parmak_sayisi} Parmak", (20, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(kare, f"JEST: {jest}", (20, 85),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, renk, 2)

            mp_draw.draw_landmarks(kare, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 4 - Adim 3: Tas-Kagit-Makas", kare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
print("Kamera kapatildi.")
