# YAZGİT Python & Görüntü İşleme 101 🚀

Bu repo, **Ankara Üniversitesi YAZGİT** bünyesinde düzenlenen 2 haftalık (4 ders) temel Python ve OpenCV / MediaPipe ile görüntü işleme eğitiminin kaynak kodlarını, ders içi pratiklerini ve bitirme projesini içerir.

> **Vizyonumuz:** Yazılımcılık artık her fonksiyonu ezbere yazmak değil; sistemin mantığını, veri akışını ve neyi nerede arayacağını bilmektir. Kodu yapay zekâ da üretir, dokümantasyonda da bulursunuz. Bu eğitimin asıl amacı; kameradan gelen ham verinin koda nasıl girdiğini, koordinatların nasıl okunduğunu ve bu verilerle neler üretilebileceğini uygulamalı olarak kavramaktır.

Her gün kendi klasöründe (`gun1/` … `gun4/`) adım adım ilerleyen dosyalardan oluşur. Dosyaların içindeki yorum satırları ders anlatımının kendisidir; her dosyanın sonunda **[DUR & ÇALIŞTIR]** / **[DUR & KONTROL]** bölümleri ve olası hatalar yer alır.

---

## 📅 Müfredat ve Ders Planı

### Hafta 1: Python Mantığı ve Veriyi Anlama

#### 1. Gün - Temel Python ve Algoritmik Düşünce (`gun1/`)

| Dosya | Konu | Süre |
|---|---|---|
| [`adim1.py`](./gun1/adim1.py) | `print()`, değişkenler ve veri tipleri (`int`, `float`, `str`, `bool`) | ~20 dk |
| [`adim2.py`](./gun1/adim2.py) | Listeler (`[]`), indeksleme, iç içe listeler, `.append()`, `len()` ve sözlükler (`{}`) | ~25 dk |
| [`adim3.py`](./gun1/adim3.py) | Karar yapıları (`if` / `elif` / `else`), `for` ve `while` döngüleri | ~25 dk |
| [`adim4.py`](./gun1/adim4.py) | **Ders sonu pratiği:** Mini koordinat filtresi (ekranın sağ yarısındaki noktaları ayıklama) | ~15-20 dk |

#### 2. Gün - Fonksiyonlar ve Veri Kütüphanelerine Bakış (`gun2/`)

| Dosya | Konu | Süre |
|---|---|---|
| [`2adim1.py`](./gun2/2adim1.py) | Fonksiyonlar (`def`), parametreler, `print` vs `return` farkı, `piksele_cevir()` örneği | ~25 dk |
| [`2adim2.py`](./gun2/2adim2.py) | NumPy nedir? Görüntünün matris olarak temsili (`np.zeros`, `.shape`) | ~20 dk |
| [`2adim3.py`](./gun2/2adim3.py) | Pandas'a kavramsal bakış: sözlükten `DataFrame` oluşturma | ~15 dk |
| [`2adim4.py`](./gun2/2adim4.py) | Kütüphane kurulumları, sürüm kontrolü ve OpenCV ile ilk canlı kamera testi | ~25 dk |

---

### Hafta 2: OpenCV & MediaPipe ile Bilgisayarlı Görü

#### 3. Gün - OpenCV & Canlı El Tespiti (`gun3/`)

| Dosya | Konu | Süre |
|---|---|---|
| [`3adim1.py`](./gun3/3adim1.py) | `cv2.VideoCapture` ile kamera akışı, `cv2.flip` ile ayna etkisi, `imshow` / `waitKey` ile pencere yönetimi | ~20 dk |
| [`3adim2.py`](./gun3/3adim2.py) | BGR → RGB dönüşümü, MediaPipe Hands modelini başlatma ve 21 eklem noktasını çizdirme | ~30 dk |
| [`3adim3.py`](./gun3/3adim3.py) | Normalize koordinatları piksele çevirme (`kare.shape`), işaret parmağı takibi (`cv2.circle`, `cv2.putText`) | ~20 dk |

