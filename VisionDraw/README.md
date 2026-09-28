# VisionDraw 🎨🖐️

VisionDraw, web kamerası karşısında el hareketlerini kullanarak havada çizim yapmanızı sağlayan basit ve eğitici bir görüntü işleme uygulamasıdır. 

Bu proje; **Python**, **OpenCV** ve **MediaPipe** kütüphaneleri kullanılarak geliştirilmiştir.

---

## 🚀 Kurulum

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla terminal veya komut satırında (CMD) uygulayın:

### 1. Gerekli Kütüphaneleri Yükleyin
Proje klasörünün içindeyken şu komutu çalıştırın:

```bash
pip install -r requirements.txt
```

*(Alternatif olarak tek tek yüklemek isterseniz:)*
```bash
pip install opencv-python mediapipe numpy
```

---

## 💻 Çalıştırma

Kurulum tamamlandıktan sonra uygulamayı başlatmak için:

```bash
python vision_draw.py
```

---

## 🕹️ Nasıl Kullanılır? (Kontroller ve Kısayollar)

Uygulama temel olarak işaret ve orta parmağınızın pozisyonuna göre çalışır:

| Hareket / Tuş | Mod | Açıklama |
|---|---|---|
| **Sadece İşaret Parmağı Açık** | **Çizim Modu** | Parmağınızın ucundan kırmızı bir çizgi çizilir. |
| **İşaret + Orta Parmak Açık** | **Gezinme Modu** | Kalem havaya kalkar; çizim yapmadan ekranda gezinebilirsiniz. |
| **C Tuşu** | **Temizle** | Dijital tuvaldeki tüm çizimleri siler ve ekranı sıfırlar. |
| **Q Tuşu** | **Çıkış** | Kamerayı kapatır ve uygulamayı sonlandırır. |

---

## 🧠 Nasıl Çalışır? (Teknik Mantık)

1. **Kamera Akışı:** `OpenCV` ile kameradan anlık kareler okunur ve ayna etkisi oluşturmak için yatayda ters çevrilir (`flip`).
2. **Yapay Zeka Tespiti:** `MediaPipe Hands` modeli el üzerindeki 21 eklem noktasını (landmark) tespit eder.
3. **Piksel Dönüşümü:** 0.0 ile 1.0 aralığında gelen normalize koordinatlar, ekran genişliği ve yüksekliği ile çarpılarak gerçek piksel konumlarına çevrilir.
4. **Parmak Durum Kontrolü:** Parmak uçlarının Y koordinatı orta eklemlerden daha küçük (ekranda daha yukarıda) olduğunda parmağın açık olduğu anlaşılır.
5. **Asetat Tuvali:** Çizimler kamera karesi üzerine değil, arka plandaki boş bir dijital tuvale (`canvas`) kaydedilir ve iki görüntü `cv2.addWeighted` ile üst üste bindirilir.