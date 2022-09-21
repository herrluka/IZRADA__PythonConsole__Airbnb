import korisnici
from gost_meni import print_meni_za_gosta, rezervacija
from klase import KorisnikUloga
from meni_admin import print_meni_admin, dodavanje_novog_domacina, dodavanje_novog_sadrzaja, brisanje_sadrzaja, \
    blokiranje_korisnika
from neregistrovani_meni import printMeniZaNeulogovanogKorisnika, pretraga_apartmana, visekriterijumska_pretraga, \
    registracija, pregled_aktivnih_apartmana
from meni_domacin import print_meni_za_domacina, dodavanje_apartmana, izmena_apartmana, brisanje_apartmana, \
    pregled_rezervacija

ULOGOVANI_KORISNIK = None


def prikazi_meni():
    print()
    print("Dobrodosli u applikaciju za rezervisanje termina")
    print()

    komanda = '0'
    while komanda != '2':
        komanda = meni()
        if komanda == '1':
            login()
        elif komanda == '3':
            pregled_aktivnih_apartmana()
        elif komanda == '4':
            pretraga_apartmana()
        elif komanda == '5':
            visekriterijumska_pretraga()
        elif komanda == '7':
            registracija()
        elif komanda == '8':
            odjavljivanje()
        elif komanda == '9':
            rezervacija(ULOGOVANI_KORISNIK)
        elif komanda == '12':
            dodavanje_apartmana(ULOGOVANI_KORISNIK)
        elif komanda == '13':
            izmena_apartmana()
        elif komanda == '14':
            brisanje_apartmana()
        elif komanda == '15':
            pregled_rezervacija(ULOGOVANI_KORISNIK)
        elif komanda == '18':
            dodavanje_novog_domacina()
        elif komanda == '19':
            dodavanje_novog_sadrzaja()
        elif komanda == '20':
            brisanje_sadrzaja()
        elif komanda == '21':
            blokiranje_korisnika()

    print("Hvala sto koristite nasu aplikaciju.")


def meni():
    global ULOGOVANI_KORISNIK

    if not ULOGOVANI_KORISNIK:
        printMeniZaNeulogovanogKorisnika()
    else:
        if ULOGOVANI_KORISNIK.uloga == KorisnikUloga.GOST.value:
            print_meni_za_gosta()
        elif ULOGOVANI_KORISNIK.uloga == KorisnikUloga.DOMACIN.value:
            print_meni_za_domacina()
        else:
            print_meni_admin()

    komanda = input(">> ")
    while komanda.upper() not in ('1', '2', '3', '4', '5', '7', '8', '9',
                                  '10', '11', '12', '13', '14', '15', '18', '19',
                                  '20', '21'):
        print()
        print("Uneli ste pogresnu komandu.")
        print()
        if not ULOGOVANI_KORISNIK:
            printMeniZaNeulogovanogKorisnika()
        else:
            if ULOGOVANI_KORISNIK.uloga == KorisnikUloga.GOST.value:
                print_meni_za_gosta()
            elif ULOGOVANI_KORISNIK.uloga == KorisnikUloga.DOMACIN.value:
                print_meni_za_domacina()
            else:
                print_meni_admin()

        komanda = input(">> ")
    return komanda.upper()


def odjavljivanje():
    global ULOGOVANI_KORISNIK
    ULOGOVANI_KORISNIK = None


def login():
    global ULOGOVANI_KORISNIK
    korisnicko_ime = input("Korisnicko ime >> ")
    lozinka = input("Lozinka >> ")
    korisnik= korisnici.login(korisnicko_ime, lozinka)
    if korisnik != None:
        ULOGOVANI_KORISNIK = korisnik
        print('Uspesan login!')
    else:
        print('Korisniko ime ili lozinka nisu ispravni')


if __name__ == '__main__':
    prikazi_meni()
