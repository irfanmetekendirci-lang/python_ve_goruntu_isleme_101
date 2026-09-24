# ==============================================================================
# BÖLÜM 2: Koleksiyonlar (Listeler ve Sözlükler)
# SÜRE: ~25 Dakika
# ==============================================================================

# "Tek bir kutuda tek bir veri saklamayı gördük. Ama görüntü işlemede elimizde binlerce piksel,
# ya da elimizin 21 tane eklem noktası olacak. Bunlar için 21 ayrı değişken açamayız.
# Birden çok veriyi tek bir çekmecede sıralı tutmak için LİSTE (list) kullanırız.
# Köşeli parantez [ ] gördüğümüz her yer bir listedir."

parmak_koordinati = [320, 240]  # [X pikseli, Y pikseli]

# "ÇOK ÖNEMLİ KURAL: Bilgisayar dünyasında saymaya 1'den değil, DAİMA 0'dan başlanır!
# 0. eleman = Listenin 1. elemanıdır.
# Yanına köşeli parantez açıp indeks numarasını yazarak istediğimiz sıradaki elemanı çekeriz."

print("X koordinatı (0. indeks):", parmak_koordinati[0])
print("Y koordinatı (1. indeks):", parmak_koordinati[1])

# [NOKTA (.) MANTIĞI]:
# "Şimdi çok kritik bir soru: Neden araya nokta koyuyoruz? (noktalar.append gibi)
# Günlük hayattan düşünün: Bir araba nesnesinin özellikleri ve yapabildiği eylemler vardır.
# 'araba.calis()', 'araba.fren_yap()'.
# Python'da da her veri tipinin kendine özel süper güçleri (metotları) vardır.
# Bir nesnenin adının yanına NOKTA (.) koymak: 'Ey liste, senin cephaneliğindeki yetenekleri bana aç!' demektir.
# '.append()' listelerin içindeki hazır bir yetenektir. İngilizce 'eklemek' demektir ve listenin sonuna yeni bir eleman yapıştırır."

noktalar = [100, 250, 400]
print("İlk liste hali:", noktalar)

noktalar.append(550) # Noktalar listesinin cephanesinden append yeteneğini çağırdık!
print("Append sonrası liste:", noktalar)

# len() fonksiyonu: "Length" (Uzunluk) kelimesinden gelir. Listenin içinde kaç kutu olduğunu sayar.
print("Listedeki toplam nokta sayısı:", len(noktalar))


# "Sözlükler (dict) ise süslü parantezle { } yazılır.
# Listede sıralar 0, 1, 2 diye giderken, sözlükte her veriye kendi verdiğimiz bir İSİM (anahtar/key) ile ulaşırız.
# Tıpkı Türkçe-İngilizce sözlük gibi: Kelimeye bakıp karşılığını alırsınız."

kamera_ayari = {
    "genislik": 640,
    "yukseklik": 480,
    "fps": 30
}
print("Kameranın genişliği:", kamera_ayari["genislik"])

# ------------------------------------------------------------------------------
# [DUR & ÇALIŞTIR]
# 1. Kodu çalıştır.
# 2. Tahtada parmak_koordinati[0] ve [1] çıktısını göster.
# 3. [ÖĞRENCİYE VURGU]: "Haftaya MediaPipe ile kamerayı açtığımızda elinizin 8. noktası olan
#    işaret parmağınızı çekerken 'landmarks[8]' yazacağız. İşte o köşeli parantez tam olarak bu!"
# ------------------------------------------------------------------------------