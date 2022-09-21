import apartmani
import korisnici
from klase import KorisnikUloga


def printMeniZaNeulogovanogKorisnika():
    print()
    print('=========================')
    print()
    print("\nIzaberite opciju:")
    print("  1 - Prijava na sistem")
    print("  2 - Izlaz iz aplikacije")
    print("  3 - Pregled aktivnih apartmana")
    print("  4 - Pretraga apartmana")
    print("  5 - Visekriterijumska pretraga")
    print("  7 - Registracija")


def pretraga_apartmana():
    print('Izaberite tip pretrage:')
    print('a - mesto')
    print('b - vreme dostupnost (pre unetog datuma)')
    print('c - vreme dostupnost (nakon unetog datuma)')
    print('d - broj soba (manje od)')
    print('e - broj soba (vece od)')
    print('f - cena (manje od)')
    print('g - cena (vece od)')
    vrsta_pretrage = input("Tip pretrage >> ")
    if vrsta_pretrage not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        print('Pogresan unos')
    else:
        tekst = input("Tekst >> ")
        try:
            lista = apartmani.pretrazi(vrsta_pretrage, tekst)
            print_naslov_tabele_apartmani()
            for a in lista:
                print_apartmana(a)
        except:
            print('Neispravan unos')


def visekriterijumska_pretraga():
    pretraga_mesto = input("Unesite mesto >> ")
    pretraga_vreme_pre = input("Unesite vreme dostupnost (pre unetog datuma) >> ")
    pretraga_vreme_posle = input('Unesite vreme dostupnost (nakon unetog datuma) >>')
    pretraga_broj_soba_manje = input('Unesite broj soba (manje od) >>')
    pretraga_broj_soba_vece = input('Unesite broj soba (vise od) >>')
    pretraga_cena_manje = input('Unesite cenu (manje od) >>')
    pretraga_cena_vece = input('Unesite cenu (vise od) >>')

    try:
        lista = apartmani.visekriterijumska_pretraga(pretraga_mesto, pretraga_vreme_pre, pretraga_vreme_posle,
                                                     pretraga_broj_soba_manje, pretraga_broj_soba_vece,
                                                     pretraga_cena_manje, pretraga_cena_vece)
        print_naslov_tabele_apartmani()
        for a in lista:
            print_apartmana(a)
    except:
        print('Neispravan unos')


def registracija():
    ime = input("Unesite ime >> ")
    if not ime:
        print('Ime je obavezno')
        return
    prezime = input("Unesite prezime >> ")
    if not prezime:
        print('Prezime je obavezno')
        return
    korisnicko_ime = input('Unesite korisnicko ime >>')
    if not korisnicko_ime:
        print('Korisnicko ime je obavezno')
        return
    lozinka = input('Unesite lozinku >>')
    if not lozinka:
        print('Lozinka je obavezna')
        return
    kontakt_telefon = input('Unesite kontakt telefon >>')
    if not kontakt_telefon:
        print('Telefon je obavezan')
        return
    email = input('Unesite email >>')
    if not email:
        print('Email je obavezan')
        return
    pol = input('Unesite pol >>')
    if not pol:
        print('Pol je obavezan')
        return

    try:
        korisnici.registracija(ime, prezime, korisnicko_ime, lozinka, kontakt_telefon, email, pol, KorisnikUloga.GOST.value)
    except Exception as e:
        print(str(e))


def pregled_aktivnih_apartmana():
    akt = apartmani.aktivni_apartmani()
    print_naslov_tabele_apartmani()
    for apartman in akt:
        print_apartmana(apartman)


def print_naslov_tabele_apartmani():
    print("{:<50} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<50} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<20}".format(
        "Sifra",
        "Tip",
        "Broj soba",
        "Broj gostiju",
        "Lokacija",
        "Cena po noci",
        "Status",
        "Domacin",
        "Sadrzaj",
        "Dostupnost"
    ))


def print_apartmana(apartamn):
    sadrzaj = ""
    for s in apartamn.sadrzaji:
        sadrzaj += s.naziv + ","

    if sadrzaj:
        sadrzaj = sadrzaj[:-1]

    dostupnost = ""
    for d in apartamn.dostupnost:
        dostupnost += d[0] + " - " + d[1] + "|"

    if dostupnost:
        dostupnost = dostupnost[:-1]

    print("{:<50} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<50} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<20} "
          "{:<20}".format(
        apartamn.sifra,
        apartamn.tip.value,
        apartamn.broj_soba,
        apartamn.broj_gostiju,
        "{} {} {}".format(apartamn.lokacija.adresa.ulica, apartamn.lokacija.adresa.broj, apartamn.lokacija.adresa.naseljeno_mesto),
        apartamn.cena_po_noci,
        apartamn.status.value,
        apartamn.domacin.ime + " " + apartamn.domacin.prezime,
        sadrzaj,
        dostupnost))
