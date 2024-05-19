# Ransomware
# Dosyaları Şifreleme ve Şifreyi Çözme

Bu Python kodu, dosyaları şifrelemek ve şifreyi çözmek için kullanılır. İşlemler şu şekilde gerçekleştirilir:

## Dosyaları Şifreleme
1. Bir anahtar oluşturulur.
2. Oluşturulan anahtar "Ransom_key.txt" adlı bir dosyaya yazılır.
3. Her dosyanın içeriği okunur, şifrelenir ve tekrar yazılır.

## Dosyaları Şifre Çözme
1. Önceden oluşturulmuş anahtar "Ransom_key.txt" dosyasından okunur.
2. Her şifreli dosyanın içeriği okunur, şifre çözülür ve tekrar yazılır.

Bu işlemler "ransom.py" ve "decrypt.py" dosyaları dışında kalan tüm dosyaları etkiler.

