# ==============================================================================
# GÜN 3 - ADIM 2: MediaPipe Hands Modelini Başlatma ve Canlı El Tespiti
# SÜRE: ~30 Dakika
# ==============================================================================

import cv2
import mediapipe as mp

# MediaPipe el modülünü ve çizim aracını tanımlıyoruz:
# mp_hands: MediaPipe'ın el takip araç kutusunu tutar.
# mp_draw: Tespit edilen eklemleri ekranda birbirine bağlamak için kullanılan hazır fırça aracıdır.
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Hazır eğitilmiş yapay zeka modelini başlatıyoruz:
# max_num_hands=1: Ekranda birden fazla el olsa bile sadece 1 tanesine odaklanmasını sağlar.
# min_detection_confidence=0.7: Model ekranda gördüğü nesnenin %70 oranında bir el olduğuna emin olmadan koordinat üretmez.
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

kamera = cv2.VideoCapture(0)

while True:
    basarili, kare = kamera.read()
    if not basarili:
        print("Kamera görüntüsü alınamadı!")
        break

    # Ayna etkisi:
    kare = cv2.flip(kare, 1)

    # Renk Uzayı Dönüşümü (BGR -> RGB):
    # OpenCV kameralardan gelen görüntüyü BGR (Mavi, Yeşil, Kırmızı) renk formatında tutar.
    # Ancak MediaPipe yapay zeka modeli internetteki standart RGB (Kırmızı, Yeşil, Mavi) fotoğraflarla eğitilmiştir.
    # Modelin renkleri doğru anlayabilmesi için formatı RGB'ye çeviriyoruz:
    rgb_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2RGB)

    # Yapay zekaya görüntüyü gönderip eli taratıyoruz:
    # results değişkeni modelin analiz raporunu tutar.
    results = hands.process(rgb_kare)

    # results.multi_hand_landmarks: Ekranda el tespit edildiyse içi dolar, el yoksa 'None' (boş) olur.
    # Bu kontrolü yapmazsak el ekranda yokken koordinat çekmeye çalışmak programı çökertir:
    if results.multi_hand_landmarks:
        # Tespit edilen elin eklem verilerine liste mantığıyla erişiyoruz:
        for hand_landmarks in results.multi_hand_landmarks:
            # mp_draw.draw_landmarks:
            # 1. Parametre (kare): Çizimin yapılacağı ana kamera görüntüsü.
            # 2. Parametre (hand_landmarks): Modelin bulduğu 21 eklem noktasının koordinatları.
            # 3. Parametre (mp_hands.HAND_CONNECTIONS): Eklemleri birbirine bağlayan iskelet çizgileri.
            mp_draw.draw_landmarks(kare, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gun 3 - Adim 2: Canli El Tespiti", kare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()