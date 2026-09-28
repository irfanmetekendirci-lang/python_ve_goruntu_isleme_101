# ==============================================================================
# BÖLÜM 3: Pandas Nedir? (Kavramsal Bakış ve Canlı Gösterim)
# SÜRE: ~15 Dakika
# ==============================================================================

# "Veri dünyasında NumPy'ın kardeşi Pandas'tır.
# Kodlamaya boğulmadan tek bir benzetmeyle aklımızda tutalım:
# 'Pandas, Python'ın Excel'idir!'
# Eğer elinizde satırları ve sütunları olan bir Excel tablosu, CSV dosyası veya kullanıcı veritabanı varsa,
# bunu işlemek, filtrelemek ve analiz etmek için Pandas kullanılır.
# Örneğin yapay zekaya el hareketlerini öğretmek için binlerce parmak koordinatını bir Excel tablosuna
# kaydetmek istersek Pandas devreye girer."

# [NOT]: Öğrencilerin bilgisayarında pandas yüklü olmayabilir, 
# kendi bilgisayarından projeksiyona yansıtıp çıktıyı göster:

import pandas as pd

ornek_veri = {
    "Parmak": ["Başparmak", "İşaret", "Orta", "Yüzük", "Serçe"],
    "X_Piksel": [120, 320, 340, 310, 280],
    "Y_Piksel": [250, 150, 130, 145, 190]
}

print("Ham Veri Sözlüğü:")
print(ornek_veri)

# "Şimdi projeksiyona bakın: Bu sözlüğü Pandas'ın DataFrame yeteneğine verdiğimde ne oluyor:"
tablo = pd.DataFrame(ornek_veri)
print("\n--- PANDAS DATAFRAME (EXCEL TABLOSU) ÇIKTISI ---")
print(tablo)

# "Gördüğünüz gibi indeksleri, sütunları olan tertemiz bir tablo yaptı.
# Biz canlı piksellerle anlık çalışacağımız için bu eğitimde ağırlıklı olarak NumPy ve OpenCV kullanacağız."