#### 4. Gün - Jest Algılama ve Akıllı Parmak Sayacı (`gun4/`)

| Dosya | Konu | Süre |
|---|---|---|
| [`4adim1.py`](./gun4/4adim1.py) | Ekran koordinat sistemi: Y aşağı indikçe büyür → parmak açık/kapalı kontrolü (`lm[8].y < lm[6].y`) | ~25 dk |
| [`4adim2.py`](./gun4/4adim2.py) | Parmak uçları listesi (`[8, 12, 16, 20]`) ve `for` döngüsüyle açık parmakları sayma | ~35 dk |
| [`4adim3.py`](./gun4/4adim3.py) | Başparmak kontrolü (X ekseni) ile 5 parmak sayımı, `cv2.rectangle` ile gösterge paneli ve basit jest tanıma (Yumruk / Açık El) | ~30 dk |

Günün sonunda bağımsız **VisionDraw** projesi incelenir ve portföye ekleme rehberi paylaşılır.

> 💡 El eklem numaralarını (0-20) takip etmek için [`MediaPipe-Hands-21-landmarks.jpg`](./MediaPipe-Hands-21-landmarks.jpg) görselini kullanabilirsiniz.

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

```bash
git clone https://github.com/irfanmetekendirci-lang/python_ve_goruntu_isleme_101.git
cd python_ve_goruntu_isleme_101
```

### 2. Gerekli Kütüphaneleri Yükleyin

```bash
pip install opencv-python mediapipe numpy
```

> 1. gün dosyaları hiçbir kütüphane gerektirmez. [`gun2/2adim3.py`](./gun2/2adim3.py) dosyası için ayrıca `pip install pandas` gerekir (derste kavramsal olarak gösterilir).
>
> VisionDraw'ın sürüm gereksinimleri için: `pip install -r VisionDraw/requirements.txt`

### 3. Örnek Kodları Çalıştırın

Dosyalar repo kök dizininden çalıştırılabilir. Kamera açan dosyalarda pencereyi kapatmak için **`q`** tuşuna basın.

```bash
# 1. Gün - Ders sonu pratiği
python gun1/adim4.py

# 2. Gün - Kurulum kontrolü ve ilk kamera testi
python gun2/2adim4.py

# 3. Gün - İşaret parmağı takibi
python gun3/3adim3.py

# 4. Gün - Akıllı parmak sayacı
python gun4/4adim3.py

# VisionDraw bitirme projesi
python VisionDraw/VisionDraw.py
```

---

## 📂 Dizin Yapısı

```
python_ve_goruntu_isleme_101/
├── README.md
├── LICENSE
├── MediaPipe-Hands-21-landmarks.jpg   # El eklem noktaları referans görseli
├── Bellek_ornegi.jpg                  # Ders görseli
├── gun1/                              # Temel Python
│   ├── adim1.py
│   ├── adim2.py
│   ├── adim3.py
│   └── adim4.py
├── gun2/                              # Fonksiyonlar, NumPy, Pandas, kurulum
│   ├── 2adim1.py
│   ├── 2adim2.py
│   ├── 2adim3.py
│   └── 2adim4.py
├── gun3/                              # OpenCV & MediaPipe el tespiti
│   ├── 3adim1.py
│   ├── 3adim2.py
│   └── 3adim3.py
├── gun4/                              # Parmak sayma ve jest algılama
│   ├── 4adim1.py
│   ├── 4adim2.py
│   └── 4adim3.py
└── VisionDraw/                        # Bitirme projesi
    ├── VisionDraw.py
    ├── requirements.txt
    ├── README.md
    └── index.html
```

---

## 🤝 Katkı ve İletişim

Bu eğitim materyalleri **Ankara Üniversitesi YAZGİT (Yapay Zeka ve Görüntü İşleme Topluluğu)** bünyesinde öğrenciler için hazırlanmıştır. Sorularınız, hata bildirimleri veya geliştirmeler için Issue açabilir veya topluluk kanallarından iletişime geçebilirsiniz.
