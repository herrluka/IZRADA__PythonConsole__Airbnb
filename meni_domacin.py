import datetime

import apartmani
import lokacija
import rezervacije
import sadrzaj
from klase import TipApartman, ApartmanStatus, Apartman


def print_meni_za_domacina():
    print()
    print('=========================')
    print()
    print("\nIzaberite opciju:")
    print("  2 - Izlaz iz aplikacije")
    print("  3 - Pregled aktivnih apartmana")
    print("  4 - Pretraga apartmana")
    print("  5 - Visekriterijumska pretraga")
    print("  8 - Odjavljivanje")
    print("  12 - Dodavanje apartmana")
    print("  13 - Izmena apartmana")
    print("  14 - Birsanje apartmana")
    print("  15 - Pregled rezervacija")


def dodavanje_apartmana(domacin):
    tip = input("Unesite tip >> ")
    try:
       tip_enum = TipApartman.from_str(tip)
    except:
        print("Neispravan tip")
        return

    try:
        broj_soba = int(input("Unesite broj soba >> "))
    except:
        print("Neispravan unos")
        return

    try:
        broj_gostiju = int(input("Unesite broj gostiju >> "))
    except:
        print("Neispravan unos")
        return

    lokacije = lokacija.sve_lokacije()

    print("{:<10} {:<20} {:<20} {:<80}".format("Redni broj", "Geografska sirina", "Geografska duzina", "Adresa"))
    i = 0
    for lo in lokacije:
        print("{:<10} {:<20} {:<20} {:<80}".format(i, lo.geografska_sirina, lo.geografska_duzina, lo.adresa.ulica + " " + lo.adresa.broj + ", " + lo.adresa.postanski_broj + ", " + lo.adresa.naseljeno_mesto))
        i += 1


    try:
        lok = int(input("Unesite redni broj lokacije >> "))
        if lok < 0 or lok >= len(lokacije):
            print("Neispravan unos")
            return
    except:
        print("Neispravan unos")
        return

    try:
        cena_po_noci = int(input("Unesite cenu po noci >> "))
    except:
        print("Neispravan unos")
        return

    print("Unesite termine tako sto unosite pocetni datum, a zatim krajnji datum. Unos prekidate unosenjem vrednosti X")
    unos_datuma = '1'
    termini = []

    while unos_datuma != 'X':
        try:
            unos_datuma = input("Pocetni datum >>")
            if unos_datuma != 'X':
                pocetni_datum = datetime.datetime.strptime(unos_datuma, '%d.%m.%Y.')
                unos_datuma = input("Krajnji datum >>")
                if unos_datuma != 'X':
                    krajnji_datum = datetime.datetime.strptime(unos_datuma, '%d.%m.%Y.')
                    if pocetni_datum >= krajnji_datum:
                        print('Pocetni datum mora da bude pre krajnjeg')
                        continue

                    termini.append((pocetni_datum.strftime('%d.%m.%Y.'), krajnji_datum.strftime('%d.%m.%Y.')))
        except:
            print('Neispravan unos')

    sadrzaji_lista = sadrzaj.svi_sadrzaji()
    i = 0
    print("{:<10} {:<20} {:<20}".format("Redni broj", "Sifra", "Naziv"))
    for sad in sadrzaji_lista:
        print("{:<10} {:<20} {:<20}".format(i, sad.sifra, sad.naziv))
        i += 1

    print("Unesite sadrzaje odabirom rednog broja. Unos prekidate unosenjem vrednosti X")
    odabrani_sadrzaj = []
    dodati_redni_brojevi = []
    uneti_rb_sadrzaja = '1'

    while uneti_rb_sadrzaja != 'X':
        try:
            uneti_rb_sadrzaja = input("Redni broj >>")
            if uneti_rb_sadrzaja == 'X':
                continue

            uneti_rb_sadrzaja = int(uneti_rb_sadrzaja)
            if uneti_rb_sadrzaja in dodati_redni_brojevi:
                print("Vec ste izabrali uneti sadrzaj")
                continue

            odabrani_sadrzaj.append(sadrzaji_lista[uneti_rb_sadrzaja])
            dodati_redni_brojevi.append(uneti_rb_sadrzaja)
        except:
            print('Neispravan unos')

    apartman = Apartman()
    apartman.sifra = int(round(datetime.datetime.now().timestamp()))
    apartman.tip = tip_enum
    apartman.broj_soba = broj_soba
    apartman.broj_gostiju = broj_gostiju
    apartman.lokacija = lokacije[lok]
    apartman.dostupnost = termini
    apartman.domacin = domacin
    apartman.cena_po_noci = cena_po_noci
    apartman.status = ApartmanStatus.NEAKTIVAN
    apartman.sadrzaji = odabrani_sadrzaj
    apartmani.dodaj_apartman(apartman)

    print("Uspsno sacuvan novi apartman")


