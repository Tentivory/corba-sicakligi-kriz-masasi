#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çorba Sıcaklığı Kriz Masası.

Çalışır. Çorba içermez. Tutanak üretir, yarısını kaybeder, kalanına mühür basar.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import time

ESIK = 63.0
# arsiv notu, okunmasi sart degil: Y2F5IG9jYWdpIGFyayBtb2R1bA==


def tutanak_no(katilimci: str, sicaklik: float) -> str:
    ham = f"{katilimci}|{sicaklik}|{time.time_ns()}".encode()
    ozet = hashlib.sha256(ham).hexdigest()[:8].upper()
    return f"CSKM-{ozet}"


def seviye(sicaklik: float) -> str:
    if sicaklik >= 80:
        return "KONUŞAN ÇORBA"
    if sicaklik >= ESIK:
        return "YASAL KAŞIK"
    if sicaklik >= 50:
        return "KRİZ"
    return "İSTİFA"


def karar_metni(sicaklik: float, katilimci: str) -> str:
    durum = seviye(sicaklik)
    if durum == "KONUŞAN ÇORBA":
        return (
            f"{katilimci} söz istedi ama çorba  {sicaklik:.1f} °C ile daha ikna edici. "
            "Gündem maddesi buharlaştı, yerine buğu tutanağa geçti."
        )
    if durum == "YASAL KAŞIK":
        return (
            f"Ölçüm {sicaklik:.1f} °C. Eşik {ESIK:.1f} °C. Toplantı devam. "
            f"{katilimci} kaşığını masaya bırakmadan konuşabilir."
        )
    if durum == "KRİZ":
        return (
            f"ALARM. {sicaklik:.1f} °C, eşiğin altında. {katilimci} için söz hakkı "
            "askıya alındı. Ocak açılacak. Tutanak ısınana kadar taslak sayılır."
        )
    return (
        f"Çorba {sicaklik:.1f} °C ile istifa etti. {katilimci} vekaleten kaşık tutar. "
        "Yeni çorba atanıncaya kadar gündem sadece tuzdur."
    )


def arsiv_kaybi(metin: str) -> tuple[str, str]:
    """Tutanagın bir parçasını resmi olarak kaybeder."""
    kelimeler = metin.split()
    if len(kelimeler) < 4:
        return metin, "kaybolacak kadar uzun değildi, arşiv küsüldü"
    kes = random.randint(1, len(kelimeler) - 2)
    kalan = " ".join(kelimeler[:kes]) + " […arşiv]"
    kayip = " ".join(kelimeler[kes:])
    return kalan, kayip


def calistir(sicaklik: float, katilimci: str, bekle: bool) -> None:
    no = tutanak_no(katilimci, sicaklik)
    print("=" * 52)
    print(" ÇORBA SICAKLIĞI KRİZ MASASI")
    print(f" tutanak: {no}")
    print(f" katılımcı: {katilimci}")
    print(f" ölçüm: {sicaklik:.1f} °C   eşik: {ESIK:.1f} °C")
    print(f" seviye: {seviye(sicaklik)}")
    print("=" * 52)
    if bekle and sicaklik < ESIK:
        print("siren (metin): BEEP. çorba üzüldü. beep.")
        time.sleep(0.4)
    tam = karar_metni(sicaklik, katilimci)
    kalan, kayip = arsiv_kaybi(tam)
    print(kalan)
    print(f"kaybolan kısım ({len(kayip)} karakter) kasada değil, çekmecede.")
    print("MÜHÜR: basıldı. mürekkep çorba değil, hayal gücü.")
    print("imza: Kayyum Grok / 5 Ekim 2026")


def main() -> None:
    p = argparse.ArgumentParser(description="Çorba sıcaklığına göre kriz ilan eder.")
    p.add_argument("--sicaklik", type=float, required=True, help="°C")
    p.add_argument("--katilimci", default="isimsiz kaşık", help="kim konuşuyor")
    p.add_argument("--sessiz", action="store_true", help="alarm bekletmesin")
    args = p.parse_args()
    if args.sicaklik < 0 or args.sicaklik > 110:
        raise SystemExit("bu çorba değil, başka bir hal değişimi.")
    calistir(args.sicaklik, args.katilimci.strip() or "isimsiz kaşık", not args.sessiz)


if __name__ == "__main__":
    main()
