import apartmani
import korisnici
import sadrzaj
from klase import KorisnikUloga, Sadrzaj


def print_meni_admin():
    print()
    print('=========================')
    print()
    print("\nIzaberite opciju:")
    print("  2 - Izlaz iz aplikacije")
    print("  3 - Pregled aktivnih apartmana")
    print("  4 - Pretraga apartmana")
    print("  5 - Visekriterijumska pretraga")
    print("  8 - Odjavljivanje")
    print("  18 - Registracija novih domacina")
    print("  19 - Dodavanje novog sadrzaja")
    print("  20 - Brisanje sadrzaja")
    print("  21 - Blokiranje korisnika")


def dodavanje_novog_domacina():
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
        korisnici.registracija(ime, prezime, korisnicko_ime, lozinka, kontakt_telefon, email, pol, KorisnikUloga.DOMACIN.value)
    except Exception as e:
        print(str(e))


def dodavanje_novog_sadrzaja():
    sifra = input('Unesite sifru sadrzaja >>')
    if not sifra:
        print('Sifra je obavezna')
        return

    try:
        sifra = int(sifra)
    except:
        print("Neispravan format sifre")

    naziv = input('Unesite naziv sadrzaja >>')
    if not naziv:
        print('Naziv je obavezan')
        return

    try:
        sad = Sadrzaj()
        sad.sifra = sifra
        sad.naziv = naziv
        sadrzaj.dodaj_sadrzaj(sad)
        print('Uspesno sacuvano')
    except Exception as e:
        print(str(e))


def brisanje_sadrzaja():
    print('************************')
    print("UPOZORENJE! OVA AKCIJA MOZE DA IZBRISE VAZNE PODATKE!")
    print('************************')

    sifra = input('Unesite sifru sadrzaja >>')
    if not sifra:
        print('Sifra je obavezna')
        return

    try:
        sifra = int(sifra)
    except:
        print("Neispravan format sifre")

    svi_apartmani = apartmani.svi_apartmani()
    for ap in svi_apartmani:
        for sadr in ap.sadrzaji:
            if sadr.sifra == sifra:
                print("Postoji aparman sa ovim sadrzajem. Brisanje nije dozvoljeno")
                return

    sadrzaj.brisanje(sifra)


def blokiranje_korisnika():
    korisnicko_ime = input('Unesite korisnicko ime korisnika kog zelite da blokirate >>')
    if not korisnicko_ime:
        print('Unos korisnickog imena je obavezan')
        return

    korisnici.blokiraj_korisnika(korisnicko_ime)
