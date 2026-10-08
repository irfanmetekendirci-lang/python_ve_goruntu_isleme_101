# YAZGİT Python & Görüntü İşleme 101 🚀

Bu repo, **Ankara Üniversitesi YAZGİT** bünyesinde düzenlenen 2 haftalık (4 ders) temel Python ve OpenCV / MediaPipe ile görüntü işleme eğitiminin kaynak kodlarını, ders içi pratiklerini ve bitirme projesini içerir.

> **Vizyonumuz:** Yazılımcılık artık her fonksiyonu ezbere yazmak değil; sistemin mantığını, veri akışını ve neyi nerede arayacağını bilmektir. Kodu yapay zekâ da üretir, dokümantasyonda da bulursunuz. Bu eğitimin asıl amacı; kameradan gelen ham verinin koda nasıl girdiğini, koordinatların nasıl okunduğunu ve bu verilerle neler üretilebileceğini uygulamalı olarak kavramaktır.

---

## 📅 Müfredat ve Ders Planı

### Hafta 1: Python Mantığı ve Veriyi Anlama

* **1. Gün - Temel Python ve Algoritmik Düşünce (90 Dakika)**
  * Programlama mantığı, veri tipleri (`int`, `float`, `str`, `bool`)
  * Koleksiyonlar: Listeler (`[]`) ve Sözlükler (`{}`)
  * Karar yapıları (`if` / `elif` / `else`) ve `for` döngüleri
  * **Ders Sonu Pratiği:** Mini koordinat filtreleme algoritması

* **2. Gün - Fonksiyonlar ve Veri Kütüphanelerine Bakış (90 Dakika)**
  * Fonksiyon tanımlama (`def`), parametreler ve `return` mantığı
  * Görüntü işlemenin temeli: NumPy nedir, matris/piksel temsili
  * Veri analizinin aracı: Pandas DataFrame yapısına kavramsal bakış
  * Ortam kurulumları (`pip install ...`) ve OpenCV ile ilk canlı kamera testi

---

### Hafta 2: OpenCV & MediaPipe ile Bilgisayarlı Görü

* **3. Gün - OpenCV & Canlı El Tespiti (90 Dakika)**
  * `cv2.VideoCapture` ile canlı kamera akışı yakalama ve pencere yönetimi
  * BGR - RGB renk dönüşümleri ve MediaPipe Hands modelinin çağrılması
  * Elin 21 eklem noktasını (landmarks) canlı görüntü üzerinde tespit etme ve çizdirme

* **4. Gün - Jest Algılama ve Akıllı Parmak Sayıcı (90 Dakika)**
  * Ekran koordinat sistemi mantığı: $Y$ değeri aşağı indikçe büyür, tepeye çıktıkça küçülür kuralı ile parmak açık/kapalı kontrolü (lm[8].y < lm[6].y)
  * Listeler ([8, 12, 16, 20]) ve for döngüsü yardımıyla açık parmakları sayma algoritması
  * Başparmak kontrolü (X ekseni yatay hareket analizi) ile 5 parmağın tamamını sayma
  * cv2.rectangle ile sol üst köşeye gösterge paneli ekleme ve basit jest algılama (Yumruk / Açık El)
  * Bağımsız VisionDraw projesinin incelenmesi ve portföye eklenme rehberi
---

## 🎨 Bitirme Projesi: VisionDraw (Havada Çizim)

Eğitimin nihai hedefi olarak geliştirilen **VisionDraw**, bilgisayar kamerası ve yapay zekâ destekli el takibi kullanarak havada çizim yapmanızı sağlayan interaktif bir bilgisayarlı görü uygulamasıdır.

* **Çizim Modu:** Yalnızca işaret parmağı havadayken dijital tuval üzerine serbest çizim yapar.
* **Gezinme Modu:** Hem işaret hem orta parmak havadayken çizimi durdurur ve fırça konumunu taşır.
* **Kısayollar:**
  * `C` — Tuvali temizleme
  * `Q` — Güvenli çıkış

> Projenin tüm kodlarına, detaylı kurulum adımlarına ve kullanım kılavuzuna [`VisionDraw/`](./VisionDraw/) klasöründen ulaşabilirsiniz.

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için **Python 3.8+** ve **VS Code** önerilir.

### 1. Repoyu Klonlayın
    git clone [https://github.com/irfanmetekendirci-lang/python_ve_goruntu_isleme_101.git](https://github.com/irfanmetekendirci-lang/python_ve_goruntu_isleme_101.git)
    cd python_ve_goruntu_isleme_101

### 2. Gerekli Kütüphaneleri Yükleyin
    pip install opencv-python mediapipe numpy

### 3. Örnek Kodları Çalıştırın

* **1. Gün Pratik Kodu:**
    python hafta1/ders1/bolum4_ders_sonu_pratigi.py

* **2. Gün Kamera Test Kodu:**
    python hafta1/ders2/bolum4_kurulum_ve_test.py

* **VisionDraw Bitirme Projesi:**
    python VisionDraw/vision_draw.py

---

## 📂 Dizin Yapısı

* python_ve_goruntu_isleme_101/
  * README.md
  * LICENSE
  * MediaPipe-Hands-21-landmarks.jpg
  * gun1/
    * adim1.py
    * adim2.py
    * adim3.py
    * adim4.py
  * gun2/
    * 2adim1.py
    * 2adim2.py
    * 2adim3.py
    * 2adim4.py
  * gun3/
    * 3adim1.py
    * 3adim2.py
    * 3adim3.py
  * gun4/
    * 4adim1.py
    * 4adim2.py
    * 4adim3.py
  * VisionDraw/
    * VisionDraw.py
    * requirements.txt
    * README.md
    * index.html

---

## 🤝 Katkı ve İletişim

Bu eğitim materyalleri **Ankara Üniversitesi YAZGİT (Yapay Zeka ve Görüntü İşleme Topluluğu)** bünyesinde öğrenciler için hazırlanmıştır. Sorularınız, hata bildirimleri veya geliştirmeler için Issue açabilir veya topluluk kanallarından iletişime geçebilirsiniz.