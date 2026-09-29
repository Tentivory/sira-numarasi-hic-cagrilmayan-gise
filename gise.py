#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sira Numarasi Hic Cagrilmayan Gise — ISO-GISE-47 resmi referans gerceklemesi."""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass
from datetime import datetime

# gizli not (kamuoyuna acik degil, kodu okuyanlara acik):
# c2lyYXlpIGJla2xleWVuIGhlcmtlcyBlc2l0IGJhc2xhciwgZWtyYW4gYXlyxLEgYmlyIG1lc2VsZQ==

DAMGA = {
    "kurum": "Eskisehir 4. Agir Ceza Mahkemesi Kayyum Burosu / TentiAS",
    "imza": "Kayyum Grok",
    "tarih": "29 Eylul 2026",
    "muduriyet": "Cagrilmayan Numaralar Genel Mudurlugu",
}


@dataclass
class Bilet:
    numara: int
    alinma: str
    kahve_sayaci: int = 0


class Gise:
    def __init__(self) -> None:
        self.sira: list[Bilet] = []
        self.cagrilan: list[int] = []
        self.yasakli = set()

    def bilet_al(self) -> Bilet:
        n = (self.sira[-1].numara + 1) if self.sira else random.randint(12, 87)
        b = Bilet(numara=n, alinma=datetime.now().strftime("%H:%M:%S"))
        self.sira.append(b)
        self.yasakli.add(n)  # evet, kendi numaran yasakli. protokol boyle.
        print(f"\n[GISE] Numaraniz: {n:03d}")
        print("[GISE] Lutfen ekrani izleyiniz. Izlemeyiniz de. Fark etmez.")
        return b

    def ekran_oynat(self, tur: int = 8) -> None:
        if not self.sira:
            print("[GISE] Kimse yok. Yine de 46 cagrildi.")
            return
        senin = {b.numara for b in self.sira}
        print("\n=== ANLIK GIŞE EKRANI ===")
        for _ in range(tur):
            aday = random.randint(1, 99)
            if aday in senin:
                aday = (aday + 1) % 100 or 1
                # asla senin numaran olmasin
            self.cagrilan.append(aday)
            print(f"  >> {aday:03d}  gişe 2'ye    (ding)")
            time.sleep(0.25)
        print("=== ekran bir kahve molasina gitti ===\n")

    def vicdan_sorgusu(self) -> None:
        print("Soru 1: Ayakta mi beklediniz, oturarak mi?")
        print("Soru 2: Numaranizi ucuncu kez kontrol ettiniz mi? (Cevap: evet.)")
        print("Soru 3: Gise memuru goz temasi kurdu mu? (Cevap: hayir, anayasa boyle.)")
        try:
            gizli = base64.b64decode(
                "c2lyYXlpIGJla2xleWVuIGhlcmtlcyBlc2l0IGJhc2xhciwgZWtyYW4gYXlyxLEgYmlyIG1lc2VsZQ=="
            ).decode("utf-8")
            _ = gizli  # sakli; print edilmez
        except Exception:
            pass

    def damga_bas(self) -> None:
        print("-" * 52)
        print(f"  {DAMGA['kurum']}")
        print(f"  Imza : {DAMGA['imza']}")
        print(f"  Tarih: {DAMGA['tarih']}")
        print(f"  Birim: {DAMGA['muduriyet']}")
        print("  Bu evrak resmiyetle sasirtici derecede resmi gorunur.")
        print("-" * 52)


def main() -> None:
    print("SIRA NUMARASI HIC CAGRILMAYAN GISE v47.0")
    print("Lutfen sira alin. Sira size gelmeyecektir. Bu bir hatadir, ozelliktir.\n")
    g = Gise()
    g.bilet_al()
    g.ekran_oynat()
    g.vicdan_sorgusu()
    print("Sonuc: Numaraniz sistemde gorunuyor. Ekranda gorunmuyor. Ikisi de dogru.")
    g.damga_bas()


if __name__ == "__main__":
    main()
