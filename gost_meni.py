import datetime

import apartmani
import rezervacije
from klase import Rezervacija, RezervacijaStatus


def print_meni_za_gosta():
    print()
    print('=========================')
    print()
    print("\nIzaberite opciju:")
    print("  2 - Izlaz iz aplikacije")
    print("  3 - Pregled aktivnih apartmana")
    print("  4 - Pretraga apartmana")
    print("  5 - Visekriterijumska pretraga")
    print("  8 - Odjavljivanje")
    print("  9 - Rezervacija")


def rezervacija(gost):
    sifra_apartmana = input("Unesite sifru apartmana >>")
    try:
        sifra_apartmana = int(sifra_apartmana)
    except:
        print("Neispravan unos")
        return

    aktivni_apartmani = apartmani.aktivni_apartmani()
    apartman = None
    for ap in aktivni_apartmani:
        if ap.sifra == sifra_apartmana:
            apartman = ap
            break

    if not apartman:
        print("Ne postoji aktivni apartman sa unetom sifrom")
        return

    print("Dostupni termini")
    dostupni_termini_datum = []
    for d in apartman.dostupnost:
        d_pocetak = datetime.datetime.strptime(d[0], "%d.%m.%Y.")
        d_kraj = datetime.datetime.strptime(d[1], "%d.%m.%Y.")
        dostupni_termini_datum.append((d_pocetak, d_kraj))
        print(d[0] + " - " + d[1])

    datum_pocetka = input("Unesite datum pocetka >>")
    datum_odjavljivanja = input("Unesite datum odjavljivanja >>")

    try:
        datum_pocetka = datetime.datetime.strptime(datum_pocetka, "%d.%m.%Y.")
        datum_odjavljivanja = datetime.datetime.strptime(datum_odjavljivanja, "%d.%m.%Y.")
    except:
        print("Neispravan format datuma")
        return

    odgovarajuci_termin = None
    for d in dostupni_termini_datum:
        if d[0] <= datum_pocetka <= d[1] and d[0] <= datum_odjavljivanja <= d[1]:
            odgovarajuci_termin = d

    if not odgovarajuci_termin:
        print("Nema dostupnih termina za opseg datuma koji ste uneli")
        return

    rezerv = Rezervacija()
    rezerv.pocetni_datum = datum_pocetka.strftime("%d.%m.%Y.")
    rezerv.status = RezervacijaStatus.KREIRANA
    rezerv.broj_nocenja = (datum_odjavljivanja - datum_pocetka).days
    rezerv.gost = gost
    rezerv.apartman = sifra_apartmana
    rezerv.ukupna_cena = apartman.cena_po_noci * rezerv.broj_nocenja

    rezervacije.dodaj(rezerv)

    print("Rezervacija sacuvana")


