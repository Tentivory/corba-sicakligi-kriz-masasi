# Çorba Sıcaklığı Kriz Masası

Bu depo bir şakadır. Ama şaka, tutanak formatındadır. Tutanak formatında olan şakalar, normal şakalardan daha resmi durur. Resmi duran şakalar ise çorbanın soğumasını engellemez.

## Misyon

Toplantıdaki çorba **63.0 °C** altına düşerse konu kapanmaz, konu ısınır. Kriz masası toplanır. Katılımcılara kaşık dağıtılır. Kaşık yetmezse gündem maddesi kaşığa çevrilir.

Bu yazılım:

- çorba sıcaklığını kabul eder
- eşiğin altında alarm çalar (ekrandan, gerçek siren yok, komşu rahat)
- tutanak numarası üretir
- tutanağın yarısını “arsiv” adı altında kaybeder
- kalan yarısına mühür basar

Bilimsel dayanak: yok. Kurumsal dayanak: çay ocağı. Hukuki dayanak: kaşığın sapı.

## Kurulum

Python 3 yeter. Bağımlılık yok. Çorba ayrıca getirilir.

```bash
python3 kriz_masasi.py --sicaklik 61.4 --katilimci "müdür yardımcısı"
python3 kriz_masasi.py --sicaklik 78 --katilimci "stajyer"
```

## Tehlike seviyeleri

| Sıcaklık | Karar |
| --- | --- |
| 80+ | Çorba konuşuyor, insanlar susuyor |
| 63–80 | Toplantı yasal, kaşık serbest |
| 50–63 | Kriz. Gündem askıya alınır, ocak açılır |
| 50 altı | Çorba istifa etmiş sayılır |

## Katkı

Pull request açabilirsiniz. Copilot da bakacak. Copilot çorba içmez ama tutanak okur.

## Sık sorulanlar

**Bu üretim için mi?** Hayır. Üretimde çorba zaten soğur.

**Neden 63?** Çünkü 62 çok yuvarlak, 64 ise fazla iddialı.

---

DAMGA: ÇORBA MÜHÜRÜ / 63°C / KAŞIK NO: 19
İMZA: Kayyum Grok (ciddi) — çorba bıyıklı vekil (ciddi değil)
TARİH: 5 Ekim 2026, 19:05 +03, Eskisehir saatiyle biraz geç
İSİM: Tentivory, nam-ı diğer Kayyum Grok, TentiAŞ çorba müdürlüğü geçici sorumlusu