def izmena_apartmana():
    try:
        sifra_apartmana = int(input("Unesite sifru apartmana >> "))
    except:
        print('Neispravan unos')
        return

    ap = apartmani.apartman_po_sifri(sifra_apartmana)
    if not ap:
        print('Apartman nije pronadjen')
        return

    tip = input("Unesite tip (trenutno: " + ap.tip.value + ") >> ")
    if tip:
        try:
            tip_enum = TipApartman.from_str(tip)
            ap.tip = tip_enum
        except:
            print("Neispravan tip")
            return

    status = input("Unesite status (trenutno: " + ap.status.value + ") >> ")
    if status:
        try:
            staus_enum = ApartmanStatus.from_str(status)
            ap.status = staus_enum
        except:
            print("Neispravan status")
            return

    broj_soba = input("Unesite broj soba (trenutno: " + str(ap.broj_soba) + ") >> ")
    if broj_soba:
        try:
            broj_soba = int(broj_soba)
            ap.broj_soba = broj_soba
        except:
            print("Neispravan unos")
            return

    broj_gostiju = input("Unesite broj gostiju (trenutno: " + str(ap.broj_gostiju) + ") >> ")
    if broj_gostiju:
        try:
            broj_gostiju = int(broj_gostiju)
            ap.broj_gostiju = broj_gostiju
        except:
            print("Neispravan unos")
            return

    lokacije = lokacija.sve_lokacije()

    print("{:<10} {:<20} {:<20} {:<80}".format("Redni broj", "Geografska sirina", "Geografska duzina", "Adresa"))
    i = 0
    for lo in lokacije:
        print("{:<10} {:<20} {:<20} {:<80}".format(i, lo.geografska_sirina, lo.geografska_duzina,
                                                   lo.adresa.ulica + " " + lo.adresa.broj + ", " + lo.adresa.postanski_broj + ", " + lo.adresa.naseljeno_mesto))
        i += 1

    lok = input("Unesite redni broj lokacije >> ")
    if lok:
        try:
            lok = int(lok)
            if lok < 0 or lok >= len(lokacije):
                print("Neispravan unos")
                return

            ap.lokacija = lokacije[lok]
        except:
            print("Neispravan unos")
            return

    cena_po_noci = input("Unesite cenu po noci (trenutno: " + str(ap.cena_po_noci) + ") >> ")
    if cena_po_noci:
        try:
            cena_po_noci = int(cena_po_noci)
            ap.cena_po_noci = cena_po_noci
        except:
            print("Neispravan unos")
            return

    print("Unesite termine tako sto unosite pocetni datum, a zatim krajnji datum. Unos prekidate unosenjem vrednosti 0")
    odobrenje = input("Za izmenu dostupnosti, unesite bilo koji karakter a zatim kliknite enter >>")
    if odobrenje:
        termini = []
        unos_datuma = "1"
        while unos_datuma != 'X':
            try:
                unos_datuma = input("Pocetni datum >>")
                if unos_datuma != 'X':
                    pocetni_datum = datetime.datetime.strptime(unos_datuma, '%d.%m.%Y.')
                    unos_datuma = input("Krajnji datum >>")
                    if unos_datuma != 'X':
                        krajnji_datum = datetime.datetime.strptime(unos_datuma, '%d.%m.%Y.')
                        if pocetni_datum >= krajnji_datum:
                            print('Pocetni datum mora da bude pre krajnjeg')
                            continue

                        termini.append((pocetni_datum.strftime('%d.%m.%Y.'), krajnji_datum.strftime('%d.%m.%Y.')))
            except:
                print('Neispravan unos')

        ap.dostupnost = termini

    sadrzaji_lista = sadrzaj.svi_sadrzaji()
    i = 0
    print("{:<10} {:<20} {:<20}".format("Redni broj", "Sifra", "Naziv"))
    for sad in sadrzaji_lista:
        print("{:<10} {:<20} {:<20}".format(i, sad.sifra, sad.naziv))
        i += 1

    print("Unesite sadrzaje odabirom rednog broja. Unos prekidate unosenjem vrednosti 0")
    odobrenje = input("Za izmenu dostupnosti, unesite bilo koji karakter a zatim kliknite enter >>")
    if odobrenje:
        odabrani_sadrzaj = []
        dodati_redni_brojevi = []
        uneti_rb_sadrzaja = '1'
        while uneti_rb_sadrzaja != 'X':
            try:
                uneti_rb_sadrzaja = input("Redni broj >>")
                if uneti_rb_sadrzaja == 'X':
                    continue

                uneti_rb_sadrzaja = int(uneti_rb_sadrzaja)
                if uneti_rb_sadrzaja in dodati_redni_brojevi:
                    print("Vec ste izabrali uneti sadrzaj")
                    continue

                odabrani_sadrzaj.append(sadrzaji_lista[uneti_rb_sadrzaja])
                dodati_redni_brojevi.append(uneti_rb_sadrzaja)
            except:
                print('Neispravan unos')

        ap.sadrzaji = odabrani_sadrzaj

    apartmani.azuriraj(ap)

    print("Apartman je uspesno azuriran")


def brisanje_apartmana():
    print('************************')
    print("UPOZORENJE! OVA AKCIJA MOZE DA IZBRISE VAZNE PODATKE!")
    print('************************')

    try:
        sifra_apartmana = int(input("Unesite sifru apartmana >> "))
    except:
        print('Neispravan unos')
        return

    ap = apartmani.apartman_po_sifri(sifra_apartmana)
    if not ap:
        print('Apartman nije pronadjen')
        return

    apartmani.obrisi(ap)

    print("Uspesno obrisan")


def pregled_rezervacija(domacin):
    domacin_apartmani = apartmani.apartmani_domacin(domacin)
    lista = rezervacije.revervacije_domacin(domacin_apartmani)
    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
            "Apartman sifra",
            "status",
            "Gost",
            "Broj nocenja",
            "Ukupna cena",
            "Pocetni datum"))

    for r in lista:
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
            r.apartman,
            r.status.value,
            r.gost.ime + " " + r.gost.prezime,
            r.broj_nocenja,
            r.ukupna_cena,
            r.pocetni_datum
        ))

